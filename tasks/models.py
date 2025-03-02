from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    is_completed = models.BooleanField(
        verbose_name='Завершена',
        default=False
    )
    created_at = models.DateTimeField(
        verbose_name='Создана',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    @classmethod
    def get_queryset(cls, request=None):
        return cls.objects.all()
