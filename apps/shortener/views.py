from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from apps.analytics.models import ClickEvent
from .forms import SubmitUrlForm
from .models import LftURL
# Create your views here.

def home_view_fbv(request, *args, **kwargs):
    if request.method == 'POST':
        print(request.POST)
    return render(request, "shortener/home.html")

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        bg_image = "https://en.wikipedia.org/wiki/Seattle#/media/File:Space_Needle002.jpg"
        context = {
            "title": "Microl.ink",
            "form": the_form,
            "bg_image": bg_image 
        }
        return render(request, "shortener/home.html", context) 

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Microl.ink",
            "form": form
        }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = LftURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"
        return render(request, template, context)

# def lft_redirect_view(request, shortcode=None, *args, **kwargs): #function based view
#     obj = get_object_or_404(LftURL, shortcode=shortcode)
#     #do something
#     return HttpResponseRedirect(obj.url)


class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs): #class based view
        qs = LftURL.objects.filter(shortcode_iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)

    def post(self, request, *args, **kwargs):
        return HttpResponse()



'''
def lft_redirect_view(request, shortcode=None, *args, **kwargs): #function based view
    obj = LftURL.objects.get(shortcode=shortcode)
    try: 
        obj = LftURL.objects.get(shortcode=shortcode)
    except: 
        obj = LftURL.objects.all().first()

def lft_redirect_view(request, shortcode=None, *args, **kwargs): #function based view
    # obj_url = None
    # qs = LftURL.objects.filter(shortcode_iexact=shortcode.upper())
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    #     obj_url = obj.url
'''