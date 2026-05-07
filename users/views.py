from django.shortcuts import render, redirect
from .models import User
from functools import wraps

# Create your views here.

def get_current_user(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            pass
    return None

def login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not get_current_user(request):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

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
            user.set_password(password)
            user.save()
            request.session['user_id'] = user.id
            return redirect('profile')

        context['username'] = username
        context['email'] = email

    return render(request, 'register.html', context)

def login(request):
    context = {
        'errors': [],
        'username': '',
    }

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if not username or not password:
            context['errors'].append('Будь ласка, заповніть всі поля.')
        else:
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    request.session['user_id'] = user.id
                    return redirect('profile')
                else:
                    context['errors'].append('Невірний пароль.')
            except User.DoesNotExist:
                context['errors'].append('Користувач із таким іменем не знайдений.')

        context['username'] = username

    return render(request, 'login.html', context)


def logout(request):
    request.session.flush()
    return redirect('main')