from django.urls import path, include
from .views import create_follower

urlpatterns = [
    path('create', create_follower, name='follow_user'),
    # path('<int:pk>/detail/', CategoryDetail.as_view()),
]


