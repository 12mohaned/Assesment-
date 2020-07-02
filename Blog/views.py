from django.shortcuts import render, redirect, HttpResponse
from .forms import SignupForm, PostForm, CommentForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post, user, Comment
# Create your views here.

#Show Posts Created By other Users
def Home(request):
    if not is_authenticated(request):
        return redirect("Blog/Login.html")
    Commentform = CommentForm()
    if request.method == "POST":
        #Create Comment on the post
        for post in Post.objects.all():
            if request.POST.get(post.Title) == "Comment":
                Commentform = CommentForm(request.POST)
                comment = Commentform.save(commit=False)
                comment.User_Comment = request.user.username
                comment.Postuser = post.User
                comment.Post = post
                comment.save()

    Body ={
    "NewFeeds" : Post.objects.all(),
    "CommentForm" : Commentform,
    "Comments"  : Comment.objects.all()
    }
    return render(request,"Blog/Home.html", Body)

#User can create post by visiting his/her profil page and view comments on his post(s)
def Profile(request):
    if not is_authenticated(request):
        return HttpResponse("Profile Can't be accessed without logging in")

    Postform = PostForm()
    if request.method == "POST":
        Postform = PostForm(request.POST)
        post = Postform.save(commit = False)
        post.User = request.user
        post.save()
        return redirect("Blog/Profile.html")
    Body ={
    "Post" : Postform,
    "Comments": Comment.objects.filter(Postuser = request.user)
    }
    print(Comment.objects.filter(Postuser=request.user))
    return render(request,'Blog/Profile.html', Body)

#Return User Posts
def Posts(request):
    if not is_authenticated(request):
        return redirect("Blog/Login.html")
    Body = {
    "Posts":Post.objects.filter(User = request.user)
    }
    return render(request, 'Blog/Posts.html',Body)
#Render Login Page and Check if LoginForm is valid
def Login(request):
    if is_authenticated(request):
        return redirect('Blog/Home.html')
    LoginForm = AuthenticationForm()
    if request.method == "POST":
        LoginForm = AuthenticationForm(request, data = request.POST)
        if LoginForm.is_valid():
            username  = LoginForm.cleaned_data.get("username")
            password = LoginForm.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            login(request, user)
            if user is None :
                return HttpResponse("You Don't Have an Account")
            else:
                return redirect('Blog/Home.html')
    Body = {'Form':LoginForm}
    return render(request,'Blog/Login.html',Body)

#Render Signup Page and Check if SignupForm is Valid
def Signup(request):
    user = None
    if is_authenticated(request):
        return redirect('Blog/Home.html')
    template = "Blog/Signup.html"
    Signup = SignupForm()
    if request.method == "POST":
        Signup = SignupForm(request.POST)
        if Signup.is_valid():
            Signup.save()
            username  = Signup.cleaned_data.get("username")
            first_name = Signup.cleaned_data.get("first_name")
            last_name  = Signup.cleaned_data.get("last_name")
            raw_password = Signup.cleaned_data.get("password1")
            Email  = Signup.cleaned_data.get("email")
            user = user(username = username)
            user.save()
            user = authenticate(username = username, password = raw_password)
            login(request,user)
            return redirect("Blog/Home")
        else:
            return redirect('Blog/Signup.html')
    body = {'Form':Signup}
    return render(request, template, body)


#Log the user out
def Logout(request):
    logout(request)
    return render(request,'Blog/Home.html')

#Check if user is authenticated
def is_authenticated(request):
    if request.user.is_authenticated:
        return True
    else:
        return False
