import time
import requests
import random

from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)
    
    @task
    def get_area(self):
        self.client.get("/get-area")
        
    @task
    def get_perimeter(self):
        self.client.get("/get-perimeter")
        
    @task
    def get_area_and_perimeter(self):
        self.client.get("/get-area-and-perimeter")