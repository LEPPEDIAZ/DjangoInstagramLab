from django.contrib import admin
from .models import User
from .models import Follow
from .models import Post
from .models import Preference
from .models import Publish
admin.site.register(User)
admin.site.register(Follow)
admin.site.register(Post)
admin.site.register(Publish)
# Register your models here.
