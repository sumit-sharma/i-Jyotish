from django.urls import path, include
from .views import ListCategory

urlpatterns = [
    path('', ListCategory.as_view()),
]
