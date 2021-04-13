from locust import HttpUser, TaskSet, task, between, SequentialTaskSet
class MyUser(HttpUser):
    wait_time = between(1, 10)
	
    @task
    def postJPG2PDF(self):
       with open('DEFAULT-L.pdf', 'rb') as image:
         response = self.client.post("/jpg/",
		                data={'filename' : 'DEFAULT-L.pdf','output' : 'myPDF2JPG-L.zip','pages':'1-3'},
		                files={'file' : image}
                    )
       print(" PDF  text: ", response.text)						 