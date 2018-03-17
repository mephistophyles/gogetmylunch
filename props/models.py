import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# A Tag is used to add some more details to a prop
class Tag(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name


# A Flair is used to add more information to a user
class Flair(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name


class GGMLUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    flair = models.OneToOneField(Flair, null=True, on_delete=models.SET_NULL)
    win_count = models.IntegerField(default=0, null=False, blank=False)
    loss_count = models.IntegerField(default=0, null=False, blank=False)


@receiver(post_save, sender=User)
def create_ggmluser(sender, instance, created, **kwargs):
    if created:
        GGMLUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_ggmluser(sender, instance, **kwargs):
    instance.ggmluser.save()


class Prop(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    text = models.TextField(max_length=5000, blank=False, null=False)
    date_added = models.DateTimeField(default=datetime.datetime.now(), blank=False, null=False)
    taker_deadline = models.DateTimeField(blank=True, null=True)
    resolution_date = models.DateTimeField(blank=False, null=False)
    creator = models.OneToOneField(GGMLUser, blank=False, null=True, on_delete=models.SET_NULL, related_name='creator')
    takers = models.ManyToManyField(GGMLUser, blank=True, null=True)
    limit_takers = models.IntegerField(default=10)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    creator_won = models.BooleanField(blank=True)
    onion_hanger = models.BooleanField(default=False)

    def get_tags(self):
        return "\t".join([t.name for t in self.tags.all()])

    def get_takers(self):
        return "\t".join([t.user.username for t in self.takers.all()])

    def get_creator(self):
        if self.creator is not None:
            return self.creator.user.username
        return "something bad"
