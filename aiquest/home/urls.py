from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("cr-details/<int:pk>", views.ProductDetailsView.as_view(), name="cr_detail"),

    path("about_us/", views.about_us, name="about_us"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)