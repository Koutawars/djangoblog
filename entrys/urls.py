from django.urls import path, include
from . import views

app_name = 'entrys'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:entryId>/', views.singleEntry, name='singleEntry'),
    path('<int:entryId>/comment', views.commentEntry, name='commentEntry')
]
