
from django.shortcuts import render, redirect
from .models import Prompt

from utils.prompt_gen import get_prompt

def generate_prompt(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        length_of_line = request.POST.get('length_of_line')

        generated_prompt = get_prompt(input_text, length_of_line)

        Prompt.objects.create(input_text=input_text, generated_prompt=generated_prompt, length_of_line=length_of_line)

        return render(request, 'prompt_app/prompt_result.html', {'generated_prompt': generated_prompt})

    return render(request, 'prompt_app/generate_prompt.html')


