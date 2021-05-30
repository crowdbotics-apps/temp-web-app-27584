from django.shortcuts import render

# Create your views here.

from home.models import CustomText, HomePage


def home(request):
    packages = [
	{'name':'django-allauth', 'url': 'https://pypi.org/project/django-allauth/0.38.0/'},
	{'name':'django-bootstrap4', 'url': 'https://pypi.org/project/django-bootstrap4/0.0.7/'},
	{'name':'djangorestframework', 'url': 'https://pypi.org/project/djangorestframework/3.9.0/'},
    ]
    context = {
        'customtext': CustomText.objects.first(),
        'homepage': HomePage.objects.first(),
        'packages': packages
    }
    return render(request, 'home/index.html', context)


import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from django_token.models import Token
from rest_framework.authtoken.models import Token

@csrf_exempt
def appleSignIn(request):
    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    usersID = request.POST.get('usersID')
    print("user id",usersID)
    if not usersID:
        data = {'data' : { 'error' : 'Invalid User ID'}}
        return JsonResponse(data)
    from users.models import User
    try:
        obj = User.objects.get(usersID=usersID)
        # print("objects - -- -- -- ",obj)
        # UsersTokens = Token.objects.get(user = obj.)
        UToken = Token.objects.get(user=obj).key
        print("Token ",UToken)
        img = str(obj.image) 
        # print("Token found ------> ", UsersTokens)
        strToken = str(UToken)
        data = {'data' : { 'key':strToken, 'user' : { 'email':obj.email,'first_name':obj.first_name,'last_name':obj.last_name,'id':obj.id,'image':img,'premium_to':obj.premium_to,'is_coach':obj.is_coach} }}
        return JsonResponse(data)
    except Exception as e:
        
        # if request.POST.get('usersID') == "":
        #     print(" None user ")
        try:
            x = User.objects.get(email=email)
            print("User with this email already exist")
            if x:
                data = {'data' : { 'error' : 'User with this email already exists'}}
                return JsonResponse(data)
        except:
            pass
        obj = User.objects.create(email=email,first_name=first_name,last_name=last_name,usersID=usersID)
        T = Token.objects.create(user=obj)
        T.save()
        print("Token has been generated")
        tokenvalue = str(T)
        img = str(obj.image) 
        data = {'data' : { 'key':tokenvalue, 'user' : { 'email':obj.email,'first_name':obj.first_name,'last_name':obj.last_name,'id':obj.id,'image':img,'premium_to':obj.premium_to,'is_coach':obj.is_coach} }}
        print("data",data)
        return JsonResponse(data)

@csrf_exempt
def newResetPassword(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    from users.models import User
    details = []
    try:
        obj = User.objects.get(email=email)
        obj.set_password(password)
        obj.save()
        data = {'message':'Password has been reset successfully'}
        
        return JsonResponse(data)
    except Exception as e:
        # print("Exception")
        data = {'message':'Something went wrong'}
        return JsonResponse(data)


from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from users.models import User
from django.contrib import messages

def password_reset_done1(request):
    return render(request,"password_reset_done1.html")

@csrf_exempt
def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "main/password/password_reset_email1.txt"
                    c = {
                    "email":user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'Restoic',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'restoic',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'blindhelper2020@gmail.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
            else:
                messages.error(request, 'Account does not exist!')
                return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form":password_reset_form})
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form":password_reset_form})

import os
from django.http import HttpResponse
from django.utils.encoding import smart_str
# def sendjson(request):
#     os.system('python manage.py dumpdata > out.json')
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     # Define text file name
#     filename = 'out.json'
#     # Define the full file path
#     filepath = BASE_DIR + '/' + filename
#     # Open the file for reading content
#     path = open(filepath, 'r')
#     response = HttpResponse(path, content_type='application/force-download')
#     # Set the HTTP header for sending to browser
#     response['Content-Disposition'] = "attachment; filename=%s" % filename
#     # Return the response value
#     return response
def sendjson(request):
    from django.conf import settings
    from django.core.files import File
    db_path = settings.DATABASES['default']['NAME']
    dbfile = File(open(db_path, "rb"))
    # response = HttpResponse(dbfile, mimetype='application/x-sqlite3')
    response = HttpResponse(dbfile, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % db_path
    response['Content-Length'] = dbfile.size

    return response