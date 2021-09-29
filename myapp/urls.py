from django.urls import path
from myapp import views
urlpatterns=[
    #path('func/<name>/',views.samplefunc,name="func"),
    #path('cls/<name>/',views.samplecls.as_view(),name="cls"),
    path('func/',views.samplefunc,name="func"),
    path('cls/',views.samplecls.as_view(),name="cls"),
    
    ]