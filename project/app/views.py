from django.shortcuts import render

from project.app.forms import UserForm

# Create your views here.
def index(request):
	return render(request, 'user/index.html')

def create(request):
    if request.method == 'GET':
        form = UserForm()

        context = {
            'form': form
        }

        
    return render(request, 'user/create.html', context=context)        