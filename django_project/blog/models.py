from django.db import models
# we import a timezone method to post the date
from django.utils import timezone
# we import the user model from django
from django.contrib.auth.models import User
from django.urls import reverse

# we create a new Post model


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
