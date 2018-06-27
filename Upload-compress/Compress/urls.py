from django.conf.urls import url, include
from Compress.views import displayUploadedFiles , uploadImage

urlpatterns = [
url(r'^list/$',displayUploadedFiles,name='List Uploaded Images'),
url(r'^upload/$',uploadImage,name='Upload Images')
]