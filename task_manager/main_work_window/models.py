from django.db import models

class Task(models.Model):
    title = models.TextField('Назва')
    task_description = models.TextField('Опис завдання')
    collaborators = models.TextField('Працівники')
    status = models.TextField('Статус')
    priority = models.TextField('Пріорітет')
    budget = models.TextField('Бюджет')
    attachments = models.FileField(upload_to='documents/')
    dead_line = models.DateField('Дедлайн')

    def __str__(self):
        return self.title