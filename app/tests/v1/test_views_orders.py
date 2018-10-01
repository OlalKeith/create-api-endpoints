import unittest, os , sys
import json

# LOCALPATH = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, LOCALPATH + '/../../../')

from app import create_app

class TestGettingAllorders(unittest.TestCase):

	def setUp(self):
		self.app = create_app("testing")
		self.app.testing = True
		self.client = self.app.test_client()

	"""Test get all orders"""
	# def test_get_orders(self):
	# 	make_response = self.client.get('/api/v1/orders', content_type='application/json')
	# 	self.assertEqual(make_response.status_code, 200)

	"""Test get single orders"""
	def test_single_order(self):
		make_response = self.client.get('/api/v1/orders/<int:order_id>', content_type='application/json')
		self.assertEqual(make_response.status_code, 404)

	"""Test update orders"""
	def test_update_order(self):
		make_response = self.client.put('/api/v1/orders/<int:order_id>', content_type = 'application/json')
		self.assertEqual(make_response.status_code, 404)
		"""Test place orders"""
	def test_place_oder(self):
		make_response = self.client.post('/api/v1/order', content_type='application/json' )
		self.assertEqual(make_response.status_code, 400)
		"""Test delete an order"""
	def test_delete_oder(self):
		make_response = self.client.post('/api/v1/orders/<int:order_id>', content_type='application/json' )
		self.assertEqual(make_response.status_code, 404)


