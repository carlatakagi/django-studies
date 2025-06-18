from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'user/index.html')

def create(request):
    return render(request, 'user/create.html')