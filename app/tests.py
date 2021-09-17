from django.test import SimpleTestCase

class TestHelloView(SimpleTestCase):
    def test_hello_view(self): 
        response = self.client.get("/hello/nate/")
        self.assertContains(response, "Hello nate")

