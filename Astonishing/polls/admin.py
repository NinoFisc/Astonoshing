from django.contrib import admin

from .models import Question,Topic,Customer

admin.site.register(Question)
admin.site.register(Topic)
admin.site.register(Customer)

# Register your models here.
