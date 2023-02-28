from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.indexEN, name='indexEN'),
    path('hb/', views.indexHB, name='indexHB'),

    path('admin-panel/', views.admin, name='admin'),

    path('service/add/', views.addService, name='addService'),
    path('service/edit/<int:id>/', views.editService, name='editService'),
    path('service/delete/<int:id>/', views.delService, name='delService'),

    path('review/add/', views.addReview, name='addReview'),
    path('review/edit/<int:id>/', views.editReview, name='editReview'),
    path('review/delete/<int:id>/', views.delReview, name='delReview'),
    
    path('content/edit/', views.editContent, name='editContent'),
    
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)