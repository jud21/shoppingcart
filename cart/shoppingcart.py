class Cart():
    def __init__(self, items):
        self.items = items
        
   # show the items inside of cart
    def showItems(self):
        print('Here are the contents of your cart:')
        for item in self.items:
            print(item)
                    
    # adding items to my cart
    def addItems(self):
        product = input('What would you like to add?')
        self.items.append(product)
        
    # deleting items from my cart
    def delItems(self):
        product = input('What would you like to remove?')
        self.items.remove(product)
    
    # Quit
    def quitShopping(self):
        print('Thank you for shopping with us today!')
        print('Here is your final list:')
        for item in self.items:
            print(item)
        
def shop():
    shopper = Cart([])
    while True:
        response = input('What would you like to do? Add Item/Show Items/Delete Item/Quit ')
        
        if response.lower() == 'quit':
            shopper.quitShopping()
            break
        
        elif response.lower() == 'add item':
            shopper.addItems()
            
        elif response.lower() == 'show items':
            shopper.showItems()
            
        elif response.lower() == 'delete item':
            shopper.delItems()
           
        else:
            print('State a valid command.')
            
shop()