from django.shortcuts import render
from django.http import JsonResponse
from .utils import run_assistant

def start_assistant(request):
    print("Starting assistant from view...")
    response = run_assistant()
    return JsonResponse({"status": "Assistant started", "response": response})

def index(request):
    return render(request, "assistant/index.html")