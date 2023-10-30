import Category
class Product:

    def __init__(self,name,description,date_fabrication, is_active, category):
        self._name = name
        self._description = description
        self._date_fabrication = date_fabrication
        self._is_active = is_active
        self._category = category


    def showInfo(self):
        print('Nome: ' + self._name)
        print('Descricao: ' + self._description)
        print('data de fabricacai: ' + self._date_fabrication)
        print('esta ativado: ' + self._is_active)
        print('categoria: ' + categoy.showCategory())