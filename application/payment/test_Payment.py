from unittest import TestCase
from unittest.mock import Mock
from domain.models.User import User
from application.util.utils import Utils
from application.payment.Payment import Payment


class TestPayment(TestCase):
    def test_process_payment(self):
        user = Mock(spec=User)
        user.get_worked.return_value = [
            # Create mock Day objects with necessary attributes
            Mock(get_day='MO', get_start_time='08:00', get_end_time='16:00'),
            Mock(get_day='TU', get_start_time='20:00', get_end_time='02:00'),
            Mock(get_day='WE', get_start_time='10:00', get_end_time='18:00')
        ]

        # Set up the mock return values for Utils and Constantes functions
        Utils.get_worked_time.side_effect = [8, 6, 8]
        Utils.get_price_per_shift.side_effect = [15, 18, 20]

        expected_total_to_pay = (8 * 15) + (6 * 18) + (8 * 20)

        # Call the process_payment function and assert the result
        total_to_pay = Payment.process_payment(user)
        self.assertEqual(total_to_pay, expected_total_to_pay)
