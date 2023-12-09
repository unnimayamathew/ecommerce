from django.contrib import admin
from .models import category,product

# Register your models here.

class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,categoryadmin)


class productadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','availables','created','updated']
    list_editable = ['price','stock','availables']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(product,productadmin)

