#!/usr/bin/env python3

class CashRegister:
  pass
  def __init__(self, discount=0):
    pass
    self.total = 0
    self.items = []
    self.discount = discount
    self.last_transaction = {
      'item': '',
      'quantity': 0,
      'price': 0
    }
  
  def add_item(self, item, price, quantity=1):
    pass
    self.total += price * quantity
    self.last_transaction['item'] = item
    self.last_transaction['quantity'] = quantity
    self.last_transaction['price'] = price
    for n in range(0, quantity):
      self.items.append(item)
  
  def apply_discount(self):
    pass
    if self.discount > 0:
      self.total = int(self.total*(1-(self.discount*0.01)))
      print(f"After the discount, the total comes to ${self.total}.")
      return

    print("There is no discount to apply.")

  def void_last_transaction(self):
    pass
    if self.last_transaction['item'] != '':
      for n in range(0, self.last_transaction['quantity']):
        self.items.remove(self.last_transaction['item'])
        self.total -= self.last_transaction['price']
    
    