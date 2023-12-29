from django.shortcuts import render
from app.forms import VehicleForm, RegisterForm
from app.models import Vehicle
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required



# Create your views here.
@never_cache
@login_required
def home(request):
    vehicle = Vehicle.objects.all()
    user = request.user
    return render(request, 'app/home.html', {'vehicle':vehicle, 'user':user})

@never_cache
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            role = request.POST['roles']
            group = Group.objects.get(name=role)
            user = form.instance
            user.groups.add(group)
            messages.success(request, "Registration Successful")
            return redirect(reverse('login'))
    else:
        form = RegisterForm()
    return render(request, 'app/register.html', {'form':form})

@never_cache
def loginView(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in Successfully")
                    return redirect(reverse('home'))
        else:
            form = AuthenticationForm()
        return render(request, 'app/login.html', {'form':form})
    else:
        return redirect(reverse('home'))

def logoutView(request):
    logout(request)
    return redirect(reverse('login'))


@login_required
@permission_required('app.add_vehicle', raise_exception=True)
@never_cache
def add(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Vehicle data Added")
            return redirect(reverse('home'))
    else:
        form = VehicleForm()
    return render(request, 'app/add.html', {'form':form})


@login_required
@permission_required('app.change_vehicle', raise_exception=True)
@never_cache
def update(request, pk):
    if request.method == 'POST':
        a = Vehicle.objects.get(id=pk)
        b = VehicleForm(request.POST, instance=a)
        if b.is_valid():
            b.save()
            messages.success(request, "Data Updated Successfully")
            return redirect(reverse('home'))
    else:
        a = Vehicle.objects.get(id=pk)
        b = VehicleForm(instance=a)
    return render(request, 'app/update.html', {'form':b, 'pk':pk})


@login_required
@permission_required('app.delete_vehicle', raise_exception=True)
def delete(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    vehicle.delete()
    messages.success(request, "Vehicle data Deleted Successfully")
    return redirect(reverse('home'))



