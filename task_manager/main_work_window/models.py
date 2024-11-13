from django.db import models

class Task(models.Model):
    title = models.TextField('Назва')
    task_description = models.TextField('Опис завдання')
    collaborators = models.TextField('Працівники')
    status = models.TextField('Статус')
    priority = models.TextField('Пріорітет')
    budget = models.TextField('Бюджет')
    attachments = models.FileField(upload_to='documents/', blank=True, null=True)
    dead_line = models.DateField('Дедлайн')

    def __str__(self):
        return self.title

class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    title = models.TextField('Назва підзавдання')
    task_description = models.TextField('Опис підзавдання')
    collaborators = models.TextField('Працівники')
    status = models.TextField('Статус')
    priority = models.TextField('Пріорітет')
    budget = models.TextField('Бюджет')
    attachments = models.FileField(upload_to='documents/', blank=True, null=True)
    dead_line = models.DateField('Дедлайн')

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField('Текст коментаря')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]