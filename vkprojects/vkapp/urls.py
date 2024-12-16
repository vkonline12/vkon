from .import views
from django.urls import path
app_name='vkapp'
urlpatterns = [
    path('',views.myworks,name='myworks'),
    path('details/',views.details,name='details'),
    path('add/',views.add,name='add'),
    path('spef_det/<int:id>/',views.spef_det,name='spef_det'),
    path('my_detail/<int:id>/',views.my_detail,name='my_detail')
]