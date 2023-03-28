import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quote:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quote:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """
  
  def test_getDataPoint_calculatePriceWithZero(self):
    quotes = [
        {'top_ask': {'price': 125.5, 'size': 5}, 'timestamp': '2022-07-02 10:09:30.572453', 'top_bid': {'price': 0, 'size': 0}, 'id': '0.007706517292', 'stock': 'ABC'},
        {'top_ask': {'price': 0, 'size': 0}, 'timestamp': '2022-07-02 10:09:30.572453', 'top_bid': {'price': 125.45, 'size': 26}, 'id': '0.007706517295', 'stock': 'DEF'},
        {'top_ask': {'price': 120.88, 'size': 8}, 'timestamp': '2022-07-02 10:09:30.572453', 'top_bid': {'price': 122.7, 'size': 11}, 'id': '0.0077065194223', 'stock': 'GHI'}
    ]
    for quote in quotes:
        if quote['top_bid']['price']==0 or quote['top_ask']['price'] == 0:
            with self.assertRaises(ZeroDivisionError):
                getDataPoint(quote)
        else:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))


if __name__ == '__main__':
    unittest.main()
