    assert price >= 0, f"Price - {price} is not greater than zero"
            assert quantity >= 0, f"Quantity - {quantity} is not greater than zero"
            assert brokenPhone >= 0, f"Broken phone - {brokenPhone} is not greater than zero"

            self.name = name
            self.price = price
            self.quantity = quantity
            self.brokenPhone = brokenPhone

            Phone.all.append(self)