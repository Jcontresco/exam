from django.shortcuts import redirect, render
from apps.user.models import User

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        return render(request, 'wall/index.html')
    else:
        return redirect('/user')

def showUser(request, id):
    print('viewing', id, 'users page')
    user = User.objects.get(id=id)
    context= {
        'user': user
    }
    return render(request, 'wall/userprofile.html', context=context)

def dashboard(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'wall/dashboard.html', context=context)    

def wish(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'wall/wish.html', context=context)