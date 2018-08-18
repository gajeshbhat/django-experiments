from SendMail.views import displaySendPage
from django.conf.urls import url, include

urlpatterns = [
  url(r'$',displaySendPage,name='Display the Email test send Page.s')
]
