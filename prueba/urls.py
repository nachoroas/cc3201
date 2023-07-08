from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mayosql/', views.mayosql, name='mayosql'),
    path('mayo/', views.mayo, name='mayo'),
    path('mes/', views.mesa, name='mes'),
]