# Subsystems classes
class FlowerSelector:
    def choose_flowers(self, occasion):
        print(f"Selecting flowers for {occasion}...")

class BouquetPreparation:
    def arrange_bouquet(self):
        print("Arranging the bouquet...")

class Packaging:
    def wrap_bouquet(self):
        print("Wrapping the bouquet...")

class Delivery:
    def deliver(self, address):
        print(f"Delivering the bouquet to {address}...")

class Payment:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}...")
        
class orderConfirmation:
    def confirm_order(self, order_id):
        print(f"Order {order_id} has been confirmed.")
    

# Facade class
class FlowerShopFacade:
    def __init__(self):
        self.selector = FlowerSelector()
        self.bouquet_preparation = BouquetPreparation()
        self.packaging = Packaging()
        self.delivery = Delivery()
        self.payment = Payment()
        self.orderConfirmation = orderConfirmation()
        

    def send_flowers(self, occasion, address, amount, order_id):
        print("Processing flower delivery order...")
        self.selector.choose_flowers(occasion)
        self.bouquet_preparation.arrange_bouquet()
        self.packaging.wrap_bouquet()
        self.delivery.deliver(address)
        self.payment.process_payment(amount)
        self.orderConfirmation.confirm_order(order_id)
        print("Flower delivery complete!")

# Client
if __name__ == "__main__":
    shop = FlowerShopFacade()
    shop.send_flowers("birthday", "123 , hometown", "1000", "079369 \n")
    shop.send_flowers("wedding", "456 , model town", "700", "123456 \n")
    shop.send_flowers("graduation", "789 , block B", "500", "926404 \n")