from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from apps.sql_alchemy_config import Base
from apps.sql_alchemy_config import engine


class RssFeed(Base):
    __tablename__ = 'rss_feed'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    url = Column(String(1024), unique=True)

    def __repr__(self):
        return "<RssFeed(name='%s', url='%s')>" % (self.name, self.url)


Base.metadata.create_all(engine)
