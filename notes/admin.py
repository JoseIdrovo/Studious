from django.contrib import admin

# Register your models here.
from .models import Event
from .models import Meeting
from .models import Note

admin.site.register(Event)
admin.site.register(Meeting)
admin.site.register(Note)