from django.test import TestCase

from jtext.schema import Query
import graphene


class TestUrls(TestCase):

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
