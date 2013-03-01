from paypal.resource import List, Find, Create, Post, Resource

# == Example
#  payment_histroy = Payment.all({"count": 5})
#  payment = Payment.find("PAY-1234")
#  payment = Payment.new({"intent": "sale"})
#
#  payment.create     # return True or False
#  payment.execute({"payer_id": 1234})  # return True or false
class Payment(List, Find, Create, Post):

  path = "v1/payments/payment"

  def execute(self, attributes = {}):
    return self.self_post('execute', attributes)

Resource.convert_resources['payments'] = Payment
Resource.convert_resources['payment']  = Payment

# == Example
#  sale = Sale.find("98765432")
#
#  refund = sale.refund({"amount": {"total": "1.00", "currency": "USD"}})
class Sale(Find, Post):

  path = "v1/payments/sale"

  def refund(self, attributes = {}):
    return self.post('refund', attributes)

Resource.convert_resources['sales'] = Sale
Resource.convert_resources['sale'] = Sale