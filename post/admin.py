from django.contrib import admin
from .models import Post, Personas
# Register your models here.

# Admin es lo que controla la parte de atrás de la web.

admin.site.register(Post)
admin.site.register(Personas)
