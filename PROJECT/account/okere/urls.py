from django.urls import path
from . import views
from .views import change_password
from django.contrib.auth import views as auth_views


urlpatterns = [
#    path('',views.public, name='public'),
    path('mis/',views.mis,name='mis'),
    path('MIS-login/',views.login_page, name='MIS-login'),
    path('signup/',views.sign_page, name='signup'),
    path('logout',views.logout_page, name='logout'),
    path('owner/',views.owner, name='owner'),
    path('change_password/', change_password, name='change_password'),


    path('change_password/',auth_views.PasswordChangeView.as_view, name='change_password'),

# ABOUT INFORMATION
    path('about_image/',views.about_image_page,name='about_image'),
    path('about_video/',views.about_video_page, name='about_video'),
    path('about_list/',views.about_list, name='about_list'),
    path("about_image_delete/<int:pk>/",views.about_image_delete, name='about_image_delete'),
    path('about_video_delete/<int:pk>/', views.about_video__delete, name='about_video_delete'),
    path('about_owner/',views.about_owner, name='about_owner'),
    path('about_image_rename/<int:pk>/',views.about_image_rename, name='about_image_rename'),
    path('about_video_rename/<int:pk>/', views.about_video_rename, name='about_video_rename'),

# SERVICE INFORMATION
    path('service_page/',views.service_page, name='service_page'),
    path('service_list/',views.service_list, name='service_list'),
    path('service_delete/<int:pk>/', views.service_delete, name='service_delete'),
    path('service_owner/',views.service_owner, name='service_owner'),
    path('service_rename/<int:pk>/', views.service_text_rename, name='service_rename'),

# NEWS INFORMATION
    path('news_image/',views.news_image_page,name='news_image'),
    path('news_video/',views.news_video_page, name='news_video'),
    path('news_list',views.news_list, name='news_list'),
    path('news_image_delete/<int:pk>/',views.news_image_delete,name='news_image_delete'),
    path('news_video_delete/<int:pk>/',views.news__video_delete, name='news_video_delete'),
    path('news_owner/',views.news_owner,name='news_owner'),
    path('news_image_rename/<int:pk>/', views.news_image_rename, name='news_image_rename'),
    path('news_video_rename/<int:pk>/', views.news_video_rename, name='news_video_rename'),

# SLIDE SHOW
    path('slide_upload/',views.slide_page,name='slide_upload'),
    path('',views.slide_list, name='slide'),
    path('slide_delete/<int:pk>/',views.slide_delete, name='slide_delete'),
    path('slide_owner/',views.slide_owner, name='slide_owner'),
    path('slide_rename/<int:pk>/', views.slide_rename, name='slide_rename'),

# TOURIST INFORMATION
    path('tourist_image/', views.tourist_image_page, name='tourist_image'),
    path('tourist_video/',views.tourist_video_page, name='tourist_video'),
    path('tourist_list/',views.tourist_list, name='tourist_list'),
    path('tourist_owner/', views.tourist_owner, name='tourist_owner'),
    path('tourist_image_delete/<int:pk>/',views.tourist_image_delete,name='tourist_image_delete'),
    path('tourist_video_delete/<int:pk>/',views.tourist_video_delete, name='tourist_video_delete'),
    path('tourist_image_rename/<int:pk>/', views.tourist_image_rename, name='tourist_image_rename'),
    path('tourist_video_rename/<int:pk>/', views.tourist_video_rename, name='tourist_video_rename'),

# FILES INFORMATION
    path('file_upload/',views.document_page, name='file_upload'),
    path('file_list/', views.document_list, name='file_list'),
    path('file_owner/',views.document_owner, name='file_owner'),
    path('open/<int:pk>/',views.view_document, name='open'),
    path('file_rename/<int:pk>/', views.document_rename, name='file_rename'),
    path('file_delete/<int:pk>/', views.document_delete, name='file_delete'),
    


]