from django.urls import include, path


from . import views as cores_views

urlpatterns = [
    path('', cores_views.IndexListView.as_view(), name='index'),
]
