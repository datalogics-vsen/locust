# target http://ec2-52-87-153-50.compute-1.amazoneaws.com


from locust import HttpUser, TaskSet, task, between
class MyUser(HttpUser):
    wait_time = between(9, 15)
	
    @task
    def postJPG2PDF(self):
       image = open('D:\\LOCUST\\DEFAULT.jpg','rb')
       self.client.post("/pdf",
		                {"file":image,
						 "filename":"DEFAULT.jpg",
						 "output":"myJPG2PDF.pdf"})

    @task
    def postJPG2PDF(self):
#      NOTE: TIF is to large and will fail 
       image = open('D:\\LOCUST\\DEFAULT.tif','rb')
       self.client.post("/pdf",
		                {"file":image,
						 "filename":"DEFAULT.tif",
						 "output":"mytif2pdf.pdf"})

    @task
    def postJPG2PDF(self):
      image = open('D:\\LOCUST\\DEFAULT.bmp','rb')
      self.client.post("/pdf",
		                {"file":image,
						 "filename":"DEFAULT.bmp",
						 "output":"mybmp2pdf.pdf"})
