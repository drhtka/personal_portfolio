from django.db import models

class Blog(models.Model):

    class Meta:
        db_table = 'blog'
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'
        ordering = ['-id']

    title = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Описание',)
    date = models.DateField('Дата',)

    def __str__(self):
        return self.title