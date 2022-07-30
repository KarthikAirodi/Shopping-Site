"""hello URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from hello.settings import MEDIA_ROOT, MEDIA_URL
path('', include('django.contrib.auth.urls'))
admin.site.site_header = "Veg Corner Admin"
admin.site.site_title = "Veg Corner Admin Portal"
admin.site.index_title = "Welcome to Veg Corner Researcher Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    #static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    #path('about',include())
]
urlpatterns+=staticfiles_urlpatterns()