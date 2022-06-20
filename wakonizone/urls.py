from . import views
from django.urls import path

urlpatterns=[
    path('', views.index, name='index'),
    path('search/', views.search_hood, name='search_hoods'),
      
    path('profile/edit', views.EditProfile, name="editprofile"),
    
    path('local/<local_id>',views.local,name='local'),
    path('local/', views.add_locality, name='add_locality'),
    path('joinhood/<local_id>',views.join_hood,name="joinhood"),
    path('leavehood/<local_id>',views.leave_hood,name="leavehood"),
    path('addbusiness/<local_id>', views.createbusiness, name='createbusiness'),
    path('addpost/<local_id>', views.post, name='post'),

    path('police/', views.Police, name='police'),
    path('health/', views.Health, name='health'),

]    