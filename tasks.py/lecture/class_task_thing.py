
i = 0
class Thing:
    def __init__(self, name, price):
        global i
        self.id = i
        i += 1

        self.name = name
        self.price = price
        self.weight = self.dims = self.memory = self.frm = None

    def get_data(self):
        return self.name, self.price, self.weight, self.memory, self.frm, self.dims


class Table(Thing):
    def __init__(self, name, price, weight, dims: float):
        super().__init__(name, price)
        self.dims = dims
        self.weight = weight


class EBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = EBook("Python 0ОП", 2000, 2048, 'pdf')
print(table.get_data())
print(book.get_data())