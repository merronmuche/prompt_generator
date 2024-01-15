from django.db import models

class Prompt(models.Model):
    input_text = models.TextField()
    length_of_line = models.IntegerField(null=True)
    generated_prompt = models.TextField(null=True)

    def __str__(self):
        return f"Prompt: {self.input_text[:50]}..."  # Display first 50 characters
