from django.contrib import admin
from .models import Election, Candidate, Vote

class ElectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'start_date']
    search_fields = ('name',)
    readonly_fields = ['id']

class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name',)
    readonly_fields = ['id']

admin.site.register(Election, ElectionAdmin)
admin.site.register(Candidate, CandidateAdmin)