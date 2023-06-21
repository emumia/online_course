from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("course_details/",views.course_details, name="python_course"),
    path("dj_course/",views.dj_course_details, name="dj_course"),
    path("ml_course/",views.ml_course_details, name="ml_course"),
    path("dl_course/",views.dl_course_details, name="dl_course"),
    path("stat_course/",views.stat_course_details, name="stat_course"),
    path("data_analysis_course/",views.data_analysis_course_details, name="data_analysis_course"),
    path("big_data_course/",views.big_data_course_details, name="big_data_course"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)