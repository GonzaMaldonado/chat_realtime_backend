from django.db import models
from users.models import User


class Room(models.Model):
  name = models.CharField(max_length=50)
  user = models.ForeignKey(User, related_name="user_rooms",on_delete=models.CASCADE)
  likes = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-id']

  def __str__(self):
      return self.name


class Like(models.Model):
   user = models.ForeignKey(User, related_name="user_likes", on_delete=models.CASCADE)
   room = models.ForeignKey(Room, related_name="room_likes", on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)

   class Meta:
      # Especifica que la combinación de los campos user y room debe ser única en la base de datos.
      # O sea que un usuario pueda dar Like solo una vez a una Room.
      unique_together = ('user', 'room')

   def __str__(self) -> str:
      return f'Like: {self.user.username} a {self.room.name}'
   

class Message(models.Model):
   room = models.ForeignKey(Room, related_name="room_messages", on_delete=models.CASCADE)
   user = models.ForeignKey(User, related_name="user_messages", on_delete=models.CASCADE)
   content = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self) -> str:
      return f'{self.content[:10]}'
