from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from feed.models import Post, Comment, PostUser_Upvotes
from django.conf import settings
from feed.forms import NewPost_Form, NewComment_Form
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

# Create your views here.

# EITHER WE CAN USE FUNCTION-BASED VIEWS OR CLASS-BASED VIEWS
# WRITING FUNCTION_BASED VIEWS IS LENGTHY AND RESULTS IN REDUNDANT CODE
# DJANGO HAS CLASSES FOR COMMON USECASES VIEWS FOR REUSABILITY - CRUD (CREATE READ UPDATE DELETE)
# SO I HAD USED THESE CLASSES TO MINIMISE REDUNDANT CODE DUE TO LESS TIME 
# ONLY OVERRIDED METHOD IN WHICH I WANTED DIFFICULT LOGIC FROM DEFAULT
# https://ccbv.co.uk/

#home page
class Home_Page(ListView):
	allow_empty = True #if no posts
	context_object_name = 'posts'
	model = Post
	template_name = 'homepage.html'
	paginate_by = settings.POST_PAGINATE_BY
	ordering = '-created_on'	# '-' indicated descending order

	def get_queryset(self):
		queryset = super().get_queryset()
		#filter GET parameters
		keyword = self.request.GET.get('keyword')
		created_by = self.request.GET.get('created_by')
		if keyword:
			queryset = queryset.filter(message__contains=keyword)
		if created_by:
			queryset = queryset.filter(created_by__username__contains=created_by)
		return queryset

#new post
@method_decorator(login_required, name='dispatch')	#login needed for new post
class New_Post(CreateView):
	context_object_name = 'post'
	form_class = NewPost_Form
	template_name = 'newpost.html'

	def form_valid(self, form):
	    """If the form is valid, save the associated model."""
	    self.object = form.save(commit=False)	#dont save, just return db instance reference
	    self.object.created_by = self.request.user
	    self.object.save()	#now save 
	    success_url = reverse_lazy('home_page') 	
	    return redirect(success_url)

#login view
class Login_View(LoginView):
	template_name = 'loginpage.html'

#comment page view for a post
class Comments_View(ListView):
	allow_empty = True #if no posts
	context_object_name = 'comments'
	model = Comment
	template_name = 'commentspage.html'
	paginate_by = settings.COMMENTS_PAGINATE_BY
	ordering = '-created_on'

	def dispatch(self, request, *args, **kwargs):
		self.postobj = get_object_or_404(Post, id=self.kwargs.get('post_id')) #return 404 if invalid post id
		#since self.post already exist for  Comment model object
		return super().dispatch(request, *args, **kwargs)

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(post__id=self.kwargs.get('post_id'))

	def get_context_data(self, **kwargs):
		#add post to template context
		kwargs['post'] = self.postobj 
		return super().get_context_data(**kwargs)

#new comment
@method_decorator(login_required, name='dispatch')	#login needed for new comment
class New_Comment(CreateView):
	context_object_name = 'comment'
	form_class = NewComment_Form
	template_name = 'newcomment.html'

	def dispatch(self, request, *args, **kwargs):
		self.postobj = get_object_or_404(Post, id=self.kwargs.get('post_id'))
		return super().dispatch(request, *args, **kwargs)

	def form_valid(self, form):
	    """If the form is valid, save the associated model."""
	    self.object = form.save(commit=False)
	    self.object.created_by = self.request.user
	    self.object.post = self.postobj
	    self.object.save()
	    success_url = reverse_lazy('comments_url', kwargs={'post_id':self.kwargs.get('post_id')})
	    return redirect(success_url)

	def get_context_data(self, **kwargs):
		#add post to template context
		kwargs['post'] = self.postobj 
		return super().get_context_data(**kwargs)

@login_required #login needed for upvoting post
def upvote_post(request, post_id):
	postobj = get_object_or_404(Post, id=post_id)
	userobj = request.user 
	page = request.GET.get('page', default=1)
	#create only if not exists
	obj, created = PostUser_Upvotes.objects.get_or_create(post=postobj, upvoted_by=userobj)
	return redirect(reverse_lazy('home_page') + '?page={}'.format(page))
