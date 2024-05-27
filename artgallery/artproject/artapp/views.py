from django.shortcuts import render,get_object_or_404
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

def artists(request):
    return render(request,'artists.html')

def shop(request):
    return render(request,'shop.html')

def artworks(request):
    return render(request,'artworks.html')

def artsupplies(request):
    return render(request,'artsupplies.html')

def styles(request):
    return render(request,'styles.html')


def art_work_details(request):
    return render(request,'art_work_details.html')

def add_art_work(request):
    return render(request,'add_art_work.html')

def artists_dashboard(request):
    return render(request,'artists_dashboard.html')


def artist_details(request):
    return render(request,'artist_details.html')

# from artworks.models import Artworks

# def art_work_details(request, name):
#     artwork = get_object_or_404(Artworks,name=name)
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
        

    return render(request, 'add_art_work.html')