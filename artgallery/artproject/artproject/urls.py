from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from artapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('header/', views.header, name='header'),
    path('footer/', views.footer, name='footer'),
    path('home/', views.home, name='home'),
    path('artists/', views.artists, name='artists'),
    path('artworks/', views.artworks, name='artworks'),
    path('artsupplies/', views.artsupplies, name='artsupplies'),
    path('shop/', views.shop, name='shop'),
    path('artist_details/', views.artist_details, name='artist_details'),
    path('artists_dashboard/', views.artists_dashboard, name='artists_dashboard'),
    path('accounts/', include('accounts.urls')),
    path('add_art_work/', views.add_art_work, name='add_art_work'),
    path('art_work_details/', views.art_work_details, name='art_work_details'),
    path('items/', views.items, name='items'),
    path('canvas/', views.canvas_page, name='canvas_page'),
    path('paint-brushes/', views.paint_brushes_page, name='paint_brushes'),
    path('sketchbooks/', views.sketchbooks_page, name='sketchbooks'),
    path('brushes/', views.brushes_page, name='brushes'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
