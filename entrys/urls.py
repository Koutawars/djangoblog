from django.urls import path, include
from . import views

app_name = 'entrys'
urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('<int:pk>/', views.singleEntry.as_view(), name='singleEntry'),
    path('<int:entryId>/comment', views.commentEntry, name='commentEntry')
]
