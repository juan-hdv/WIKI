from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:entry>', views.pageShow, name="pageShow"),
    path('search', views.pageSearch, name="pageSearch"),
    path('pageNew', views.pageNew, name="pageNew"),
    path('pageEdit/<str:entry>', views.pageEdit, name="pageEdit"),
    path('pageRandom', views.pageRandom, name="pageRandom"),
    path('delwiki/<str:entry>', views.pageDelete, name="pageDelete")
]
