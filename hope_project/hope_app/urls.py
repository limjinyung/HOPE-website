from . import views
from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('postlist', views.PostList.as_view(), name='postlist'),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)