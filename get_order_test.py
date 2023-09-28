# Алина Вельдемар, когорта 08-а - Финальный проект. Инженер по тестированию плюс

import sender_stand_request


def test_assert():
    """Функция для выполнения проверки."""
    order_responce = sender_stand_request.get_order()
    assert order_responce.status_code == 200

