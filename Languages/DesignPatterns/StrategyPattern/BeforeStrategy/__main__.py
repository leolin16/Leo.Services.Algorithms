from .before_strategy import order, shipper, shipping_cost

# Test Federal Express shipping

order = order.Order(shipper.Shipper.fedex)
cost_calculator = shipping_cost.ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0

print('Tests passed')