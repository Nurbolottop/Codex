from django.contrib import admin
from  .models import User,Blog,SportBlog,BussnuiseBlog

# Register your models here.
admin.site.register(User)
admin.site.register(Blog)
admin.site.register(SportBlog)
admin.site.register(BussnuiseBlog)

