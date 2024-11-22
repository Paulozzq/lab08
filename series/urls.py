from django.urls import path
from .views import SeriesView, SerieDetailView, CategoryView, CategoryDetailView, LoginView

urlpatterns = [
    # Series
    path('series/', SeriesView.as_view(), name='series-list'), 
    path('series/<int:serie_id>/', SerieDetailView.as_view(), name='serie-detail'), 
    path('login/', LoginView.as_view(), name='login'), 
    path('categories/', CategoryView.as_view(), name='categories-list'), 
    path('categories/<int:category_id>/', CategoryDetailView.as_view(), name='category-detail'), 
]
