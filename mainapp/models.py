from django.db import models

# Create your models here.



class Map(models.Model):
    name = models.TextField()
    locations = models.ManyToManyField('Location', null = True, blank = True)
    def __str__(self):
        return self.name

class Location(models.Model):
    name= models.TextField()
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    tileorder = models.TextField()
    events = models.ManyToManyField('Event', null = True, blank = True)
    npcs = models.ManyToManyField('NPC', null = True, blank = True)
    def __str__(self):
        return f"{self.name},{self.id}"


class Event(models.Model):
    EVENT_CHOICES =(
        ("1", "TEXT"),
        ("2", "WARP"),
        ("3", "TALK"),
    )
    ORIENTATION_CHOICES =(
        ("1", "UP"),
        ("2", "RIGHT"),
        ("3", "DOWN"),
        ("4", "LEFT"),
    )
    type = models.CharField(max_length=1, choices = EVENT_CHOICES)
    text = models.TextField(null = True, blank = True)
    warpto = models.PositiveIntegerField(null = True, blank = True)
    warpx = models.PositiveIntegerField(default = 1)
    warpy = models.PositiveIntegerField(default = 1)
    warpor = models.CharField(max_length = 1, null = True, blank = True)

    def __str__(self):
        return f"{self.text},{self.type}"

class NPC(models.Model):
    NPC_CHOICES =(
        ("1", "WALK"),
        ("2", "STAY"),
        ("3", "SPIN"),
    )
    name= models.TextField()
    dialog = models.TextField()
    startposx = models.PositiveIntegerField(default = 1)
    startposy = models.PositiveIntegerField(default = 1)
    type = models.CharField(max_length=1, choices = NPC_CHOICES)
    startposex = models.CharField(max_length=5,default = 'down')
    starttop = models.PositiveIntegerField(default = 1)
    startleft = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return self.name
