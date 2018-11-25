"""freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView
from books import views
from books.backends import MyRegistrationView
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from books.sitemap import (
    BookSitemap,
    StaticSiteMap,
    HomepageSiteMap,
)
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

sitemaps = {
    'books': BookSitemap,
    'static': StaticSiteMap,
    'homepage': HomepageSiteMap,
}

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    # path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('contact/', views.contact, name='contact'),
    path('books', RedirectView.as_view(pattern_name='browse', permanent=True)),
    path('books/<slug>/', views.book_detail, name='book_detail'),
    path('books/<slug>/edit/', views.edit_book, name='edit_book'),
    path('browse/', RedirectView.as_view(pattern_name='browse', permanent=True)),
    path('browse/title/', views.browse_by_title, name='browse'),
    path('browse/title/<initial>/', views.browse_by_title, name='browse_by_title'),
    path('browse/title/<category>/', views.browse_by_category, name='browse_by_category'),
    # Account Registration URL's
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),
    path('accounts/create_book/', views.create_book, name='create_book'),
    # Password Reset URL's
    path('accounts/password/reset/', PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name="password_reset"),
    path('accounts/password/reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_done"),
    path('accounts/password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name="password_reset_confirm"),
    path('accounts/password/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name="password_reset_complete"),
    path('sitemap.xml', sitemap, { 'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
