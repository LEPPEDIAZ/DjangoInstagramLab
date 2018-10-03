from django.contrib import admin
from .models import USER
from .models import FOLLOW
from .models import POST
from .models import LIKE
from .models import NOLIKE
from .models import Publicar



admin.site.register(USER)
admin.site.register(FOLLOW)
admin.site.register(POST)
admin.site.register(Publicar)
admin.site.register(LIKE)
admin.site.register(NOLIKE)

# Register your models here.
