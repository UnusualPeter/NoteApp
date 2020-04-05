from django.db import models
from django.utils import timezone


# Create your models here.
class Notes(models.Model):
    # Create the fields for the database
    # Then python manage.py makemigrations Notes
    # Then python manage.py migrate
    title_note = models.CharField(max_length=100, verbose_name='Title')
    content_note = models.TextField(verbose_name='Content')
    pub_date = models.DateTimeField(verbose_name='Date published')

    # This returns the title note on the admin and the shell
    def __str__(self):
        return '{}'.format(self.title_note)

    # This sets the correct plural for the Notes, if is not initially accurate
    class Meta:
        verbose_name_plural = 'Notes'
