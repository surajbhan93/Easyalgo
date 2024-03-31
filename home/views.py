from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect, get_object_or_404
from django.http import Http404
from home.models import Blog
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.db.models import Q
import random
import re
from home.forms import ContactForm
from django.contrib import messages
# from .models import ContactMessage
# from .forms import ContactForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout

# Create your views here.
def index (request):
    blogs = Blog.objects.all()
    random_blogs = random.sample(list(blogs), 3)
    context = {'random_blogs': random_blogs}
    return render(request, 'index.html', context)

def about (request):
    return render(request, 'about.html')

def thanks(request):
    return render(request, 'thanks.html')
def DSA1(request):
    return render(request,'DSA.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
def projects (request):
    return render(request, 'projects.html')

def project1(request):
    blogs = Blog.objects.all().order_by('-time')
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    context = {'blogs': blogs}
    return render(request, 'blog.html', context)

def category(request, category):
    category_posts = Blog.objects.filter(category=category).order_by('-time')
    if not category_posts:
        message = f"No posts found in category: '{category}'"
        return render(request, "category.html", {"message": message})
    paginator = Paginator(category_posts, 3)
    page = request.GET.get('page')
    category_posts = paginator.get_page(page)
    return render(request, "category.html", {"category": category, 'category_posts': category_posts})

def categories(request):
    all_categories = Blog.objects.values('category').distinct().order_by('category')
    return render(request, "categories.html", {'all_categories': all_categories})

def search(request):
    query = request.GET.get('q')
    query_list = query.split()
    results = Blog.objects.none()
    for word in query_list:
        results = results | Blog.objects.filter(Q(title__contains=word) | Q(content__contains=word)).order_by('-time')
    paginator = Paginator(results, 3)
    page = request.GET.get('page')
    results = paginator.get_page(page)
    if len(results) == 0:
        message = "Sorry, no results found for your search query."
    else:
        message = ""
    return render(request, 'search.html', {'results': results, 'query': query, 'message': message})


def blogpost (request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
        context = {'blog': blog}
        return render(request, 'blogpost.html', context)
    except Blog.DoesNotExist:
        context = {'message': 'Blog post not found'}
        return render(request, '404.html', context, status=404)

# def blogpost (request, slug):
#     blog = Blog.objects.filter(slug=slug).first()
#     context = {'blog': blog}
#     return render(request, 'blogpost.html', context)


# //login and sungup and logout __package__
def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        number = request.POST.get('number')
        password = request.POST.get('password')

        user = authenticate(request, username=number, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully logged in.")
            return redirect('/')
        else:
            messages.error(request, "Invalid number or password. Please try again.")
            return redirect('/login')

    return render(request, 'auth/login.html', {'messages': messages.get_messages(request)})

def signup(request):
        if request.user.is_authenticated:
                return  redirect('/')

        if request.method == 'POST':
                fname = request.POST['fname']
                lname = request.POST['lname']
                number = request.POST['number']
                email = request.POST['email']
                password = request.POST['password']
                cpassword = request.POST['cpassword']


                number_check = User.objects.filter(username=number).exists()
                email_check = User.objects.filter(email=email).exists()

                if number_check == True:
                        messages.error(request,"Your Number  Already Exists")
                        return redirect('/signup')

                if email_check == True:
                        messages.error(request,"Your Email Already Exists")
                        return redirect('/signup')


                if len(number) != 10:
                        messages.error(request,'Number Should Be 10 Digit')
                        return redirect('/signup')

                elif password != cpassword:
                        messages.error(request,"Password And Confirm Did'nt Match")
                        return redirect('/signup')

                else:
                        user = User.objects.create_user(username=number,email=email,password=cpassword)
                        user.first_name = fname
                        user.last_name = lname
                        user.save()
                        messages.success(request,"Your Account Successfully Created")
                        return redirect('/login')


        return render(request,'auth/signup.html')


def logout(request):
        auth_logout(request)
        messages.success(request,"Logout Succesfully")
        return redirect('/')

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'auth/password_reset.html'
    email_template_name = 'auth/password_reset_email.html'
    subject_template_name = 'auth/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('check-email')

    

def check_email_view(request):
    return render(request, 'auth/check_email.html')
def Support(request):
      return render(request,'support.html')

def Cokies(request):
      return render(request,'Cokies.html')
def Privacy(request):
      return render(request,'Privacy.html')

def certificate(request):
      return render(request,'certificate.html')
      

def free_certificate(request):
      return render(request,'free_certificate.html')

def web_dovelopment(request):
      return render(request,'web_dovelopment.html')
def infromatic(request):
      return render(request,'infromatic.html')
def UIXI(request):
      return render(request,'UIXI.html')
def applicatoion_dov(request):
      return render(request,'applicatoion_dov.html')
    