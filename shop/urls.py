from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('product/',views.product,name='product'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('search/',views.search,name='search'),
    path('products/<int:myid>/', views.productView, name='productView'),
    path('handlerequest/',views.handlerequest,name='handleRequest'),
    path('login/',views.login,name='login'),
    path('Registered/',views.register,name='Registered'),
    # path('tracker/',views.tracker,name='tracker'),
    
]