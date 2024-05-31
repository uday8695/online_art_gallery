# from django.shortcuts import render,redirect
# from artworks.models import Artworks
# from artworks.forms import ArtworkForm


# def add_art_work(request):
#     if request.method == 'POST':
#         form = ArtworkForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('art_work_details')
#     else:
#         form = ArtworkForm()
#     return render(request,'add_art_work.html',{'form':form})


# def art_work_details(request):
#     artworks = Artworks.objects.all()
#     return render(request, 'art_work_details.html',{'artworks':artworks})
