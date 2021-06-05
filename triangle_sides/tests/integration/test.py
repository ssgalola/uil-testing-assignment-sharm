import unittest
import requests
import json

class IntegrationTestChecker(unittest.TestCase):

    
    def test_checker_check_sides(self):
        check_sides_url = "http://13.212.56.51:8080/check-sides"
        r = requests.post(check_sides_url, json={'sides': [3,4,5]})
        status_code = r.status_code
        self.assertEqual(status_code, 200)
        
    
    def test_checker_get_sides(self):
        get_sides_url = "http://13.212.56.51:8080/get-sides"
        r = requests.get(get_sides_url)
        status_code = r.status_code
        self.assertEqual(status_code, 200)
        
    
    def test_checker_check_sides_err(self):
        check_sides_url = "http://13.212.56.51:8080/check-sides"
        r = requests.post(check_sides_url, json={'sides': [8,1,9]})
        status_code = r.status_code
        self.assertEqual(status_code, 400)
    
    def test_checker_get_sides_err(self):
        get_sides_url = "http://13.212.56.51:8080/get-sides"
        r = requests.get(get_sides_url)
        status_code = r.status_code
        self.assertEqual(status_code, 400)

    
    if __name__ == '__main__':
        unittest.main()