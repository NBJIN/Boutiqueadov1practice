"""boutique_ado URL Configuration

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
from django.urls import path, include
from django.conf import settings # Lastly to allow Django to see the MEDIA_URL. We need to go to urls.py Import our settings and the static function from django.conf.urls.static
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # T
    path('', include('home.urls')), # This is the home level urls 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # once settings added above in django - And then use the static function to add the MEDIA_URL to our list of URLs.
