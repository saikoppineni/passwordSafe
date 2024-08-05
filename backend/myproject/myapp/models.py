from django.db import models

# Create your models here.
class NoteModel(models.Model):
    mainuser = models.CharField(max_length=20,default=True,null=False,unique=True)
    mainpass = models.CharField(max_length=20,blank=True,null=True)
    username = models.CharField(max_length=100,blank=True,null=True)
    password = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table='user'
        ordering=['mainuser']

        def __str__(self)->str:
            return self.username