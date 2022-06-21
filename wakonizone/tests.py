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
        
        
class BusinessTestCase(TestCase):
    '''
    setup
    '''
    def setUp(self):
        self.business = Business(name='boutique',image='cloudinary image',user='1',NeighborHood='1')
    '''
    test instance of business
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))
        '''
        test for save instance of business
        '''
    def test_save_business(self):
        self.business.save_business()
        name = Business.objects.all()
        self.assertTrue(len(name)>0)

class PostTestCase(TestCase):
    '''
    setup
    '''
    def setUp(self):
        self.post = Post(name='annual meeting',image='cloudinary image',user='1',Locality='1')
    '''
    test instance of post
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))
        '''
        test for save instance of business
        '''
    def test_save_post(self):
        self.post.save_post()
        name = Post.objects.all()
        self.assertTrue(len(name)>0)        