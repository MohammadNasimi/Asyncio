# Event Bus
class EventBus:
    subscribers = {}

    @classmethod
    def subscribe(cls, event_type, subscriber):
        if event_type not in cls.subscribers:
            cls.subscribers[event_type] = []
        cls.subscribers[event_type].append(subscriber)

    @classmethod
    def publish(cls, event_type, data=None):
        if event_type in cls.subscribers:
            for subscriber in cls.subscribers[event_type]:
                subscriber.handle_event(event_type, data)


# Event Subscriber
class OrderNotificationSubscriber:
    def handle_event(self, event_type, data=None):
        if event_type == 'OrderPlaced':
            print(f"Notification: Your order with ID has been placed {data['order_id']}")


# Event Publisher
class OrderService:
    def place_order(self, order_id):
        # Order placement logic here
        # ...

        # Notify subscribers about the order placement
        EventBus.publish('OrderPlaced', {'order_id': order_id})


# Example Usage
if __name__ == "__main__":    # Creating instances
    order_notification_subscriber = OrderNotificationSubscriber()
    order_service = OrderService()

    # Subscribing the subscriber to the 'OrderPlaced' event
    EventBus.subscribe('OrderPlaced', order_notification_subscriber)

    # Placing an order
    order_service.place_order(order_id=123)

