"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from .views import home_page, about_page, contact_page
from blog.views import blogPostCreate
from search.views import search_view

urlpatterns = [
    path('administrator/', admin.site.urls),

    path('', home_page),
    path('about/', about_page),
    path('contact/', contact_page),

    path('blog/', include('blog.urls')),

    path('createBlogPost/', blogPostCreate),

    path('search/', search_view),
]


from django.conf.urls.static import static

print(os.path.join(settings.LOCAL_STATIC_CDN_PATH, 'static'))

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
