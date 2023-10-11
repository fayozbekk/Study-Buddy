from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('room-detail/<int:pk>', room_detail, name='room-detail'),
    path('profile/<int:pk>', profile, name='profile'),
    path('create-room/', create_room, name="create-room"),
    path('update-room/<str:pk>', update_room, name='update-room'),
    path('delete-message/<str:pk>', delete_message, name='delete-message'),
    path('delete-room/<str:pk>', delete_room, name='delete-room'),
    path('create-category/', create_category, name='create-category'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('reg/', registration_user, name='registration'),
    path('categories/', categories, name='cats'),
]
