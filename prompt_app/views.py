
from django.shortcuts import HttpResponse, render

from prompt_app.utils.prompt_gen import get_prompt
from .utils.embed_text import embed_text
from .utils.similarity import cosine_similarity

from .models import Prompt, TextChunk



def generate_prompt_from_vector(text_chunk, user_question):

    prompt = text_chunk + " \n based on the above data, give an answer to \
            the following question. restrict yourself to the above data only. \
            if you can't get an answer based on the data, you can feel free to \
                say i don't know. here is the question. \n" + user_question +\
                 "DONOT add anything from yourself."
    return prompt



def generate_prompt(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')

        # Embed the user's input
        embeded_question = embed_text([input_text])[0]

        highest_similarity = -1
        best_text_chunk = None

        # Compare with embeddings in TextChunk objects
        for text_chunk in TextChunk.objects.all():
            similarity = cosine_similarity(embeded_question, text_chunk.embed)

            if similarity > highest_similarity:
                highest_similarity = similarity
                best_text_chunk = text_chunk.chunk

        if best_text_chunk is not None:
            generated_prompt = generate_prompt_from_vector(best_text_chunk, input_text)
            # return HttpResponse(generated_prompt)
            return render(request, 'prompt_app/prompt_result.html', {'generated_prompt': generated_prompt})
        else:
            return HttpResponse("No similar documents found.")
    else:
        return render(request, 'prompt_app/generate_prompt.html')
    
       





