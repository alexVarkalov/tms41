from django.urls import path

from catdog.views import home, get_image, save_image, filter_images, send_image

urlpatterns = [
    path('', home, name='home'),
    path('get_image/', get_image, name='get-image'),
    path('save_image/', save_image, name='save-image'),
    path('send_image/', send_image, name='send-image'),
    path('filter_images/', filter_images, name='filter-images'),
]
