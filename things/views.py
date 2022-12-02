from django.shortcuts import render
from .forms import ThingForm
from django.shortcuts import redirect

def home(request):
    if request.method == "POST":
        form = ThingForm(request.POST)
        if form.is_valid():
            form = form.save()
            redirect("home")
    else:
        form = ThingForm()
    return render(request, 'home.html', {'form': form})
