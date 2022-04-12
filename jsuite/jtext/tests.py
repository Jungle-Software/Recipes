from django.test import TestCase


class TestUrls(TestCase):
    app_url = "/text/"  # This is the path to the urls in this app (same as jsuite.urls with leading '/')

    def test_jtext_index_url(self):
        url = self.app_url + ''  # This is the relative url in this app (same as jtext.urls)
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
