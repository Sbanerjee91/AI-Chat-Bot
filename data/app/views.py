from django.shortcuts import render
import json
import ollama
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def chat_interface(request):
    return render(request, 'app/index.html')

@csrf_exempt
def api_ask_ai(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_text = data.get('message', '')
        
        response = ollama.chat(model='llama3.2:1b', messages=[
            {'role': 'user', 'content': user_text}
        ])
        
        return JsonResponse({'reply': response['message']['content']})