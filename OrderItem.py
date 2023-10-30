class OrderItem:
    def __init__(self, quantity, unitary_price, order, product):
        self._quantity = quantity
        self._unitary_price = unitary_price
        self._order = order
        self._product = product

    def showPercentageOfTotal(self):
        totalpriceItem = self._quantity * self._unitary_price
        percentage = (totalpriceItem * 100) / self._order.self._total_price()
        print('o item ocupa' + percentage + ''%'da compra')
