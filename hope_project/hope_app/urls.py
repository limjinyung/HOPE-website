from . import views
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('confession/', views.post_list, name='confession'),
    path("portfolio/", views.portfolio, name='portfolio'),
    path('create_confession/', views.create_confession, name="create_confession"),
    path('create_portfolio/', views.create_portfolio, name="create_portfolio"),
    path('create_portfolio/add_work_experience', views.add_work_experience, name="add_work_experience"),
    path('create_portfolio/add_volunteer_experience', views.add_volunteer_experience, name="add_volunteer_experience"),
    path("about_us/", views.about_us, name='about_us'),
    path("signup/", views.sign_up, name='signup'),
    path("login/", views.sign_in, name='login'),
    path("logout/", views.log_out, name='logout'),
    path("confession/<slug:slug>/", views.confession_detail, name='confession_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
