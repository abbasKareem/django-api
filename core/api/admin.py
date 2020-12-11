from django.contrib import admin

from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_image')
    list_display_links = ('user',)
    list_per_page = 10
    search_fields = ('user','bio')


admin.site.register(Profile, ProfileAdmin)



# class ExperienceAdmin(admin.ModelAdmin):
#     list_display = ('title', 'company', 'location', 'from_date', 'to_date', 'current', 'description')
#     list_display_links = ( 'company',)
#     list_per_page = 10
#     search_fields = ('title',)


# admin.site.register(Experience, ExperienceAdmin)


# class EducationAdmin(admin.ModelAdmin):
#     list_display = ('school', 'degree')
#     list_display_links = ('school',)
#     list_per_page = 10
#     search_fields = ('school',)


# admin.site.register(Education, EducationAdmin)


# class SocialAdmin(admin.ModelAdmin):
#     list_display = ('youtube', 'facebook')
#     list_display_links = ('youtube', 'facebook')
#     list_per_page = 10
#     search_fields = ('youtube', 'facebook')


# admin.site.register(Social, SocialAdmin)


