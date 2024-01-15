from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from prompt_app.views import generate_prompt
 
urlpatterns = [
    path('', generate_prompt, name='generate')
] 
