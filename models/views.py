from django.shortcuts import render, redirect, get_object_or_404
from .models import Status, Comment, NestedComment
from pprint import pprint
from .forms import PostComment
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.contrib.auth.models import User
def index(request):
	list =[]
	all_status = Status.objects.all()
	dict ={}
	for i in all_status:
		list1 =[]
		dict['status'] = i.status_text
		comments = i.comment_set.all()
		for i in comments:
			list1.append(str(i))
		dict['comments'] = list1 
		list.append(dict)
		dict ={}
     
	context_data = list
	pprint(context_data)
	all_user = User.objects.all()

	return render(request, "index.html", {'user': all_user, 'statusComments': context_data})

def status(request):
	all_status = Status.objects.all()
	return render(request, "status.html", {'all_status': all_status})

def status_detail(request, pk):
	status = Status.objects.get(pk=pk)
	comments = status.comment_set.all()
	
	for comment in comments:
		comment.nested_comments = comment.nestedcomment_set.all()

	if request.method == 'POST':
		form = PostComment(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.status_id = status
			post.save()
			return redirect('status_detail', pk=pk)
	else:
		form = PostComment()
	
	return render(request, "status_detail.html", {'form': form, 'status': status, 'comments': comments})

def nestedcomment(request):
	if request.method == "POST":
		if request.is_ajax():
			statusId = request.POST.get('statusid')
			replytext = request.POST.get('reply')
			commentid = request.POST.get('comment_id')
			comment = Comment.objects.get(pk=commentid)
			nestedcomment = NestedComment.objects.create(comment_id = comment,nested_comment_text = replytext)
			nestedcomment.save()
			return redirect('status_detail', pk=statusId)
		else:
			pprint("this is not ajax request")
	return render(request, 'base.html')


# @csrf_protect
def login(request):
	if request.method == 'POST':
		user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
		if user is not None:
			auth.login(request, user)
			return redirect('status')
		else:
			return HttpResponse('failier')
	else:
		return render(request, 'login.html', {})

def logout(request):
	auth.logout(request)
	return redirect('status')

def post_status(request):
	if request.method == "POST":
		status = Status.objects.create(status_text=request.POST['status'], user_id=User.objects.get(username=request.user.username))
		return redirect('status')
	else:
		return render(request, 'post_status.html', {})