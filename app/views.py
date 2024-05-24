from django.shortcuts import get_object_or_404, redirect, render

from shortner.models import UrlDB

# Create your views here.
def home(request):
    # UrlDB.objects.all().delete()
    return render(request, 'index.html')

def redir(request, short_id):
    # url_instance = UrlDB.objects.get(short_id=short_id)
    url_instance = get_object_or_404(UrlDB, short_id=short_id)
    print(url_instance)
    return redirect(url_instance.resource_url)