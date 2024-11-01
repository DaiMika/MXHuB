from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Course, Module, Quiz

def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/course_list.html", {"courses": courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, "courses/course_detail.html", {"course": course})

def module_detail(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    return render(request, "courses/module_detail.html", {"module": module})
