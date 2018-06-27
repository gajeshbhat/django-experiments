import sys
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class Upload(models.Model):
    Name = models.CharField(max_length = 140,blank=False,null=True)
    uploadedImage =  models.ImageField(upload_to = 'Upload/',blank=False,null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.uploadedImage = self.compressImage(self.uploadedImage)
        super(Upload, self).save(*args, **kwargs)

    def compressImage(self,uploadedImage):
        imageTemproary = Image.open(uploadedImage)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (1020,573) ) # Resize can be set to various varibale values in settings.py
        imageTemproary.save(outputIoStream , format='JPEG', quality=60) # change quality according to requirement.
        outputIoStream.seek(0)
        uploadedImage = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % uploadedImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return uploadedImage