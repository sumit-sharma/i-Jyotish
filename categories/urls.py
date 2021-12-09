from django.urls import path, include
from .views import CategoryDetail, CategoryList

urlpatterns = [
    path('', CategoryList.as_view()),
    path('<int:pk>/detail/', CategoryDetail.as_view()),
]
