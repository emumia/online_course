from django.contrib import admin
from . models import Course

# Register your models here.
@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ["id","title","type_of_course","fee_of_course","batch","discount_course","start_date_course","course_video_link","first_description","second_description","duration_of_course","class_time","teacher_name","teacher_image","image1_course","image2_course","post_date"]
