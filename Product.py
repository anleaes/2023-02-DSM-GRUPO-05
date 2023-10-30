import Category
from datetime import datetime
class Product:

    def __init__(self,name,description,date_fabrication, is_active, category):
        self._name = name
        self._description = description
        self._date_fabrication = date_fabrication
        self._is_active = is_active
        self._category = category


    def showAge(self):
        if self._is_active:
            now = datetime.now()
            age = now - self._date_fabrication
            age = age.strftime("%Y")
            print('esse produto esta no mercado a : ' + age  + 'anos')
        else :
            print('esse produto esta desativado')