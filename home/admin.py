from django.contrib import admin
from home.models import Consejos,Aboutus, Banner, Collaborators, Documents


@admin.register(Consejos)
class ConsejosAdmin(admin.ModelAdmin):
    list_display = ('name','user','type_consejo')

@admin.register(Aboutus)
class AboutusAdmin(admin.ModelAdmin):
    list_display = ('name','description')
  
@admin.register(Collaborators)
class CollaboratorsAdmin (admin.ModelAdmin):
    list_display = ('firstname','lastname', 'position','get_type_consejo' )
    
    def get_type_consejo(self,obj):
        return obj.consejo.name
    get_type_consejo.short_description = 'Consejo'

@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')
   
admin.site.register(Banner)

