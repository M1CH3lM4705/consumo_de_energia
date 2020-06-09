from django.shortcuts import render

# Create your views here.

#Pagina inical do site
def pagInicio(request):
    return render(request, 'index.html')
