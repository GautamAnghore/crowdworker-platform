from django.db import models

class Person(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	country = models.CharField(max_length=50)
	phone = models.IntegerField(default=0)

class Worker(models.Model):
	worker = models.ForeignKey(Person)
	qualification = models.CharField(max_length=200)
	dob = models.DateTimeField('Date of birth')

class Requester(models.Model):
	requester = models.ForeignKey(Person)
