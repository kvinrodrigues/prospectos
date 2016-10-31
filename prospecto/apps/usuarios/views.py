from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
   text = """<h1>welcome to my app !</h1>

    <a> Inicio </a>









   """


   return HttpResponse(text)