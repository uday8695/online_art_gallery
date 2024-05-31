from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
# def art(request):
#     return HttpResponse("<h1>welcome to art gallery</h1>")

def header(request):
    return render(request,'header.html')

def footer(request):
    return render(request,'footer.html')

def home(request):
    return render(request,'home.html')

def artworks(request):
    return render(request,'artworks.html')

def artsupplies(request):
    return render(request,'artsupplies.html')

def items(request):
    return render(request,'items.html')

from shop.models import Shop
def shop(request):
    product= Shop.objects.all()
    return render(request,'shop.html',{'product':product})


def artists_dashboard(request):
    return render(request,'artists_dashboard.html')

from artists.models import Artists

def artist_details(request):
    Artist= Artists.objects.all()
    return render(request,'artist_details.html',{'Artist':Artist})


from artists.forms import ArtistForm

def artists(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artist_details.html')
    else:
        form = ArtistForm()
    return render(request,"artists.html",{'form':form})


from django.shortcuts import render,redirect
from artworks.models import Artworks
from artworks.forms import ArtworkForm


def add_art_work(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('art_work_details')
    else:
        form = ArtworkForm()
    return render(request,"add_art_work.html",{'form':form})


def art_work_details(request):
    artworks = Artworks.objects.all()
    return render(request, "art_work_details.html",{'artworks':artworks})


# def shop(request):
#     return render(request,'shop.html')

# def art_work_details(request):
#     return render(request,'art_work_details.html')

# def add_art_work(request):
#     return render(request,'add_art_work.html')

# from artworks.models import Artworks

# def art_work_details(request, name):
#     artwork = Artworks.objects.all(Artworks,name=name)
#     return render(request, 'art_work_details.html',{'artwork':artwork})

# def Login(request):
#     return render(request,'Login.html')

# def Register(request):
#     return render(request,'Register.html')
# from artworks.models import Artworks
# def add_art_work(request):
#     if request.method == 'POST':
#         Artwork_id = request.POST['Artwork_id']
#         title = request.POST['title']
#         artist_id = request.POST['artist_id']
#         artist_name = request.POST['artist_name']
#         medium = request.POST['medium']
#         dimensions = request.POST['dimensions']
#         category = request.POST['category']
#         price = request.POST['price']
#         description = request.POST['description']
#         status = request.POST['status']
#         image_url=request.POST['image_url']
       
#         artworks= Artworks(
#             Artwork_id=Artwork_id,
#             title=title,
#             artist_id=artist_id,
#             artist_name=artist_name,
#             medium=medium,
#             dimensions=dimensions,
#             category=category,
#             price=price,
#             description=description,
#             status=status,
#             image_url=image_url,
#         )
#         artworks.save()
        

#     return render(request, 'add_art_work.html')