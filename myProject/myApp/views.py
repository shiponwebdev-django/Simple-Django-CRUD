from django.shortcuts import render, redirect, get_object_or_404
from .models import AboutModel
from django.core.files.storage import FileSystemStorage


# Show all data
def about_list(request):
    data = AboutModel.objects.all()
    return render(request, 'about_list.html', {'data': data})


# Create / Add data
def about_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Address = request.POST.get('Address')
        Age = request.POST.get('Age')
        date_of_birth = request.POST.get('date_of_birth')
        Education = request.POST.get('Education')
        department = request.POST.get('department')
        image = request.FILES.get('image')

        AboutModel.objects.create(
            name=name,
            Address=Address,
            Age=Age,
            date_of_birth=date_of_birth,
            Education=Education,
            department=department,
            image=image
        )

        return redirect('about_list')

    return render(request, 'about_create.html')


# Update / Edit data
def about_update(request, id):
    data = get_object_or_404(AboutModel, id=id)

    if request.method == "POST":
        data.name = request.POST.get('name')
        data.Address = request.POST.get('Address')
        data.Age = request.POST.get('Age')
        data.date_of_birth = request.POST.get('date_of_birth')
        data.Education = request.POST.get('Education')
        data.department = request.POST.get('department')

        if request.FILES.get('image'):
            data.image = request.FILES.get('image')

        data.save()

        return redirect('about_list')

    return render(request, 'about_update.html', {'data': data})


# Delete data
def about_delete(request, id):
    data = get_object_or_404(AboutModel, id=id)
    data.delete()
    return redirect('about_list')