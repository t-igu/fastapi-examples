from django.contrib import admin
from .models import TDepartment, TEmployee

class TDepartmentAdmin(admin.ModelAdmin):
    model = TDepartment
    list_display = ["name",]

class TEmployeeAdmin(admin.ModelAdmin):
    model = TEmployee
    list_display = ["name", "birthday"]

admin.site.register(TDepartment, TDepartmentAdmin)
admin.site.register(TEmployee, TEmployeeAdmin)

# admin.site.register(TDepartment)
# admin.site.register(TEmployee)
