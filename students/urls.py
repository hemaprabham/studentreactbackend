from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.viewall,name='viewall'),
    path('addall/',views.addall,name='addall'),
    path('delete/',views.delete,name='delete'),
    path('search/',views.search,name='search'),

]
