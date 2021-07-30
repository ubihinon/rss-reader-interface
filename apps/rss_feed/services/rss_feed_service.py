import urllib
from datetime import datetime
from xml.etree import ElementTree

import requests
from django.templatetags.static import static

from apps.rss_feed.models import RssFeed
from apps.rss_feed.models import RssFeedItem
from apps.rss_feed.models import Session


class RssFeedService:
    def receive(self):
        with Session.begin() as session:
            for feed in session.query(RssFeed).all():
                news_xml = requests.get(feed.url)
                xml_tree = ElementTree.fromstring(news_xml.content)

                if len(xml_tree) > 0:
                    for news_item in xml_tree[0].findall('item'):
                        title = news_item.find('title').text
                        link = news_item.find('link').text
                        publication_date = news_item.find('pubDate').text
                        try:
                            thumbnail = news_item.find('enclosure').attrib['url']
                        except Exception:
                            thumbnail = None

                        if not session.query(RssFeedItem).filter(RssFeedItem.link == link).first():
                            rss_feed_item = RssFeedItem(
                                feed_id=feed.id,
                                title=title,
                                link=link,
                                publish_date=datetime.strptime(publication_date, '%a, %d %b %Y %H:%M:%S %z'),
                                thumbnail=thumbnail
                            )
                            session.add(rss_feed_item)
            session.commit()
