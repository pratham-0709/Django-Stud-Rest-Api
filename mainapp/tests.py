from django.test import TestCase

from .models import StudentDetails


# Model Tests
class ModelTests(TestCase):
    def test(self):
        StudentDetails(name="demouser", mark1="60", mark2="60", mark3="80", total="200").save()
        swathy = StudentDetails.objects.get(name="demouser")
        self.assertEqual(swathy.name, "demouser")
        self.assertEqual(swathy.mark1, "60")
        self.assertEqual(swathy.total, "200")
