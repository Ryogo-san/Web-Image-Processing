from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='recognition'

urlpatterns=[
        path('',views.IndexView.as_view(),name="index"),
        path('prediction',views.PredictionView.as_view(),name="prediction"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
