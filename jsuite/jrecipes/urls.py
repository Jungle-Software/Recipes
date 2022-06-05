from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

from jrecipes.schema.schema import schema as jrecipes_schema

urlpatterns = [
    # TODO can we find a way to SeCuRElY do this without csrf exempt? Ie, require a user to be authenticated to make requests
    path('recipes', csrf_exempt(GraphQLView.as_view(schema=jrecipes_schema, graphiql=True))),
]
