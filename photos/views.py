from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo, Category

def About(request):
    return render(request, 'about.html')

def Gallery(request):
    category = request.GET.get('category') # for categories in left card

    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'home.html', context)


def Pics(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name = category)

    categories = Category.objects.all()
    context = {'categories' : categories,
               'photos': photos}
    return render(request, 'pics.html', context)


def Image(request, pk):
    photo = Photo.objects.get(id = pk)
    return render(request, 'photo.html', {'photo' : photo})

def Add(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id = data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name = data['category_new'])
        else:
            category = None
        
        photo = Photo.objects.create(
            category = category,
            description = data['description'],
            image = image,
        )
        return redirect('picture', pk = photo.pk)

    context = {'categories': categories}
    return render(request, 'add.html', context)

def PhotoUp(request, pk):
    photo = get_object_or_404(Photo, id = pk)
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id = data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name = data['category_new'])
        else:
            category = None

        photo.category = category
        photo.description = data['description']
        if image:
            photo.image = image
        photo.save()
        return redirect('picture', pk = pk)
    
    return render(request, 'update.html', {'photo': photo, 'categories': categories})


def PhotoDel(request, pk):
    photo = get_object_or_404(Photo, id = pk)

    if request.method == 'POST':
        photo.delete()
        return redirect('pictures')

    return render(request, 'delete.html', {'photo':photo})