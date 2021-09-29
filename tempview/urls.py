from django.urls import path
from tempview import views
urlpatterns=[
    path('',views.Tempview.as_view(),name="tempview")
]