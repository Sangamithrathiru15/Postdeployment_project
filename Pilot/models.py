from django.db import models

# Create your models here.
class FileUpload(models.Model):
    title=models.CharField(max_length=50)
    uploaded_date=models.DateTimeField()
    files=models.FileField(upload_to="uploaded_files/")

    
