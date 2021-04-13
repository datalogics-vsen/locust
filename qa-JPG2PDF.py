# target http://ec2-52-87-153-50.compute-1.amazoneaws.com
# 4/12 switching to ec2-54-197-179-52.compute-1.amazonaws.com


from locust import HttpUser, TaskSet, task
class UserBehavior(TaskSet):

    @task(1)
    def postJPG2PDF(self):
      with open('D:\\LOCUST-QA\\DEFAULT-L.jpg','rb') as image:
        self.client.post("/pdf",
		                {"file":image,
						 "filename":"DEFAULT-L.jpg",
						 "output":"myJPG2PDF.pdf"})
						 
class WebsiteUser(HttpUser):
    tasks = {UserBehavior}
    min_wait = 1000
    max_wait = 9000