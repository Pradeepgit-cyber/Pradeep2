from locust import HttpUser, between, task


class practice(HttpUser):
    wait_time = between(1, 5)
    host = "https://jsonplaceholder.typicode.com/"
    #
    # @task
    # def prad(self):
    #     url="https://jsonplaceholder.typicode.com/posts"
    #     with self.client.get(url) as response:
    #         print(response.text)


    @task
    def prad2(self):
        request_body={"title": 'Pradeep',
    "body": 'sexy',
    "userId": 1}
        url="https://jsonplaceholder.typicode.com/posts"
        with self.client.post(url,json=request_body) as response:
            if response.status_code in [400,401]:
                print(response.text)
            else:
                print("Api chal gayi")
                print(response.status_code)
