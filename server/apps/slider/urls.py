from django.urls import path
from .views import PictureListView

urlpatterns = [
    path('', PictureListView.as_view(), name='slider-list'),
]
