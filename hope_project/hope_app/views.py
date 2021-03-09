from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import Post, Portfolio
from .forms import PostCommentForm, LoginForm
from django.core.exceptions import PermissionDenied
from django.contrib.postgres.search import SearchQuery, SearchVector


# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'post_list.html'

def index(request):
    template_name = 'index.html'

    anonymous_user = request.user.is_anonymous
    return render(request, template_name, {'anonymous_user': anonymous_user})


def post_list(request):
    template_name = 'post_list.html'

    anonymous_user = request.user.is_anonymous

    if request.method == "GET":
        daily_reading_post = Post.objects.order_by("?")[:3]
        most_view_post = Post.objects.order_by("?")[:3]
        weekly_popular_post = Post.objects.order_by("?")[:3]
        editor_recommend_post = Post.objects.order_by("?")[:3]
        latest_post_list = Post.objects.order_by("?")[:3]

    # return render(request, template_name, {'anonymous_user': anonymous_user,
    #                                        'daily_reading': daily_reading_post,
    #                                        'most_view': most_view_post,
    #                                        'weekly_popular': weekly_popular_post,
    #                                        'editor_recommend': editor_recommend_post,
    #                                        'lastest_post': latest_post_list})

    return render(request, template_name, {'anonymous_user': anonymous_user})


def portfolio(request):
    template_name = 'portfolio.html'

    portfolio_list = Post.objects.all().order_by("?")[:9]
    print(portfolio_list)

    return render(request, template_name)


def about_us(request):
    template_name = 'about_us.html'

    return render(request, template_name)


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = PostCommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = PostCommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def create_confession(request):
    template_name = 'confession.html'

    if not request.user.is_authenticated:
        raise PermissionDenied

    if request.method == "POST":
        confession_form = ConfessionForm(data=request.POST)

        if confession_form.is_valid():
            payload = confession_form.cleaned_data

            author = request.user
            title = payload.get('title')
            content = payload.get('content')
            slug = title.replace(' ', '-')
            status = 1

            post = Post.objects.create(author=author, title=title, content=content, slug=slug, status=status)
            try:
                post.save()
            except Exception as e:
                print(e)

            return redirect("/")

    confession_form = ConfessionForm()

    return render(request, template_name, {'form': confession_form})



class SearchResultsView(ListView):
    template_name = 'search_result.html'

    def get_queryset(self):
        hope_search = self.request.GET.get('search_hope')
        if hope_search is None:
            return redirect('/')
        return Post.objects.annotate(search=SearchVector('title', 'content')).filter(search=hope_search)


def sign_in(request):
    template_name = "login.html"

    if request.method == "POST":
        payload = request.POST

        username = payload.get("username")
        password = payload.get("password")
        current_user = authenticate(username=username, password=password)

        if current_user is not None:
            login(request, current_user)
            return redirect("/")
        else:
            raise PermissionDenied
    else:
        form = LoginForm()

        return render(request, template_name, {'form': form})


def log_out(request):
    logout(request)
    print(request.user)
    return redirect('/')