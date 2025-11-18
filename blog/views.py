from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Like
from .forms import CommentForm
from .models import Comment


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(parent__isnull=True)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            parent_id = request.POST.get('parent_id')
            if parent_id:
                comment.parent = Comment.objects.get(id=parent_id)
            comment.save()
            return redirect('post-detail', pk=pk)
    else:
        form = CommentForm()
    
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})

def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
    return redirect('post-detail', pk=pk)




"""from django.shortcuts import render,redirect
from.models import Post,Like 

def post_list(request):
    posts=Post.objects.all().order_by('-created_at')
    return render(request,'post_list.html')"""




