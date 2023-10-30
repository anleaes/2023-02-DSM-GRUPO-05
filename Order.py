class Order:
    def __init__(self, total_price, status, client):
        self._total_price = total_price
        self._status = status
        self._client = client


    def showInfo(self):
        print(self._client.nome + 'comprou por' + self._total_price + ' e o pedido está' + self._status )


