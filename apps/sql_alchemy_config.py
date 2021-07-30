from django.conf import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine(settings.DATABASE_URL)
Session = sessionmaker(bind=engine)
