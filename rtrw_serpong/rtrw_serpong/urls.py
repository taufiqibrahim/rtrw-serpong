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
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
# from wagtail.admin import urls as wagtailadmin_urls
# from wagtail.core import urls as wagtail_urls
# from wagtail.documents import urls as wagtaildocs_urls


admin.site.index_title = _('Administrasi RT RW')
admin.site.site_header = _('RT RW Serpong')
admin.site.site_title = _('Administrasi RT RW')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('cms/', include(wagtailadmin_urls)),
    # path('documents/', include(wagtaildocs_urls)),
    # path('pages/', include(wagtail_urls)),
]

# from .wagtail_settings import WAGTAIL_URLS
# urlpatterns += WAGTAIL_URLS
