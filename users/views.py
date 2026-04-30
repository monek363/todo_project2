from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def register(request):
    context = {
        'errors': [],
        'username': '',
        'email': '',
    }

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if not username or not email or not password or not confirm_password:
            context['errors'].append('Будь ласка, заповніть всі поля.')
        elif password != confirm_password:
            context['errors'].append('Паролі не співпадають.')
        elif len(password) < 6:
            context['errors'].append('Пароль повинен містити щонайменше 6 символів.')
        elif User.objects.filter(username=username).exists():
            context['errors'].append('Користувач із таким іменем уже існує.')
        elif User.objects.filter(email=email).exists():
            context['errors'].append('Користувач із таким email уже зареєстрований.')
        else:
            user = User.objects.create(
                username=username,
                email=email,
                password=password,
            )
            request.session['user_id'] = user.id
            return redirect('profile')

        context['username'] = username
        context['email'] = email

    return render(request, 'register.html', context)

def login(request):
    return render(request, 'login.html')
