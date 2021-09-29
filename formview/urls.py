from django.urls import path
from formview import views
import formview
appname = formview
urlpatterns=[
    path('form/',views.Formview.as_view(),name="formview"),
    path('list/',views.Listview.as_view(),name="listview"),
    path('details/<pk>/',views.detailsview.as_view(),name="detailsview"),
    path('create/',views.createview.as_view(),name="createview"),
    path('update/<pk>/',views.updateview.as_view(),name="updateview"),
    path('delete/<pk>/',views.deleteview.as_view(),name="deleteview")
]