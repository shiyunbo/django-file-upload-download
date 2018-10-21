from django.urls import re_path, path
from . import views

# namespace
app_name = "file_upload"

urlpatterns = [

    # Upload File Without Using Model Form
    re_path(r'^upload1/$', views.file_upload, name='file_upload'),

    # Upload Files Using Model Form
    re_path(r'^upload2/$', views.model_form_upload, name='model_form_upload'),

    # Upload Files Using Ajax Form
    re_path(r'^upload3/$', views.ajax_form_upload, name='ajax_form_upload'),

    # Handling Ajax requests
    re_path(r'^ajax_upload/$', views.ajax_upload, name='ajax_upload'),

    # View File List
    path('', views.file_list, name='file_list'),

]