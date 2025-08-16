from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.QuoteListView.as_view(), name='quote_list'),
    path('quote/<int:pk>/', views.QuoteDetailView.as_view(), name='quote_detail'),
    path('author/add/', views.AddAuthorView.as_view(), name='add_author'),
    path('quote/add/', views.AddQuoteView.as_view(), name='add_quote'),

    path('login/', auth_views.LoginView.as_view(template_name='quotes/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='quote_list'), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),

    path('tag/<str:tag_name>/', views.QuotesByTagView.as_view(), name='quotes_by_tag'),
]
