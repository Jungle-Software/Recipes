from django.test import TestCase

import graphene

from jsuite.schema import SuperQuery

""" Temp until I figure out how to add tests with the frontend separate.
class TestUrls(TestCase):

    # TODO Add a redirect in landing page so that there is no 404
    def test_jsuite_index_url(self):
        url = ""
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 404)

    # TODO Create graphql queries for every model
    def test_jsuite_graphql_url(self):
        # TODO Create a randomizer for graphql queries
        query = \"\"\" obvi need to remove the backslashes ~
                    query {
                      recipes{
                          id
                          title
                        }
                    }
                \"\"\"
        schema = graphene.Schema(query=SuperQuery)
        result = schema.execute(query)
        self.assertIsNone(result.errors)

"""
