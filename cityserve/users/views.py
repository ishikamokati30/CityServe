from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

def user_logout(request):
    logout(request)
    return redirect('/')

def login_redirect(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    elif request.user.is_staff:
        return redirect('/owner/dashboard/')
    else:
        return redirect('/')
    
def owner_only(user):
    return user.is_staff and not user.is_superuser


@user_passes_test(owner_only)
def owner_dashboard(request):
    return render(request, 'owner_dashboard.html')
# Create your views here.
