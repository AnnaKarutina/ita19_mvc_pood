class View:
    # show items
    def showItems(self, items):
        print("Shop items")
        print("============================")
        print("name\t|\tprice\t|\tamount")
        for item in items:
            print(item.getName()+"\t|\t"+
                  str(item.getPrice())+"\t\t|\t"+
                  str(item.getAmount()))
            print("---------------------------")
        print("============================")
    # show item
    def showItem(self, item):
        print("Shop item {}".format(item.getName()))
        print("============================")
        print("name\t|\tprice\t|\tamount")
        print(item.getName()+"\t|\t"+
                  str(item.getPrice())+"\t\t|\t"+
                  str(item.getAmount()))
        print("---------------------------")
        print("============================")

    # no item error
    def noItemError(self, name):
        print("============================")
        print("Shop do no not consist item {}".format(name))
        print("============================")

    # no item to update error
    def noItemToUpdateError(self, name):
        print("============================")
        print("Not possible to update item {}".format(name))
        print("============================")

    # update item
    def updateItem(self, name):
        print("Shop item {} is updated".format(name))
        print("============================")