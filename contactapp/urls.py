from django.urls import path
from .import views

urlpatterns=[
    path('',views.home),
    path('add',views.addcontact),
    path('view',views.display),
    path('del',views.delete),
    path('upd',views.update),

]
