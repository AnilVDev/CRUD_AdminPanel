from django.contrib import admin
from app1.models import Custom_user

# Register your models here.
admin.site.register(Custom_user)



def __str__(self):
    return f"Username: {self.username}, First Name: {self.first_name}, Email: {self.email}"
