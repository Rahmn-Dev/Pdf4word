from django.db import models

class Document(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/', max_length=255)
    word_file = models.FileField(upload_to='words/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)