from django.db import models
    # makemigrations creates changes and store them in a file
    # migrate apply those pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    number = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    # THe above function gives each contact form data a name as same as the person's name who submitted it