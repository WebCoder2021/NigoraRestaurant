from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Special)
admin.site.register(Chefs)
admin.site.register(Events)
admin.site.register(SayingAbout)
admin.site.register(Gallery)
admin.site.register(Message)