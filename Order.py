class Order:
    def __init__(self, total_price, status, client):
        self._total_price = total_price
        self._status = status
        self._client = client


    def getStatus(self):
        print(self._status)