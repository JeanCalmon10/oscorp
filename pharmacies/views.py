from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from .models import Product

from .forms import LoginForm, RegistrationForm, ProductForm

from django.urls import reverse_lazy




# Create your views here.
def home(request):
    return render(request, 'pharmacies/index.html')


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bem vindo, {username}!")
                return redirect('pharmacies:home')
            else:
                error_message = "Login falhou. Por favor observe o seu usuário e senha."
                return render(request, 'pharmacies/login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'pharmacies/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'Você foi deslogado')
    return redirect('pharmacies:home')

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect back to the login page.
            return redirect('pharmacies:login')
    else:
        form = RegistrationForm()
    return render(request, 'pharmacies/register.html', {'form': form})

@login_required(login_url=reverse_lazy('pharmacies:login'))
def products(request):
    # If user is here, then user's connected.
    products = Product.objects.all()
    return render(request, 'pharmacies/products.html', {'products': products})

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  # Associate the current user with the product.
            product.save()
            messages.success(request, 'Produto salvo com sucesso')
            return redirect('pharmacies:products')
        else:
            messages.error(request, 'Por favor, entre com um produto corretamente')
    else:
        form = ProductForm()
    return render(request, 'pharmacies/create_product.html', {'form': form})

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso')
            return redirect('pharmacies:products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'pharmacies/edit_product.html', {'form': form, 'product': product})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Produto deletado com sucesso')
        return redirect('pharmacies:products')
    return render(request, 'pharmacies/delete_product.html', {'product': product})

def about_us(request):
    return render(request, 'pharmacies/about_us.html')

