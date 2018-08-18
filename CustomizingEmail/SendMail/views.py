from django.shortcuts import render
from SendMail.forms import sendMessageForm
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def getFeildText(request,feildName):
	dataForm = sendMessageForm(request.POST,request.FILES)
	feildText = str(dataForm[feildName])
	return feildText

def isFormValid(request):
	dataForm = sendMessageForm(request.POST,request.FILES)
	if dataForm.is_valid():
		return True
	return False

def getForm(request):
	return sendMessageForm(request.POST,request.FILES)

def getEmailReciever(request):
	return getFeildText(request,'Email')

def sendMessageEmail(request):
	mailReciever = getEmailReciever(request)
	mailMessage = getFeildText(request,'Message')
	sendDemoMail(mailMessage,mailReciever)

def displaySendPage(request):
	if request.method == 'POST':
		if isFormValid(request):
			sendDemoMail(request)
			dbSaveForm = getForm(request)
			dbSaveForm.save()
			return
	return render(request,'SendMail/Page.html',{'sendMessageForm':sendMessageForm})

def sendDemoMail(text):
	subject = 'This is Demo!'
	html_message = render_to_string('SendMail/CustomAlert.html', {'message': text})
	plain_message = strip_tags(html_message)
	from_email = 'From <localhost@example.com>'
	to = 'test@example.com'
	mail.send_mail(subject,plain_message,from_email,[to],html_message=html_message)
