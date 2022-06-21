from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver


class Locality(models.Model):
    locality_name = models.CharField(max_length=50)
    description = models.CharField(max_length = 200,null = True)
    occupants = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    police_num=models.IntegerField(null=True,blank=True)
    hospital_num=models.IntegerField(null=True,blank=True)
    location = models.CharField(max_length = 50,null = True)

    def create_locality(self):
        self.save()

    @classmethod
    def delete_locality(cls, id):
        cls.objects.filter(id=id).delete()


    # find neighbourhood by id
    @classmethod
    def find_locality(cls, id):
        hood = cls.objects.get(id=id)
        return hood
    
    def __str__(self):
        return self.locality_name
    

#User Model
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image')
    fullname = models.CharField(max_length=500, blank=True, null=True)
    bio = models.CharField(max_length=500, blank=True, null=True)
    phone_number= models.CharField(max_length=50, blank=True, null=True)
    localty = models.ForeignKey(Locality, on_delete=models.CASCADE,null=True)


    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    def __str__(self):
        return str(self.user)
    
# business class model
class Business(models.Model):
    business_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    description = models.CharField(max_length = 200,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # locality = models.ForeignKey(Locality, on_delete=models.CASCADE)
    business_pic = CloudinaryField('image', blank=True, null=True)
    
    def __str__(self):
        return self.business_name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self):
        self.update()

    @classmethod
    def search_by_business(cls, search_term):
      business_name = cls.objects.filter(business_name__icontains=search_term)
      return business_name
 

class Post(models.Model):
    title = models.CharField(max_length=50,blank=True)
    post_pic = CloudinaryField('image')
    description = models.CharField(max_length = 150,null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # neighbourhood = models.ForeignKey(Locality, on_delete=models.CASCADE, default=1)
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def get_locality_posts(cls,id):
        posts = Post.objects.filter(id = id)
        return posts