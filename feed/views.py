from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, News, Comments, Like
from .forms import UserRegistrationForm, UserLogin, NewsCreateForm, CommentForm, LikeButtonForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User





def news_create(request):
    user = User(id=request.user.id).id
    if request.method == 'POST':
        news_form = NewsCreateForm(request.POST)
        if news_form.is_valid():
            cd = news_form.cleaned_data
            new = News.objects.create(user=User(id=request.user.id), category=cd['category'],
                                title=cd['title'],
                                image=cd['image'],
                                body=cd['body'])
            new.save()
            return redirect('news_list')
    else:
        news_form = NewsCreateForm()
    return render(request, 'news_create.html', {'news_form': news_form,
                                                'user': user})



def news_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    news = News.objects.filter(status=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        news = news.filter(category=category)

    return render(request, 'news_list.html', {'category': category,
                                              'categories': categories,
                                              'news': news})


def post_detail(request, post_id):
    likes = Like.objects.filter(news_likes=News(id=post_id))
    post = get_object_or_404(News, id=post_id)
    comments = Comments.objects.filter(news=News(id=post_id))
    reply = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        like_form = LikeButtonForm(request.POST)
        if comment_form.is_valid():
            cd = comment_form.cleaned_data
            if cd['text'] == '':
                pass
            else:
                Comments.objects.create(news=News(id=post_id), text=cd['text']).save()

        if like_form:
            if like_form.is_valid():
                if Like.objects.filter(user=request.user) and Like.objects.filter(news_likes=News(id=post_id)):
                    reply = "Вы уже ставили оценку"
                else:
                    Like.objects.create(user=request.user, news_likes=News(id=post_id)).save()


    else:
        like_form = LikeButtonForm()
        comment_form = CommentForm()

    return render(request, 'details.html', {'post': post,
                                            'comment_form': comment_form,
                                            'comments': comments,
                                            'like_form': like_form,
                                            'likes': likes,
                                            'reply': reply})




def user_login(request):
    if request.method == 'POST':
        user_form = UserLogin(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('news_list')
    else:
        user_form = UserLogin()

    return render(request, 'login.html', {'user_form': user_form})


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            cd = user_form.cleaned_data
            new_user.set_password(cd['password'])
            new_user.save()
            login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'news_list.html')
    else:
        user_form = UserRegistrationForm()

    return render(request, 'registration.html', {'user_form': user_form})


def user_logout(request):
    logout(request)
    return redirect('news_list')


# class CategoryListView(ListView):
#     model = Category
#     template_name = 'category_list.html'
#     context_object_name = 'categories'



