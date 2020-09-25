import exceptions
from product import Product

# repsresents shop structure
# list of Product type objects
items = []

# add item to items
def addItem(name, price, amount):
    global items
    # create product with reqiure description
    product = Product(name, price, amount)
    # control is item already exists
    if product in items:
        raise exceptions.ItemExists("Item {} is exists".format(name))
    else:
        items.append(product)
# show items
def showItems():
    global items
    # control if items exists
    if len(items) == 0:
        raise exceptions.ItemNotExists("List of items is empty")
    else:
        return items
# show item
def showItem(name):
    global items
    # control all items step by step
    for item in items:
        # if the name is the same as we search
        if(item.getName() == name):
            return item
        else:
            continue
            raise exceptions.ItemNotExists("Not found {} item".format(name))

# update item
def updateItem(name, price, amount):
    global items
    isUpdated = False
    # control all items step by step
    for item in items:
        # if the name is the same as we search
        if(item.getName() == name):
            # update item
            item.setPrice(price)
            item.setAmount(amount)
            isUpdated = True
        else:
            continue
    # control if is not updated - error message
    if(isUpdated != True):
        raise exceptions.ItemNotExists("Not found {} item".format(name))

# delete item
def deleteItem(name):
    global items
    isDeleted = False
    # control all items step by step
    for item in items:
        # if the name is the same as we search
        if(item.getName() == name):
            # delete item
            items.remove(item)
            isDeleted = True
        else:
            continue
    # control if is not updated - error message
    if(isDeleted != True):
        raise exceptions.ItemNotExists("Not found {} item".format(name))

# delete all items
def deleteItems():
    global items
    # if items contains more than 0 elements
    if(len(items) > 0):
        items.clear()
    else:
        raise exceptions.ItemNotExists("Not found any items")