from django.test import TestCase
from django.urls import reverse
from .models import Course

class CourseModelTest(TestCase):
    def setUp(self):
        # Create a course instance for testing
        self.course = Course.objects.create(
            title='Introduction to Python',
            description='Learn the basics of Python programming.',
            duration=10,
        )

    def test_course_creation(self):
        # Test if the course is created correctly
        self.assertEqual(self.course.title, 'Introduction to Python')
        self.assertEqual(self.course.description, 'Learn the basics of Python programming.')
        self.assertEqual(self.course.duration, 10)

    def test_course_str(self):
        # Test the string representation of the course
        self.assertEqual(str(self.course), 'Introduction to Python')

class CourseViewTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title='Introduction to Python',
            description='Learn the basics of Python programming.',
            duration=10,
        )

    def test_course_list_view(self):
        response = self.client.get(reverse('course_list'))  
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Introduction to Python')
        self.assertTemplateUsed(response, 'courses/course_list.html')  
    def test_course_detail_view(self):
        response = self.client.get(reverse('course_detail', args=[self.course.id]))  
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Learn the basics of Python programming.')
        self.assertTemplateUsed(response, 'courses/course_detail.html')  

