import helpers

class Model:
    # get shop data - [] of products
    def __init__(self, items):
        self.items = items
    # add item to items
    def addItem(self, name, price, amount):
        helpers.addItem(name, price, amount)
    # show items
    def showItems(self):
        return helpers.showItems()
    # show item
    def showItem(self, name):
        return helpers.showItem(name)
    # update item
    def updateItem(self, name, price, amount):
        helpers.updateItem(name, price, amount)
    # delete item
    def deleteItem(self, name):
        helpers.deleteItem(name)
    # delete items
    def deleteItems(self):
        helpers.deleteItems()