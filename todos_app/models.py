from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    active = models.IntegerField(default=1)
    creation_date = models.DateTimeField()
    
    def __unicode__(self):
        return self.username

class Task(models.Model):
    task = models.CharField(max_length=80)
    creation_date = models.DateTimeField()
    date = models.DateTimeField('date')
    active = models.IntegerField(default=1)
    id_user = models.ForeignKey(User)

    def __unicode__(self):
        return self.task