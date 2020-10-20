from django.contrib import admin
from rrps_web.models import EightClassAdmission,SevenClassAdmission,SixthClassAdmission,NinethClassAdmission,TenthClassAdmission,Announcement
# Register your models here.

class SixthClassAdmissionAdmin(admin.ModelAdmin):



    search_fields = ['Student_Name','Caste']

    list_filter = ['Caste']

    list_display = ['Student_Name','Caste']

    list_editable = ['Caste']


admin.site.register(SixthClassAdmission,SixthClassAdmissionAdmin)
admin.site.register(SevenClassAdmission)
admin.site.register(EightClassAdmission)
admin.site.register(NinethClassAdmission)
admin.site.register(TenthClassAdmission)
admin.site.register(Announcement)
