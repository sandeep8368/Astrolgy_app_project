from django.contrib import admin
from django.urls import path
from astroapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.display_view),
    path('contact/', views.Contact_view),
    path('about/', views.about_view),
]
