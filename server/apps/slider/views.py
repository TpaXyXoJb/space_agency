from django.views.generic import ListView
from .models import Picture


class PictureListView(ListView):
    model = Picture
    template_name = 'index.html'
    queryset = Picture.objects.all()
    context_object_name = 'picture_list'
