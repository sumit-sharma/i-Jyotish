from django.urls import path, include
from .views import CreateFollower

urlpatterns = [
    path('create', CreateFollower.as_view()),
    # path('<int:pk>/detail/', CategoryDetail.as_view()),
]


