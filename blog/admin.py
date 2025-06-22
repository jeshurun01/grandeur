from django.contrib import admin
from . import models

admin.site.site_header = "LA GRANDEUR"


admin.site.register(models.Notification)
admin.site.register(models.Feedback)
