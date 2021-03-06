from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import EmailPostForm



def post_list(request):
    posts = Post.published.all()
    return render(request,
                    'blog/post/list.html',
                    {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    return render(request,
                    'blog/post/detail.html',
                    {'post': post})


def post_share(request, post_id):
# Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    if request.method == 'POST':
# Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
# Form fields passed validation
            cd = form.cleaned_data
# ... send email
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form})