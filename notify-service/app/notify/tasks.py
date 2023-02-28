from celery import shared_task
from .serializers import DepositNotificationSerializer, ReferralRewardNotificationSerializer
from .models import DepositNotification, ReferralRewardNotification
import pika, json, os
from notify.utils import validate_notification
import logging 

logger = logging.getLogger(__name__)

@shared_task(name='consume_notifications')
def consume_notifications():
    """
    Consumes notifications from the notification queue and saves them to the database
    
    :return: None

    TODO: Add error handling and start consuming on launch
    """

    user=os.environ.get('RABBITMQ_DEFAULT_USER')
    password=os.environ.get('RABBITMQ_DEFAULT_PASS')
    queue_name = os.environ.get('NOTIFICATION_QUEUE_NAME')
    host = os.environ.get('NOTIFICATION_QUEUE_HOST')
    port = os.environ.get('NOTIFICATION_QUEUE_PORT')
    exchange_name = os.environ.get('NOTIFICATION_EXCHANGE_NAME')
    routing_key = os.environ.get('NOTIFICATION_ROUTING_KEY')
    credentials = pika.PlainCredentials(user, password)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, credentials=credentials))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange_name, exchange_type='direct')
    channel.queue_declare(queue=queue_name)
    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

    def callback(ch, method, properties, body):
        notification = json.loads(body.decode('utf-8'))
        # valid, error = validate_notification(notification)
        # if not valid:
        #     logger.error("Invalid notification: {}".format(error))
        #     return
        if notification['type'] == 'D':
            push_notification.delay(notification)
            del notification['type']
            serializer = DepositNotificationSerializer(data=notification)
            if serializer.is_valid():
                serializer.save()
        elif notification['type'] == 'R':
            push_notification.delay(notification)
            del notification['type']
            serializer = ReferralRewardNotificationSerializer(data=notification)
            if serializer.is_valid():
                serializer.save()

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


@shared_task
def push_notification(notification):
    """
    Pushes a notification to the notification queue
    
    :param notification: The notification to be pushed
    :return: None
    """
    # routing_key = 'private.{}.{}'.format(notification['uid'], notification['type'])
    routing_key = 'public.test.{}'.format(notification['type'])
    user=os.environ.get('RABBITMQ_DEFAULT_USER')
    password=os.environ.get('RABBITMQ_DEFAULT_PASS')
    exchange_name = os.environ.get('RANGO_EXCHANGE_NAME')

    credentials = pika.PlainCredentials(user, password)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672, credentials=credentials))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange_name, exchange_type='topic')
    channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=json.dumps(notification))
    connection.close()
