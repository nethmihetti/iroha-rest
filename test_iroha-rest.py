import json
import unittest


import app
import requests

class IrohaTestCase(unittest.TestCase):
    """This class represents the bucketlist test case"""

    # def setUp(self):
    #     app.run(debug=True)

    def test_app_get_tasks(self):
        """Test API can create a bucketlist (POST request)"""
        r = requests.get('http://127.0.0.1:5000/todo/api/v1.0/tasks')
        self.assertEqual(r.status_code, 200)
        self.assertIn('{"tasks":[{"description":"Milk, Cheese, Pizza, Fruit, Tylenol","done":false,"id":1,"title":"Buy groceries"},{"description":"Need to find a good Python tutorial on the web","done":false,"id":2,"title":"Learn Python"}]}', r.text)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()