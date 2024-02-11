from django.contrib import admin
from first_app.models import Topic,WebPage,AccessReocrd

# Register your models here.

admin.site.register(AccessReocrd)
admin.site.register(Topic)
admin.site.register(WebPage)

