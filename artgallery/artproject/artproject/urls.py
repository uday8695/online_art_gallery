"""
URL configuration for artproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from artapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('header/',views.header,name='header'),
    path('footer/',views.footer,name='footer'),
    path('home/',views.home,name='home'),
    path('artists/',views.artists,name='artists'),
    path('artworks/',views.artworks,name='artworks'),
    path('artsupplies/',views.artsupplies,name='artsupplies'),
    path('shop/',views.shop,name='shop'),
    path('styles/',views.styles,name='styles'),
    path('art_work_details/',views.art_work_details,name='art_work_details'),
    path('add_art_work/',views.add_art_work,name='add_art_work'),
    path('artist_details/',views.artist_details,name='artist_details'),
    path('artists_dashboard/',views.artists_dashboard,name='artists_dashboard'),
    path('accounts/',include('accounts.urls')),
    # path('artworks/',include('artworks.urls')),
    # path('artists/',include('artists.urls')),
    # path('styles/',include('styles.urls')),
    
    
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)