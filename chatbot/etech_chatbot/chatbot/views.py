from django.shortcuts import render
from django.http import JsonResponse
import openai
#import dotenv

openai_api_key = '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'
openai.api_key = openai_api_key
#env_vars = dotenv.dotenv_values()
#openai.api_key = env_vars['OPENAI_SECRET_KEY']

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    return answer
 
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')