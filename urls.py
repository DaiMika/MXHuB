# urls.py
from django.contrib import admin
from django.urls import path
from .views import course_list, course_detail, module_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', course_list, name="course_list"),
    path('courses/<int:course_id>/', course_detail, name="course_detail"),
    path('modules/<int:module_id>/', module_detail, name="module_detail"),
]

