from email.utils import localtime
from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.


# Neighbourhood Model Tests
class LocalityTestClass(TestCase):
    def setUp(self):
        # create an admin user
        self.admin = User.objects.create_superuser(
            username='maureen',
            password='maureen'
        )
        self.locality =  Locality(
            name='Test  Locality', location=self.location, occupants_count=10, admin_id=self.admin.id)
    
    def test_instance(self):
        self.assertTrue(isinstance(self. local,  Locality))

    def test_save_method(self):
        self. locality.create_ locality()
        localities =  Locality.objects.all()
        self.assertTrue(len( localities) > 0)

    def test_delete_method(self):
        self. locality.create_ locality()
        self. locality.delete()
        localities =  Locality.objects.all()
        self.assertTrue(len( localities) == 0)
        
        
      