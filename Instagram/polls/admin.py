from django.contrib import admin
from .models import User
from .models import Follow
from .models import Post
from .models import Preference
from .models import Publish
from .models import Like
from .models import Likebyme
admin.site.register(User)
admin.site.register(Follow)
admin.site.register(Post)
admin.site.register(Publish)
admin.site.register(Like)
admin.site.register(Likebyme)
# Register your models here.
