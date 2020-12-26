from django.shortcuts import render
posts = [
    {
        'author' : 'surya',
        'title'  :  'Blog post 1',
        'content':  'Fist post content',
        'date_posted': 'December 26, 2020'
    },
    {
        'author' : 'Muttu',
        'title'  :  'Blog post 2',
        'content':  'Second post content',
        'date_posted': 'December 25, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})