from machine.states import Order

class MessageHandler:
    
    accepted_commands = [
            'order',
            'small',
            'cash',
            'card',
            'big',
            'yes',
            'no']

    commands = {
        'started': 'handle_start',
        'start__size': 'handle_size',
        'start__pay': 'handle_payment',
        'confirming': 'handle_confirm',
        }

    def __init__(self):
        self.order = Order()

    def handle_msg(self, msg):
        msg = msg.lower()
        return getattr(self, self.commands[self.order.state])(msg)

    def handle_start(self, msg=None):
        self.order.to_start__size()
        return 'Please Choose a Pizza size (big, small)'

    def handle_size(self, msg):
        if 'big' in msg or 'small' in msg:
            self.order.end_size()
            self.order.start_pay()
            return 'Please Choose a payment method(card or cash)'
        return 'Choose a pizza size'

    def handle_payment(self, msg):
        if 'cash' in msg or 'card' in msg:
            self.order.end_pay()
            self.order.start_confirm()
            return 'Please Confirm your order'
        return 'Choose a payment method'

    def handle_confirm(self, msg):
        if 'no' in msg:
            self.order.cancel
            return 'Order has been cancelled'
        elif 'yes' in msg:
            self.order.confirm()
            return 'Order has been confirmed'
        return 'pick either yes or no'
