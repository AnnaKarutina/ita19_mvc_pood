import exceptions
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def addItem(self, name, price, amount):
        try:
            self.model.addItem(name, price, amount)
            print("Ok!")
        except:
            print("Problem!")

    def showItems(self):
        items = self.model.showItems()
        self.view.showItems(items)

    def showItem(self, name):
        try:
            item = self.model.showItem(name)
            self.view.showItem(item)
        except:
            self.view.noItemError(name)

    def updateItem(self, name, price, amount):
        try:
            self.model.updateItem(name, price, amount)
            self.view.updateItem(name)
            self.showItem(name) # controller method showItem
        except:
            self.view.noItemToUpdateError(name)
            self.view.noItemError(name)

    def deleteItem(self, name):
        try:
            self.model.deleteItem(name)
            self.view.deleteItem(name)
            self.showItems() # controller method showItem
        except:
            self.view.noItemToDeleteError(name)
            self.view.noItemError(name)
    def deleteItems(self):
        try:
            self.model.deleteItems()
            self.view.deleteItems()
        except:
            self.view.noItemsToDeleteError()