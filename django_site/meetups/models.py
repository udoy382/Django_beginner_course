from django.db import models

# Create your models here.

# Username = admin
# Password = admin


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} ({self.address})'


class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
 

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    desc = models.TextField()
    image = models.ImageField(upload_to='images')
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # location = models.ManyToManyField(Location, blank=True)
    participant = models.ManyToManyField(Participant, blank=True)

    def __str__(self):
        return f'{self.title} - {self.slug}'