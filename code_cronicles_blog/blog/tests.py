from django.test import TestCase


class TestBlog(TestCase):

    def test_posts(self):
        response = self.client.get('/api/v1/posts/')
        self.assertEqual(response.status_code, 200)

    def test_create_post(self):
        response = self.client.get('/api/v1/post-create/')
        self.assertEqual(response.status_code, 401)

    def test_change_post(self):
        response = self.client.get('/api/v1/post/Databases for C++/')
        self.assertEqual(response.status_code, 404)

    def test_categories(self):
        response = self.client.get('/api/v1/categories/')
        self.assertEqual(response.status_code, 200)

    def test_comment(self):
        response = self.client.get('/api/v1/comment/')
        self.assertEqual(response.status_code, 401)




