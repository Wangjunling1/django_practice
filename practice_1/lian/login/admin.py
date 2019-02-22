from django.contrib import admin
from .models import user,jiaoce,mianbaoce,mpvce,paoce,pikace,xinnengyuance,yueyece
# Register your models here.

class useradmin(admin.ModelAdmin):
    list_display=['username','email']

class shujuadmin(admin.ModelAdmin):
    list_display = ['id','carname','cardata','carurl','cartu','carjiage']

admin.site.register(user,useradmin)
admin.site.register(jiaoce,shujuadmin)
admin.site.register(mianbaoce,shujuadmin)
admin.site.register(mpvce,shujuadmin)
admin.site.register(paoce,shujuadmin)
admin.site.register(pikace,shujuadmin)
admin.site.register(xinnengyuance,shujuadmin)
admin.site.register(yueyece,shujuadmin)