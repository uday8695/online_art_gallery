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


from django.shortcuts import render, redirect
from django.http import HttpResponse
from artists.models import Artists
from django.urls import reverse
from datetime import datetime

def artists(request):
    if request.method == 'POST':
        # Retrieve form data
        artist_id = request.POST.get('Artist_id')
        artist_name = request.POST.get('artist_name')
        artist_age = request.POST.get('artist_age')
        category = request.POST.get('category')
        experience = request.POST.get('experience')
        earnings = request.POST.get('earnings')
        no_of_drawings_made = request.POST.get('no_of_drawings_made')
        created_date = request.POST.get('created_date')

        # Create and save new Artist object
        artist = Artists(
            Artist_id=artist_id,
            artist_name=artist_name,
            artist_age=artist_age,
            category=category,
            experience=experience,
            earnings=earnings,
            no_of_drawings_made=no_of_drawings_made,
            created_at=datetime.strptime(created_date, '%Y-%m-%d')
        )
        artist.save()

        return redirect(reverse('artist_details'))  # Redirect to a page showing all artists or a success page

    return render(request, 'artists.html')

from artworks.models import Artworks
from django.shortcuts import render, redirect


from django.urls import reverse

def add_art_work(request):
    if request.method == 'POST':
        # Retrieve form data
        artwork_id = request.POST.get('Artwork_id')
        title = request.POST.get('title')
        artist_id = request.POST.get('artist_id')
        artist_name = request.POST.get('artist_name')
        medium = request.POST.get('medium')
        dimensions = request.POST.get('dimensions')
        category = request.POST.get('category')
        price = request.POST.get('price')
        description = request.POST.get('description')
        status = request.POST.get('status')
        image = request.FILES.get('image')

        # Create and save new Artwork object
        artwork = Artworks(
            Artwork_id=artwork_id,
            title=title,
            artist_id=artist_id,
            artist_name=artist_name,
            medium=medium,
            dimensions=dimensions,
            category=category,
            price=price,
            description=description,
            status=status,
            image=image
        )
        artwork.save()

        return redirect(reverse('art_work_details'))  # Redirect to a page showing all artworks or a success page

    return render(request, 'add_art_work.html')

def art_work_details(request):
    artworks = Artworks.objects.all()
    return render(request, "art_work_details.html", {'artworks': artworks})



def sketchbooks_page(request):
    # Add any necessary context data
    return render(request, 'sketchbooks.html')

def brushes_page(request):
    # Add any necessary context data
    return render(request, 'brushes.html')
