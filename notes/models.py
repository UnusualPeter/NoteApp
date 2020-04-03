from django.db import models


# Create your models here.
class Notes(models.Model):
    title_note = models.CharField(max_length=100)
    content_note = models.TextField()
    created_note = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.search)

    class Meta:
        verbose_name_plural = 'Notes'
