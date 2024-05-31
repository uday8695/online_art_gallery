# """
# URL configuration for artproject project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from artists import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('artist/<str:artist_name>',views.artist_details,name='artist_details'),
#     path('artists/',views.artists,name='artists'),
#     path('artist_details/',views.artist_details,name='artist_details'),
#     path('artists_dashboard/',views.artists_dashboard,name='artists_dashboard'),

# ]
