from apps.rss_feed.models import RssFeed
from apps.sql_alchemy_config import Session

with Session.begin() as session:
    session.add_all([
        RssFeed(name='lenta', url='https://lenta.ru/rss/news'),
        RssFeed(name='tass', url='http://tass.ru/rss/v2.xml'),
    ])
