from django.shortcuts import render
from Compress.models import Upload
from Compress.forms import imageUploadForm


def displayUploadedFiles(request):
	uploadImageList = Upload.objects.all()
	return render(request, 'Compress/list.html', {'uploadImageList': uploadImageList})

def uploadImage(request):
	imageUploadFormResult = imageUploadForm(request.POST, request.FILES)
	if request.method == 'POST':
		if imageUploadFormResult.is_valid():
			imageUploadFormResult.save()
		else:
			return render(request, 'Compress/list.html', {'imageUploadFormResult': imageUploadFormResult})
	return render(request, 'Compress/upload.html', {'imageUploadFormResult': imageUploadFormResult})


