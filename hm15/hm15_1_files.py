"""Homework 15 - 9. Enum

Создайте OrderStatus — Enum, который содержит следующие статусы:
PENDING (Заказ ожидает обработки)
IN_PROGRESS (Заказ готовится)
READY (Заказ готов)
COMPLETED (Заказ выдан)
CANCELLED (Заказ отменён)
Реализуйте класс Order, который:

Принимает order_id и статус (по умолчанию PENDING).
Содержит метод update_status(new_status), который обновляет статус заказа.
Содержит метод display_status(), который выводит текущий статус заказа."""

from enum import Enum

OrderStatus = Enum('OrderStatus', 'IN_PROGRESS READY COMPLETED CANCELLED PENDING', start=1)


class Order:
    """
    make an order
    """
    def __init__(self, order_id, status):
        self.order_id = order_id
        self.status = status

    def update_status(self, new_status):
        """
        update_status
        """
        self.order_id = new_status.value
        self.status = new_status.name

    def display_status(self):
        """
        display_status_of _order
        """
        print(f"{self.order_id} - {self.status}")


def task_nine():
    """
    task_nine
    """
    order = Order(1, 'PENDING')
    order.display_status()

    for order_status in OrderStatus:
        order.update_status(order_status)
        order.display_status()


if __name__ == "__main__":
    task_nine()
