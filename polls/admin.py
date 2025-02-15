from django.contrib import admin
from .models import Election, Candidate, Vote

class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 1
    readonly_fields = ['id']

class ElectionAdmin(admin.ModelAdmin):
    inlines = [CandidateInline]
    readonly_fields = ['id']

admin.site.register(Election, ElectionAdmin)
admin.site.register(Vote)