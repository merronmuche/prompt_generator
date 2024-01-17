

from django.db import models

class Prompt(models.Model):
    input_text = models.TextField()
    length_of_line = models.IntegerField(null=True)
    generated_prompt = models.TextField(null=True)

    def __str__(self):
        return f"Prompt: {self.input_text[:50]}..."  # Display first 50 characters
    

class Document(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')
    chunks = models.JSONField(blank=True, null=True) 
    embeds = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"PDF File uploaded on {self.created_at}"
