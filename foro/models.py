from django.db import models
from users.models import User


class Room(models.Model):
  name = models.CharField(max_length=50)
  user = models.ForeignKey(User, related_name="users",on_delete=models.CASCADE)
  like = models.ManyToManyField(User, related_name="likes", default=None, blank=True)

  @property
  def num_like(self):
     return self.like.all().count()

  class Meta:
    ordering = ['-id']

  def __str__(self):
      return self.name


LIKE_CHOICES = (
   ('Like', 'Like'),
   ('Unlike', 'Unlike')
)

class Like(models.Model):
   user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
   room = models.ForeignKey(Room, related_name="room", on_delete=models.CASCADE)
   value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=6)

class Message(models.Model):
   room = models.ForeignKey(Room, related_name="messages", on_delete=models.CASCADE)
   user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
   content = models.TextField()