import graphene

import jtext.schema.queries
import jtext.schema.mutations
# TODO find a way to optimize schema import methodology, this might become very long for many apps


class SuperQuery(jtext.schema.queries.Query):
    pass


class SuperMutation(jtext.schema.mutations.Mutation):
    pass


schema = graphene.Schema(query=SuperQuery, mutation=SuperMutation)
