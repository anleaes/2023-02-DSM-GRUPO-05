from categoria import categoria

class produto(categoria):
    def __init__(self, name, description, date_fabrication, is_active, category):
        self.name = name
        self.description = description
        self.date_fabrication= date_fabrication
        self.is_active = is_active
        self.category = category
        

