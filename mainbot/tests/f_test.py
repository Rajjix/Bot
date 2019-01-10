from mainbot.messages import MessageHandler

def test_msg_handler():
    test = MessageHandler()
    try:
        assert test.handle_msg('hello') == 'Please Choose a Pizza size (big, small)', 'error 1'
        assert test.handle_msg('no_size') == 'Choose a pizza size', 'error 2'
        assert test.handle_msg('big') == 'Please Choose a payment method(card or cash)', 'error 3'
        assert test.handle_msg('no_payemnt') == 'Choose a payment method', 'error 4'
        assert test.handle_msg('card') == 'Please Confirm your order', 'error 5'
        assert test.handle_msg('answer') == 'pick either yes or no', 'error 6'
        assert test.handle_msg('yes') == 'Order has been confirmed', 'error 7'
    except Exception as e:
        print(e)
    else:
        print("Test Passed!!! \n")

test_msg_handler()
