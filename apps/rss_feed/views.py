from django.http import HttpResponseNotFound
from django.views.generic import TemplateView
from sqlalchemy import desc

from apps.rss_feed.models import RssFeedItem
from apps.sql_alchemy_config import Session


class RssFeedItemsView(TemplateView):
    template_name = 'rss_feed_item_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session = Session()
        context['object_list'] = session.query(RssFeedItem).order_by(desc(RssFeedItem.publish_date)).all()
        session.close()
        return context


class RssFeedItemDetailsView(TemplateView):
    template_name = 'rss_feed_item_details.html'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        news_id = kwargs.get('pk')
        news_id = int(news_id)
        if news_id:
            session = Session()
            if not session.query(RssFeedItem).filter(RssFeedItem.id == news_id).first():
                return HttpResponseNotFound('<h1>Page not found</h1>')
            session.close()

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_id = kwargs.get('pk')
        news_id = int(news_id)
        if news_id:
            session = Session()
            context['object'] = session.query(RssFeedItem).filter(RssFeedItem.id == news_id).first()
            session.close()
        return context
