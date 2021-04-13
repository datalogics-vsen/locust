from locust import HttpUser, TaskSet, task, between, SequentialTaskSet
class MyUser(HttpUser):
    wait_time = between(1, 10)
	
#class GetURLFromPost(SequentialTaskSet):
    request_list = []
	
    @task
    def postJPG2PDF(self):
       with open('DEFAULT-L.pdf', 'rb') as image:
         response = self.client.post(
                         "/jpg/",
		                data={'filename' : 'DEFAULT-L.pdf','output' : 'myPDF2JPG-L.zip','pages' : '1-3'},
		                files={'file' : image}
                    )
       print(" POST  status code: ", response.status_code)
       print(" POST  response   : ", response.text)						 

       json_response_dict = response.json()
       output_id = json_response_dict['outputId']
       self.request_list.append(output_id)

       self.client.get("/resource/" + str(self.request_list.pop(0)) + "?format=url")
       print(" GET  status code: ", response.status_code)
       print(" GET  response   : ", response.text)						 
						 
						 
						 
						 
#
# OTHER DOC
#						 
# curl -X GET "https://zapier.datalogics.com/resource/1f8954a3c-a7d3-4b73-af1a-a77e38b928ac?format=url" -H  "accept:   application/json"
 
     
#response body
#{
#  "url": "https://zapier.datalogics.com/resource/1f8954a3c-a7d3-4b73-af1a-a77e38b928ac?format=file"
#}


#GET   /resource​/{id}    Get a resource by ID

#{{Testing-URL}}/resource/1c3bb825c-7a32-4f92-9c31-b9959c84cf8b?format=url


# Raw response via postman
#{"outputUrl":"https://ec2-3-87-153-50.compute-1.amazonaws.com/resource/00553df77-bd70-4bd4-a8e5-bc838cb70424?format=file","outputId":"00553df77-bd70-4bd4-a8e5-bc838cb70424","inputId":"14e106631-b33d-45c7-9331-ebc934ff5399"}