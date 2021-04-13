from locust import HttpUser, TaskSet, task, constant
from TestFiles import *

class UserBehaviour(TaskSet):
    testfile = "NOT_FOUND"

    def on_start(self):
       if len(TEST_FILES) > 0:
         self.file = TEST_FILES.pop()
         print(">>>>>>  " + self.file)

    @task
    def one_task(self):
       with open(self.file, 'rb') as image:
         response = self.client.post("/jpg/",
		                data={'filename' : self.file,'output' : 'myOUTPUT-L.zip','pages' : '1-3'},
		                files={'file' : image}
                    )
       print ("running POST api with " + self.file)
       print('Response status code -: ', response.status_code)
       print('Response content     -: ', response.content)


class User(HttpUser):
    tasks = {UserBehaviour:2}
    wait_time = constant(9)
	
