from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, brokenPhone=0):
        # Calling super fn to have access to all attributes / methods of parents class
        super().__init__(
            name, price, quantity
        )

        assert brokenPhone >= 0, f"Broken phone - {brokenPhone} is not greater than zero"

        self.brokenPhone = brokenPhone
