from django.contrib import admin

from .models import Idea, Topic, Creator

admin.site.register(Idea)
admin.site.register(Topic)
admin.site.register(Creator)
