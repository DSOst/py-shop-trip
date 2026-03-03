class Shop:
    def __init__(self, name: str,
                 location: list[int],
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_products_cost(self, product_cart: dict) -> float :
        total_sum = 0
        for product, quantity in product_cart.items():
            total_sum += quantity * self.products[product]
        return total_sum

    def print_receipt(self, customer_name: str,
                      product_cart: dict) -> None:
        date_str = "04/01/2021 12:33:41"
        print(f"Date: {date_str}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total = 0
        for product, quantity in product_cart.items():
            price = self.products[product] * quantity
            total += price
            print(f"{quantity} {product}s for {price:g} dollars")
        print(f"Total cost is {round(total, 2)} dollars")
        print("See you again!\n")
