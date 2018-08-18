from django.db import models

class SendMessage(models.Model):
	Message = models.CharField(max_length = 140,blank=False,null=True)
	Email = models.CharField(max_length = 140,blank=False,null=True)

