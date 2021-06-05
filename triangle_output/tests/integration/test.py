import unittest
import requests
import json

class IntegrationTestCompute(unittest.TestCase):

    
    def test_compute_area(self):
        check_sides_url = "http://13.212.56.51:8080/check-sides"
        requests.post(check_sides_url, json={'sides': [3,4,5]})
        # status_code = r.status_code
        
        get_area_url = "http://13.212.56.51:8081/area"
        r = requests.get(get_area_url)
        r_json = r.json()
        area = r_json['area']
        
        self.assertEqual(area, 6.0)
        
    
    def test_compute_perimeter(self):
        check_sides_url = "http://13.212.56.51:8080/check-sides"
        requests.post(check_sides_url, json={'sides': [3,4,5]})
        # status_code = r.status_code
        
        get_perimeter_url = "http://13.212.56.51:8081/perimeter"
        r = requests.get(get_perimeter_url)
        r_json = r.json()
        perimeter = r_json['perimeter']
        
        self.assertEqual(perimeter, 12.0)
        
        
    def test_compute_area_and_perimeter(self):
        check_sides_url = "http://13.212.56.51:8080/check-sides"
        requests.post(check_sides_url, json={'sides': [3,4,5]})
        # status_code = r.status_code
        
        get_area_and_perimeter_url = "http://13.212.56.51:8081/area-and-perimeter"
        r = requests.get(get_area_and_perimeter_url)
        r_json = r.json()
        area = r_json['area']
        perimeter = r_json['perimeter']
        
        self.assertEqual(area, 6.0)
        self.assertEqual(perimeter, 12.0)

    
    if __name__ == '__main__':
        unittest.main()