"""rtrw_serpong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from wagtail.core import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
# from wagtail.documents import urls as wagtaildocs_urls


admin.site.index_title = _('Administrasi RT RW')
admin.site.site_header = _('RT RW Serpong')
admin.site.site_title = _('Administrasi RT RW')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cms-admin/', include(wagtailadmin_urls)),
    path('accounts/', include('allauth.urls')),
    # path('documents/', include(wagtaildocs_urls)),
    # path('pages/', include(wagtail_urls)),
]


if settings.DEBUG:
    # from django.conf.urls.static import static
    # from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic import TemplateView
    # from django.views.generic.base import RedirectView

    # # Serve static and media files from development server
    # urlpatterns += staticfiles_urlpatterns()
    # urlpatterns += static(settings.MEDIA_URL,
    #                       document_root=settings.MEDIA_ROOT)
    # urlpatterns += [
    #     url(
    #         r'^favicon\.ico$', RedirectView.as_view(
    #             url=settings.STATIC_URL + 'img/bread-favicon.ico'
    #         )
    #     )
    # ]

    # Add views for testing 404 and 500 templates
    urlpatterns += [
        url(r'^test404/$', TemplateView.as_view(template_name='404.html')),
        url(r'^test500/$', TemplateView.as_view(template_name='500.html')),
    ]

urlpatterns += [
    url(r'', include(wagtail_urls)),
]
