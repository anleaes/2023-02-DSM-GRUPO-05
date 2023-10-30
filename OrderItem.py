class OrderItem:
    def __init__(self, quantity, unitary_price, order, product):
        self._quantity = quantity
        self._unitary_price = unitary_price
        self._order = order
        self._product = product

    def showOrderItemPrice(self):
        totalPriceItem = self._quantity * self._unitary_price
        print(self._product.showInfo() + 'preco : ' + totalPriceItem)
