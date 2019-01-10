from mainbot.messages import MessageHandler
import unittest

class TestMessageHandler(unittest.TestCase):

    def setUp(self):
        self.handler = MessageHandler()

    def test_handle_size_msg(self):
        self.handler.order.to_start__size()
        self.assertEqual(self.handler.handle_size('big'), 'Please Choose a payment method(card or cash)', 'Incorrect Output')
        self.assertNotEqual(self.handler.handle_size('adsa'), 'Please Choose a payment method(card or cash)', 'Incorrect Output')
    
    def test_handle_pay_msg(self):
        self.handler.order.to_start__pay()
        self.assertEqual(self.handler.handle_payment('cash'), 'Please Confirm your order', 'Incorrect Output')
        self.assertNotEqual(self.handler.handle_payment('adsad'), 'Please Confirm your order', 'Incorrect Output')
    
    def test_handle_confirm_msg(self):
        self.handler.order.to_confirming()
        self.assertEqual(self.handler.handle_confirm('no'), 'Order has been cancelled', 'Incorrect Output')
        self.assertNotEqual(self.handler.handle_confirm('ndasadaso'), 'Order has been cancelled', 'Incorrect Output')

if __name__ == '__main__':
    unittest.main()
