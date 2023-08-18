from django.urls import path
from . import views



urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # path('', views.home, name='home'),
    path('details/<int:pk>', views.ContactDetailView.as_view(), name='detail'),
    # path('/details/<int:id>', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    # path('/search/', views.ContactSearchView.as_view(), name='search'),
    path('contact/create', views.ContactCreateView.as_view(), name='create'),
    path('contact/update/<int:pk>', views.ContactUpdateView.as_view(), name='update'),
    path('contact/delete/<int:pk>', views.ContactDeleteView.as_view(), name='delete'),
    path('signup', views.SignUpView.as_view(), name='signup'),
]
