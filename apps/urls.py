from django.urls import path
from .views import PersonListView, PersonDetailView, GroupListView, GroupDetailView

urlpatterns = [
    path('persons/', PersonListView.as_view(), name='person_list'),
    path('persons/<int:pk>/', PersonDetailView.as_view(), name='person_detail'),
    path('groups/', GroupListView.as_view(), name='group_list'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group_detail'),
]