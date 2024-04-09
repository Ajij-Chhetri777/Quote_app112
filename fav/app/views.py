from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from app.models import Categories, Quote, Comment, Reply, Favourite
from app.forms import PostForm, LoginForm, RegisterForm,  CommentForm, ReplyForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required(login_url='login')
def home(request):
    category = Categories.objects.all()
    context = {'category':category}
    return render(request,'home.html',context)

def quote_view(request,id1):
    gories = get_object_or_404(Categories , id = id1)
    quote = Quote.objects.filter(categories = gories) 
    return render(request, "quote_view.html",{"quote":quote, 'gories':gories})


def post(request):
    form = PostForm()
    if request.method == "POST":
          form = PostForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('home')
    return render(request,'post.html',{'form':form})

def register(request):
    form = RegisterForm()
    if request.method == "POST":
         form = RegisterForm(request.POST)
         if form.is_valid():
              form.save()
              return redirect('login')
    return render(request,'register.html',{'form':form})
              
def login(request):
    form = LoginForm()
    if request.method == "POST":
         form = LoginForm(request, request.POST)
         if form.is_valid():
              username = form.cleaned_data['username']
              password = form.cleaned_data['password']
              user = authenticate(request, username=username,password = password)
              if user is not None:
                  auth_login(request, user)
                  return redirect('home')

    return render(request,'login.html',{'form':form})

def ping(request,key ):
     ping = get_object_or_404(Quote,key = key)
     form1 = CommentForm()
     if request.method == "POST":
          form1 = CommentForm(request.POST)
          if form1.is_valid():
               form1.save()
     comment = Comment.objects.filter(quotes=ping)

     return render(request,'line.html',{'ping':ping,'comment':comment,'form1':form1})
def add_favourite(request,key):
               rite = get_object_or_404(Quote,key = key)
               favourite_instance, created = Favourite.objects.get_or_create(user = request.user, favourite_item = rite)
               return redirect('favourite_quotes')

@login_required(login_url='login')
def favourite_quotes(request):
     quotes = Favourite.objects.all()
     return render(request, 'favourite.html',{'quotes':quotes})


def delete_favourite(request,id ):
     rite = get_object_or_404(Favourite,id = id )
     rite.delete()
     return redirect('favourite_quotes')       
def edit_comment(request,id):
     pass
def delete_quote(request,key):
     object = get_object_or_404(Quote,key = key)
     object.delete()
     return redirect('home')


def edit_quote(request,key):
     object = get_object_or_404(Quote,key = key)
     form = PostForm(instance=object)
     if request.method == "POST":
          form = PostForm(request.POST, instance=object)
          if form.is_valid():
               form.save()
               return redirect('.')
     return render(request,'post.html',{'form':form}) 


def delete_comment(request,id):
     pass