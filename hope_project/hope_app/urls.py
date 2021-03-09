from . import views
from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('postlist/', views.post_list, name='postlist'),
    path("portfolio/", views.portfolio, name='portfolio'),
    path('create_confession', views.create_confession, name="confession"),
    path("about_us/", views.about_us, name='about_us'),
    path("login/", views.sign_in, name='login'),
    path("logout/", views.log_out, name='logout'),
    path("<slug:slug>/", views.post_detail, name='post_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)