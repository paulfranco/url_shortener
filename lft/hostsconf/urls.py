from django.conf.urls import url
from .views import wildcard_redirect

from .views
urlpatterns = [
    url(r'^(?P<path>.*)', admin.site.urls),
]