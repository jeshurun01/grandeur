from django.shortcuts import render, redirect
from . import models, forms


def index(request):
    return render(request, 'blog/index.html')


def infos(request):
    notifications = models.Notification.objects.all().order_by('-created')[:5]
    context = {
        'notifications': notifications,
    }
    return render(request, 'blog/infos.html', context)


def notes(request):
    return render(request, 'blog/notes.html')


def contact(request):
    print("Contact")
    if request.method == "POST":
        form = forms.FeedbackForm(request.POST)
        print(form)
        if form.is_valid():
            print('okay')
            form.save()
            return redirect('blog:home')
        else:
            print("error")
    else:
        form = forms.FeedbackForm()
    return render(request, 'blog/contact.html', {'form': form})


def about_us(request):
    return render(request, 'blog/about.html')
