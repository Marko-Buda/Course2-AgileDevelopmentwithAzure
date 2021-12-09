import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(0.5, 1)

    @task
    def test_load_of_webapp(self):
        self.client.get("https://project2-ci-and-cd.azurewebsites.net/")

#    @task(3)
#    def view_item(self):
#        for item_id in range(10):
#            self.client.get(f"/item?id={item_id}", name="/item")
#            time.sleep(1)

#    def on_start(self):
#        self.client.post("/login", json={"username": "foo", "password": "bar"})
