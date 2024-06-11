from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from shop.models import Shop
from artists.models import Artists
from artists.forms import ArtistForm
from artworks.models import Artworks
from artworks.forms import ArtworkForm

def header(request):
    return render(request, 'header.html')

def footer(request):
    return render(request, 'footer.html')

def home(request):
    return render(request, 'home.html')

def artworks(request):
    artworks = Artworks.objects.all()
    return render(request, 'artworks.html', {'artworks': artworks})

def artsupplies(request):
    return render(request, 'artsupplies.html')

def items(request):
    return render(request, 'items.html')

def shop(request):
    products = Shop.objects.all()
    return render(request, 'shop.html', {'products': products})

def artists_dashboard(request):
    return render(request, 'artists_dashboard.html')

def artist_details(request):
    artists =Artists.objects.all()
    return render(request, 'artist_details.html', {'artists': artists})

def artists(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_details', artist_id=artist.id)
    else:
        form = ArtistForm()
    return render(request, "artists.html", {'form': form})

def add_art_work(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('art_work_details')
    else:
        form = ArtworkForm()
    return render(request, "add_art_work.html", {'form': form})

def art_work_details(request):
    artworks = Artworks.objects.all()
    return render(request, "art_work_details.html", {'artworks': artworks})


from artsupplies.models import Artsupplies

def canvas_page(request):
    products = Artsupplies.objects.filter(category='Canvas')
    return render(request, 'canvas.html', {'products': products})
# Repeat the same for other product categories

def paint_brushes_page(request):
    # Add any necessary context data
    return render(request, 'paint_brushes.html')

def sketchbooks_page(request):
    # Add any necessary context data
    return render(request, 'sketchbooks.html')

def brushes_page(request):
    # Add any necessary context data
    return render(request, 'brushes.html')
