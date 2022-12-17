from django.urls import path
from portfolio.views import *
from api.views import *



urlpatterns = [
    path('', home, name='home'),
    path('all/', all_works, name='all_works'),
    path('work/<int:pk>/', work, name='detail-work'),
]
