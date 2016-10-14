from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.
from .models import Post, Comment

def index(request):
	all_posts = Post.objects.order_by('-id')
	context = {'all_posts' : all_posts}
	return render(request,'blog/index.html',context)

def newpost(request):
	return render(request,'blog/new.html',{})

def detail(request, post_title):
	post = get_object_or_404(Post, title=post_title)
	all_comments = post.comment_set.order_by('-id')
	return render(request, 'blog/post.html', {'post': post, 'all_comments' : all_comments})

def post(request):
	if request.method == 'POST':
		q = Post(title = request.POST['title'], content = request.POST['content'], tags = request.POST['tags'], url = request.POST['url'])
		q.save()
		return HttpResponseRedirect(reverse('blog:index'))
	return render(request, 'blog/new.html', {
            'error_message': "You didn't complete everything.",
        })

def newcomment(request, post_title):
	if request.method == 'POST':
		post = get_object_or_404(Post, title=post_title)
		post.comment_set.create(content = request.POST['content'])
		post.save()
		return redirect('blog:detail', post_title = post_title)
