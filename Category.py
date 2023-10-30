class Category:
    def __init__(self, id, name, description):
        self._id = id
        self._name = name
        self._description = description
    
    def changeDescription(self, newDescription):
        self._description = newDescription
        print('essa e a nova descricao: ' + self._description)