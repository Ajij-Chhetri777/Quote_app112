from django.contrib import admin
from app.models import Categories, Quote, Favourite

# Register your models here.

admin.site.register(Categories)
admin.site.register(Quote)
admin.site.register(Favourite)