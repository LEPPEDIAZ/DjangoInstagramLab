from django.contrib import admin
from .models import User
from .models import Follow
from .models import Post
from .models import Preference
admin.site.register(User)
admin.site.register(Follow)
admin.site.register(Post)
admin.site.register(Preference)
# Register your models here.
