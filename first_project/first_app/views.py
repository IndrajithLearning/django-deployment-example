from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,WebPage,AccessReocrd
from first_app.forms import FormName

# Create your views here.

def index(request):
    wepages_list = AccessReocrd.objects.order_by("date")
    date_dict = {"acc_rec":wepages_list}
    return render(request,"first_app/index.html",context=date_dict)


def forms(request):
    form = FormName()
    if request.method == "POST":
        form = FormName(request.POST)

        if form.is_valid():
            print("Validation Success")
            print("Name" + form.cleaned_data["name"])
            print("Email"+form.cleaned_data["email"])
            print("Text"+form.cleaned_data["text"])
    return render(request,"forms/forms.html",{"form":form})




