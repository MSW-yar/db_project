from django.urls import path
from . import views
urlpatterns=[
    path('',views.get,name="index"),
    path('post',views.post),
    path('put',views.put)
]
