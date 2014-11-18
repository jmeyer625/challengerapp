from django.contrib import admin
from challengerapp.models import Challenge, Day, Task, Post

# admin.AdminSite.site_header = 'Challenger admin'

# Register your models here.

class DayInline(admin.TabularInline):
	model = Day
	extra = 1

class ChallengeAdmin(admin.ModelAdmin):
	inlines = [DayInline]
	list_display = ('title', 'pub_date')
	list_filter = ['pub_date']

admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Day)
admin.site.register(Task)
admin.site.register(Post)