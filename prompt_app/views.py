
from django.shortcuts import HttpResponse, render

from prompt_app.utils.prompt_gen import get_prompt
from .utils.embed_text import embed_text
from .utils.similarity import cosine_similarity

from .models import Prompt, TextChunk



# def generate_prompt(request):
#     if request.method == 'POST':
#         input_text = request.POST.get('input_text')
#         length_of_line = request.POST.get('length_of_line')
#         #embed the users prompt
#         embeded_question = embed_text([input_text])[0]
#         embeded_document_vectors = TextChunk.objects.all()
#         for embeded_document_vector in embeded_document_vectors:
#             similarity = cosine_similarity(embeded_question, embeded_document_vector.embed)
            
#             print(similarity)




# def generate_prompt(request):
#     if request.method == 'POST':
#         input_text = request.POST.get('input_text')
#         length_of_line = request.POST.get('length_of_line')
        
#         # Embed the user's prompt
#         embeded_question = embed_text([input_text])[0]

#         # Initialize variables to store the best match
#         highest_similarity = -1  # Start with a low value
#         best_document_vector = None

#         # Loop through each document vector
#         embeded_document_vectors = TextChunk.objects.all()
#         for embeded_document_vector in embeded_document_vectors:
#             similarity = cosine_similarity(embeded_question, embeded_document_vector.embed)
            
#             # Update if a higher similarity is found
#             if similarity > highest_similarity:
#                 highest_similarity = similarity
#                 best_document_vector = embeded_document_vector
                

#         if best_document_vector is not None:
#             # Assuming there is a method to generate prompt from a document vector
#             best_prompt = generate_prompt_from_vector(best_document_vector)
#             return best_prompt  # Or render it in your response
#         else:
#             return "No similar documents found."
        
    #     generated_prompt = get_prompt(input_text, length_of_line)

    #     Prompt.objects.create(input_text=input_text, generated_prompt=generated_prompt, length_of_line=length_of_line)

    #     return render(request, 'prompt_app/prompt_result.html', {'generated_prompt': generated_prompt})

    # return render(request, 'prompt_app/generate_prompt.html')


# def generate_prompt_from_vector(best_document_vector ):
#     # Replace 'correct_attribute' with the actual attribute name
#     text = getattr(best_document_vector , 'correct_attribute', 'Default text if attribute not found')

#     # Generate the prompt based on the extracted text
#     prompt = "Reflecting on the topic '{}', what are your thoughts?".format(text)

#     # Return the generated prompt
#     return prompt

def generate_prompt_from_vector(text_chunk):
    # Access the text from the 'chunk' attribute of the TextChunk instance
    text = text_chunk.chunk

    # Generate the prompt based on the extracted text
    prompt = "Considering the content: '{}', what insights can you derive?".format(text)

    # Return the generated prompt
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
                best_text_chunk = text_chunk

        if best_text_chunk is not None:
            generated_prompt = generate_prompt_from_vector(best_text_chunk)
            # return HttpResponse(generated_prompt)
            return render(request, 'prompt_app/prompt_result.html', {'generated_prompt': generated_prompt})
        else:
            return HttpResponse("No similar documents found.")
    else:
        return render(request, 'prompt_app/generate_prompt.html')
    
       





