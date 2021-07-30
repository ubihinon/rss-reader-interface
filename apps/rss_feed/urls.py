from django.urls import path

from apps.rss_feed.views import RssFeedItemDetailsView
from apps.rss_feed.views import RssFeedItemsView

urlpatterns = [
    path('', RssFeedItemsView.as_view(), name='news-list'),
    path('<int:pk>/', RssFeedItemDetailsView.as_view(), name='news-item-details'),
]
