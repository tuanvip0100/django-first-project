from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, render
from polls import services
from django.forms.models import model_to_dict
from django.core import serializers
import json

from polls.models import User
from .forms import NameForm, LoginForm, ChangeName, SignIn


def index(request):
    if request.POST:
        print(0)
    latest_user = User.objects.order_by('user_name')
    context = {'latest_user_list': latest_user}
    return render(request, 'polls/index.html', context)


def detail(request, user_id):
    question = get_object_or_404(User, pk=user_id)
    return render(request, 'polls/detail.html', {'question': question})


def user_name(request, user_id):
    user = User.objects.get(id=user_id)
    return HttpResponse("%s" % user.user_name)


def do_something(request):
    latest_user = User.objects.order_by('user_name')
    context = {'latest_user_list': latest_user}
    return render(request, 'polls/index.html', context)


def test_request(request):
    if request.POST:
        do_something(request)
    else:
        return render(request, 'polls/post.html')


def post_form(request):
    form = NameForm()
    return render(request, 'name.html', {'form': form})


def get_name(request):
    print(1000)
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get("user_name"))
            return HttpResponse("Correct post request")
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})


def login_page(request):
    form = LoginForm()
    if 'user_name' in request.session:
        current_user = request.session['user_name']
        return HttpResponse("Already logged in!, noted current user is %s" % current_user, )
    return render(request, "login_page.html", {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("user_name")
            password = form.cleaned_data.get("password")
            print(name, password)
            if services.is_user_ex(name) is True:
                if services.check_password(name, password) is True:
                    request.session['user_name'] = name
                    request.session.set_expiry(300)
                    return HttpResponse("Login success!")
            return HttpResponse("Wrong user name or password!")
        else:
            return HttpResponse("Wrong user name or password!")
    else:
        return HttpResponse("Wrong user name or password!")


def logout(request):
    request.session.clear()
    form = LoginForm()
    return render(request, "login_page.html", {'form': form})


def get_detail(request):
    if 'user_name' in request.session:
        current_user = request.session['user_name']
        data = services.get_detail(current_user).as_json()
        return HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponse("Unauthorized user!")


def change_user_name_view(request):
    form = ChangeName()
    return render(request, "change_user_name_page.html", {'form': form})


def change_user_name(request):
    if 'user_name' in request.session:
        if request.method == 'POST':
            form = ChangeName(request.POST)
            if form.is_valid():
                current_user = request.session['user_name']
                new_name = form.cleaned_data.get('user_name')
                services.change_user_name(current_user, new_name)
                request.session['user_name'] = new_name
                request.session.modified = True
                return HttpResponse("change current user name success!")
            else:
                return HttpResponse("not valid form!")
        else:
            return HttpResponse("method type error!")
    else:
        form = LoginForm()
        return render(request, "login_page.html", {'form': form})


def sign_in_view(request):
    form = SignIn()
    return render(request, "sign_in.html", {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = SignIn(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get("user_name")
            password = form.cleaned_data.get("password")
            email = form.cleaned_data.get("email")
            age = form.cleaned_data.get("age")

            if services.sign_in(services.set_person(user_name, password, email, age)):
                return HttpResponse("sign in success!")
            return HttpResponse("sign in failure!")
        return HttpResponse("sign in failure!")
    return HttpResponse("sign in failure!")


def get_all_person(request):
    if 'user_name' in request.session:
        name = request.session['user_name']
        if services.is_admin(name) is False:
            return HttpResponse('admin permission is required')
    objects = services.get_all_person()
    results = [ob.as_json() for ob in objects]
    return HttpResponse(json.dumps(results), content_type="application/json")


def delete_person(request, user_id):
    if 'user_name' in request.session:
        name = request.session['user_name']
        if services.is_admin(name) is False:
            return HttpResponse('admin permission is required')
        if services.delete_person(user_id) is True:
            return HttpResponse("delete person success!")
        else:
            return HttpResponse("request failure!")
    form = LoginForm()
    return render(request, "login_page.html", {'form': form})
