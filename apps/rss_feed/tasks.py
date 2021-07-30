from celery import shared_task
from celery.utils.log import get_task_logger

from apps.rss_feed.services import RssFeedService

logger = get_task_logger(__name__)


@shared_task
def receive_news():
    feed_service = RssFeedService()
    feed_service.receive()
    logger.info('News received')
