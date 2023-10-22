from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_name/', views.add_name, name='add_name'),
    path('add_rule/', views.add_rule, name='add_rule'),
    path('secret_santa/', views.secret_santa, name='secret_santa'),
    path('delete_name/<int:name_id>/', views.delete_name, name='delete_name'),
    path('delete_rule/<int:rule_id>/', views.delete_rule, name='delete_rule'),
]
