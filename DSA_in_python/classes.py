
class Bank:

  max_withdraw_limit = 50000

  def __init__(self, name) -> None:
    self.name = name

  def deposit(self, amount):
    pass
  
  @classmethod
  def set_withdraw_limit(cls, limit):
    cls.max_withdraw_limit = limit

  @staticmethod
  def utils():
    pass
  
"""
classes and objects
instance methods
class methods
static methods 
dunder /magic methods
Pillas ops
"""