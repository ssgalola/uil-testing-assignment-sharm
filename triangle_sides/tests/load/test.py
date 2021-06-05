import time
import requests
import random

from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)
    
    @task
    def get_sides(self):
        self.client.post("/check-sides", json={'sides': 
            [random.randint(1,10000),random.randint(1,10000),random.randint(1,10000)]})
        self.client.get("/get-sides")