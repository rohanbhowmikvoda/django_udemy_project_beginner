from django.urls import path
from myapp import views

app_name = 'myapp' #Application Namespace

urlpatterns = [
    path('index/', views.index,name='index'),
    # path('item/', views.item),
    path('detail/<int:id>/', views.detail,name='detail'),
]
