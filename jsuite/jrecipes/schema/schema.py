import graphene

from jrecipes.schema.queries import Query
from jrecipes.schema.mutations import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
