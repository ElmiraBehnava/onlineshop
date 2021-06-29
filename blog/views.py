from django.shortcuts import render, get_object_or_404
from .models import Post, PostCategory

# comment
from .models import Comment, Post
from .forms import CommentForm

"""
pagination
"""
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




# def post_list(request):
#     posts = Post.published.all()
#     return render(request, 'blog/post/list.html', {'posts': posts})

def post_list(request, postcategory_slug=None):
    post_category = None
    post_categories = PostCategory.objects.all()
    posts = Post.published.all()
    if postcategory_slug:
        post_category = get_object_or_404(PostCategory, slug=postcategory_slug)
        posts = posts.filter(post_category=post_category)
    
    #pagination
    object_list = Post.published.all()
    paginator = Paginator(posts, 2) # number of show products in each page
    page_number = request.GET.get('page')
    posts_of_each_page = paginator.get_page(page_number) # page_obj = products in each page

    return render(request, 'blog/post/list.html', {'posts': posts_of_each_page, 'post_category' : post_category, 'post_categories' : post_categories})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    post_categories = PostCategory.objects.all()
    new_posts = Post.published.all()[:3]
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post/detail.html', {'post': post, 'comments': comments, 'new_comment': new_comment,'comment_form': comment_form, 'post_categories' : post_categories, 'new_posts':new_posts})





    

