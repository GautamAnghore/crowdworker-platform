from django.db import models


class Person(models.Model):

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    # person is a worker or a requester (w/r)
    who = models.CharField(max_length=1, choices=(('w', 'Worker'), ('r', 'Requester')))

    def is_worker(self):
        return self.who == 'w'

    def is_requester(self):
        return self.who == 'r'
