from django.db import models


# Create your models here.
class Logs(models.Model):
    action_choices = (('created', 'created'),
                      ('updated', 'updated'),
                      ('refresh', 'refresh'))

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    action = models.CharField('Action', max_length=10, choices=action_choices)
    url = models.CharField('URL', max_length=100)


class Pontaj(models.Model):
    objects = None
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
