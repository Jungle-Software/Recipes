import graphene

from jtext.schema.queries import Query
from jtext.schema.mutations import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
