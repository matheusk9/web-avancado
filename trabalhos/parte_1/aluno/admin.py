from django.contrib import admin
from .models import Matricula

# Register your models here.

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('nome','periodo_de_ingresso','nota')
    
admin.site.register(Matricula, MatriculaAdmin)
