from django.shortcuts import render
from users.views import login_required, get_current_user

# Create your views here.

def main(request):
    return render(request, "main.html")

@login_required
def index(request):
    user = get_current_user(request)
    context = {
        'user': user,
    }
    return render(request, "index.html", context)
