
from django.urls import path
from .views import *


from rest_framework.routers import DefaultRouter

app_name = 'home'


#------------Default Router------------
router = DefaultRouter()
router.register(r'to-do-view-set', TodoViewSet, basename='todo')
#------------Default Router End------------


#http://127.0.0.1:8000/to-do-view-set/get_timing_todo/
#http://127.0.0.1:8000/to-do-view-set/add_date_to_todo/




urlpatterns = [
    path('', home, name='home'),
    path('post_todo/', post_todo, name='post_todo'),
    path('get_todo/', get_todo, name='get_todo'),
    path('patch_todo/', patch_todo, name='patch_todo'),
    
    
    
    #class bashed url
    path('TodoView/', TodoView.as_view()),
]


#------------Default Router------------
urlpatterns += router.urls
#------------Default Router ENd------------
