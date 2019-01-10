from transitions import Machine

class Order(object):

    states = ['started', 'start__size', 'end__size', 'start__pay', 'end__pay', 'confirming', 'confirmed', 'cancelled']
    transitions = [
            {'trigger': 'start_size', 'source':'started', 'dest':'start__size'},
            {'trigger': 'end_size', 'source':'start__size', 'dest':'end__size'},
            {'trigger': 'start_pay', 'source':'end__size', 'dest':'start__pay'},
            {'trigger': 'end_pay', 'source':'start__pay', 'dest':'end__pay'},
            {'trigger': 'start_confirm', 'source':'end__pay', 'dest':'confirming'},
            {'trigger': 'confirm', 'source':'confirming', 'dest':'confirmed'},
            {'trigger': 'cancel', 'source':'confirming', 'dest':'cancelled'}]

    def __init__(self):
        self.machine = Machine(model=self, states=Order.states,
                               transitions=self.transitions, initial='started')
