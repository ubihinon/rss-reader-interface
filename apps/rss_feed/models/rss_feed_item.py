from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from apps.sql_alchemy_config import Base
from apps.sql_alchemy_config import engine


class RssFeedItem(Base):
    __tablename__ = 'rss_feed_item'
    id = Column(Integer, primary_key=True)
    feed_id = Column(Integer, ForeignKey('rss_feed.id'))
    link = Column(String(1024), unique=True)
    title = Column(String(100))
    publish_date = Column(DateTime())
    thumbnail = Column(String(1024), nullable=True)

    def __repr__(self):
        return "<RssFeedItem(feed_id='%s', title='%s', link='%s', publish_date='%s', thumbnail='%s')>" % (
            self.feed_id,
            self.title,
            self.link,
            self.publish_date,
            self.thumbnail
        )


Base.metadata.create_all(engine)
