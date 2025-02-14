from django.urls import path
from .views import vote, results

urlpatterns = [
    path('vote/<int:election_id>/', vote, name='vote'),
    path('results/<int:election_id>/', results, name='results')
]