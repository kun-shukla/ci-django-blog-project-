from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm
# Create your views here.

def about_content(request):
    about = About.objects.all().order_by("-updated_on").first()
    if request.method == "POST":
        collab_form = CollaborateForm(data=request.POST)
        if collab_form.is_valid():
            collab_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )
            
    collab_form = CollaborateForm()

    print("About to render template")

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collab_form": collab_form,
        },
    )
