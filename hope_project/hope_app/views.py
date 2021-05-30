from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import Post, Portfolio, WorkExperience, VolunteerExperience
from .forms import PostCommentForm, LoginForm, SignUpForm, ConfessionForm, PortfolioForm, WorkExperienceForm, VolunteerExperienceForm
from django.core.exceptions import PermissionDenied
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.core import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'post_list.html'

def index(request):
    template_name = 'index.html'

    anonymous_user = request.user.is_anonymous
    index_post = Post.objects.order_by("?")[:6]
    index_portfolio = Portfolio.objects.order_by("?")[:4]

    return render(request, template_name, {'anonymous_user': anonymous_user,
                                           'index_post':index_post,
                                           'index_portfolio': index_portfolio})


def post_list(request):
    template_name = 'post_list.html'

    anonymous_user = request.user.is_anonymous

    daily_reading_post = Post.objects.order_by("?")[:3]
    most_view_post = Post.objects.order_by("?")[:3]
    editor_recommend_post = Post.objects.order_by("?")[:3]

    return render(request, template_name, {'anonymous_user': anonymous_user,
                                           'daily_reading': daily_reading_post,
                                           'most_view': most_view_post,
                                           'editor_recommend': editor_recommend_post})

    # return render(request, template_name, {'anonymous_user': anonymous_user})


def portfolio(request):
    template_name = 'portfolio.html'

    anonymous_user = request.user.is_anonymous

    portfolio_id_list = []
    user_id_list = []

    portfolio_list = Portfolio.objects.all().order_by("?")[:9]

    for portfolio in portfolio_list:
        portfolio_id_list.append(portfolio.portfolio_id)

    for user_id in portfolio_list:
        user_id_list.append(user_id.author.pk)

    work_experience_list = WorkExperience.objects.filter(portfolio__in=portfolio_id_list)
    volunteer_experience_list = VolunteerExperience.objects.filter(portfolio__in=portfolio_id_list)
    user_list = User.objects.filter(pk__in=user_id_list)

    portfolio_json = serializers.serialize('json', portfolio_list)
    work_experience_json = serializers.serialize('json', work_experience_list)
    volunteer_experience_json = serializers.serialize('json', volunteer_experience_list)
    user_json = serializers.serialize('json', user_list)

    return render(request, template_name, {'anonymous_user': anonymous_user,
                                           'portfolio_list': portfolio_list,
                                           'portfolio_json':portfolio_json,
                                           'work_experience_json':work_experience_json,
                                           'volunteer_experience_json': volunteer_experience_json,
                                           'user_json': user_json})


def about_us(request):
    template_name = 'about_us.html'

    anonymous_user = request.user.is_anonymous

    return render(request, template_name, {'anonymous_user': anonymous_user})


def confession_detail(request, slug):
    template_name = 'post_detail.html'
    confession = get_object_or_404(Post, slug=slug)

    anonymous_user = request.user.is_anonymous

    return render(request, template_name, {'confession': confession,'anonymous_user': anonymous_user})


def create_confession(request):
    template_name = 'create_confession.html'

    anonymous_user = request.user.is_anonymous

    if not request.user.is_authenticated:
        messages.warning(request, 'Please login to add a post.')
        return redirect('login')

    if request.method == "POST":
        confession_form = ConfessionForm(request.POST, request.FILES)

        if confession_form.is_valid():
            payload = confession_form.cleaned_data
            image = request.FILES['post_image']

            author = request.user
            title = payload.get('title')
            content = payload.get('content')
            # post_image = payload.get('post_image')
            post_image = image
            tag = payload.get('tag')
            slug = title.replace(' ', '-')
            status = 1

            post = Post.objects.create(author=author, title=title, content=content, slug=slug, post_image=post_image,
                                       tag=tag, status=status)
            try:
                post.save()
                messages.success(request, 'Confession successfully created.')
            except Exception as e:
                print(e)

            return redirect("/confession")

    confession_form = ConfessionForm()

    return render(request, template_name, {'form': confession_form,'anonymous_user': anonymous_user})


class SearchResultsView(ListView):
    template_name = 'search_result.html'

    def get_queryset(self):
        hope_search = self.request.GET.get('search_hope')
        print(len(hope_search)==0)
        if len(hope_search) == 0:
            return redirect('/')
        else:
            return Post.objects.annotate(search=SearchVector('title', 'content')).filter(search=hope_search)


def create_portfolio(request):
    anonymous_user = request.user.is_anonymous

    if not request.user.is_authenticated:
        messages.warning(request, 'Please login to create a portfolio.')
        return redirect('login')

    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        try:
            user_portfolio = Portfolio.objects.get(author=user)
        except ObjectDoesNotExist:
            user_portfolio = ''

    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        try:
            user_portfolio = Portfolio.objects.get(author=user)
        except ObjectDoesNotExist:
            user_portfolio = ''

        portfolio_form = PortfolioForm(request.POST, request.FILES)

        if portfolio_form.is_valid():
            payload = portfolio_form.cleaned_data
            image = request.FILES['portfolio_image']

            author = request.user
            title = payload.get("title")
            biography = payload.get("biography")
            phone_number = payload.get("phone_number")
            address = payload.get("address")
            # portfolio_img = payload.get("portfolio_image")

            portfolio = Portfolio.objects.create(
                author=author,
                title=title,
                biography=biography,
                phone_number=phone_number,
                address=address,
                portfolio_image=image
            )

            try:
                portfolio.save()
                messages.success(request, 'Portfolio successfully created.')
            except Exception as e:
                print(e)

            # return render(request, "/portfolio/")
            return redirect('create_portfolio')

    portfolio_form = PortfolioForm()
    work_experience_form = WorkExperienceForm()
    volunteer_form = VolunteerExperienceForm()

    return render(request, "create_portfolio.html", {
        'portfolio_form': portfolio_form,
        'work_experience_form': work_experience_form,
        'volunteer_form': volunteer_form,
        'user_portfolio': user_portfolio,
        'current_user': request.user,
        'anonymous_user': anonymous_user
    })


def add_work_experience(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please login to add work experience.')
        return redirect('login')

    work_experience_form = WorkExperienceForm(data=request.POST)

    if work_experience_form.is_valid():
        form_data = work_experience_form.cleaned_data

        description = form_data.get("description")
        start_date = form_data.get("start_date")
        end_date = form_data.get("end_date")

        user = User.objects.get(username=request.user.username)
        user_portfolio = Portfolio.objects.get(author=user)

        work_experience = WorkExperience.objects.create(
            portfolio=user_portfolio,
            description=description,
            start_date=start_date,
            end_date=end_date
        )

        try:
            work_experience.save()
            messages.success(request, 'Work Experience successfully created.')
        except Exception as e:
            print(e)

    return redirect('create_portfolio')


def add_volunteer_experience(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please login to add volunteer experience.')
        return redirect('login')

    volunteer_experience_form = VolunteerExperienceForm(data=request.POST)

    if volunteer_experience_form.is_valid():
        form_data = volunteer_experience_form.cleaned_data

        description = form_data.get("description")
        start_date = form_data.get("start_date")
        end_date = form_data.get("end_date")

        user = User.objects.get(username=request.user.username)
        user_portfolio = Portfolio.objects.get(author=user)

        volunteer_experience = VolunteerExperience.objects.create(
            portfolio=user_portfolio,
            description=description,
            start_date=start_date,
            end_date=end_date
        )

        try:
            volunteer_experience.save()
            messages.success(request, 'Volunteer Experience successfully created.')
        except Exception as e:
            print(e)

    return redirect('create_portfolio')


def sign_up(request):
    template_name = "sign_up.html"

    if request.method == "POST":
        form_data = request.POST

        sign_up_form = SignUpForm(data=form_data)

        if sign_up_form.is_valid():
            username = form_data.get("username")
            password = form_data.get("password")
            email = form_data.get("email")
            first_name = form_data.get("first_name")
            last_name = form_data.get("last_name")
            confirm_password = form_data.get("confirm_password")

            if password == confirm_password:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )

                try:
                    user.save()
                    messages.success(request, 'Successfully sign up.')
                except Exception as e:
                    print("Something went wrong when saving the user data to the database.")

                return redirect("/")
            else:
                print("Password and Confirmed Password doesn't match!")
        else:
            print(sign_up_form.errors)

    sign_up_form = SignUpForm()

    return render(request, template_name, {'sign_up_form': sign_up_form})


def sign_in(request):
    template_name = "login.html"

    if request.method == "POST":
        payload = request.POST

        username = payload.get("username")
        password = payload.get("password")
        current_user = authenticate(username=username, password=password)

        if current_user is not None:
            login(request, current_user)
            messages.success(request, 'Successfully Login.')
            return redirect("/")
        else:
            messages.warning(request, "There's something wrong. Please try again")
            return redirect('/login')
    else:
        form = LoginForm()

        return render(request, template_name, {'form': form})


def log_out(request):
    logout(request)
    messages.info(request, 'Successfully Logout.')
    return redirect('/')