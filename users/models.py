from django.db import models
from django.contrib.auth.models import User
from PIL import Image  # from pillow import image


class Profile(models.Model):  # there are two attributes of profile database, which are user and image
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # a User has one user
    # here one to one relationship between user and profile picture, CASCADE means if i delete the user then profile pic is deleted or if delete the profile pic then user is deleted
    image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')  # imagefield is built in django for image

    def __str__(self):
        return f'{self.user.username} Profile'  # here the dunder string which shows f string one time (username)

# after models create to store its on datatbase, make migrations
    def save(self):  # this method using for resizing image
        super().save()  # run save method with parent class which is called super

        img = Image.open(self.image.path)  # image path stores in img variable

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)  # the image save on this type of format (300 by 300)
            img.save(self.image.path)
