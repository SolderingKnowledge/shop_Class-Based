from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .forms import ContactForm, LoginForm, SignUpForm
from django.contrib.auth import logout

def index(request):
    return render(request, "index.html")


def location(request):
    return render(request, "locations.html")

def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content":" Hello this is contact page.",
        "form": contact_form,
    }
    if request.method == "POST":
        print(request.POST.get('name'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    return render(request, "contact.html", context)


User=get_user_model()
def user_sign_up(request):
    form = SignUpForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        return render(request, 'index.html')
    return render(request, 'sign_up.html', context)



def user_log_in(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form,
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print("Error")
    return render(request, 'log_in.html', context)


def user_log_out(request):
    logout(request)
    return render(request, 'log_in.html')
