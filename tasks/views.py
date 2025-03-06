from rest_framework import permissions, viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Task
from .serializers import TaskSerializer


class TaskPagination(PageNumberPagination):
    page_size_query_param = "page_size"


class TaskViewSet(viewsets.ModelViewSet):
    model = Task
    queryset = model.get_queryset()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = TaskPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        show_completed = self.request.query_params.get('show_completed', None)
        sort_order = self.request.query_params.get('sort_order', None)
        queryset = self.queryset.filter(
            author=self.request.user
        ).order_by(sort_order or '-created_at')

        if show_completed is not None and show_completed.lower() != 'true':
            queryset = queryset.filter(is_completed=False)

        return queryset
