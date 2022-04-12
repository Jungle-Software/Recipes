from django.test import TestCase

from jtext.schema import Query
import graphene


class TestUrls(TestCase):

    # TODO Add a redirect in landing page so that there is no 404
    def test_jsuite_index_url(self):
        url = ""
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 404)

    def test_jsuite_graphql_url(self):
        # TODO Create a randomizer for graphql queries
        query = """
                    query {
                      recipes{
                          id
                          title
                        }
                    }
                """
        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        self.assertIsNone(result.errors)
