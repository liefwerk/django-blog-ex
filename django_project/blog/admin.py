from django.contrib import admin
from .models import Post

admin.site.register(Post)

# my_site = Site.objects.get(pk=1)
# my_site.domain = 'localhost'
# my_site.name = 'localhost'
# my_site.save()
