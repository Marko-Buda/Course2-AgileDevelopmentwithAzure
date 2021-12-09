import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
#    wait_time = between(0.5, 1)
nameInquiry = json.loads("""{
   "CHAS":{
      "0":0
   },
   "RM":{
      "0":6.575
   },
   "TAX":{
      "0":296.0
   },
   "PTRATIO":{
      "0":15.3
   },
   "B":{
      "0":396.9
   },
   "LSTAT":{
      "0":4.98
   }
}""")

    @task
    def test_load_of_webapp(self):
        self.client.get("https://project2-ci-and-cd.azurewebsites.net/")

    @task(1)
    def users(self):
        self.client.post("/posts", data=nameInquiry, headers=myheaders)

#    @task(3)
#    def view_item(self):
#        for item_id in range(10):
#            self.client.get(f"/item?id={item_id}", name="/item")
#            time.sleep(1)

#    def on_start(self):
#        self.client.post("/login", json={"username": "foo", "password": "bar"})
