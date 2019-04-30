from django.urls import path
from TrimExtraction_Services import views
from django.conf.urls import url

urlpatterns = [
    url(r'^TestEndPoint/', views.TestEndPoint),
    url(r'^ReceiveImage/', views.ReceiveImage)
]
