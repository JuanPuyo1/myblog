from django.urls import path

urlspattern = [
    path("", views.index),
    path("posts"),
    path("posts/<slug:slug>")
]