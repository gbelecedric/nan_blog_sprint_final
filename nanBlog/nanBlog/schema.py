import graphene

import blogApp.schema
import comptesApp.schema
import contactApp.schema

class Query(contactApp.schema.Query,blogApp.schema.Query,comptesApp.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(contactApp.schema.Mutation,comptesApp.schema.Mutation, graphene.ObjectType):
        pass

schema = graphene.Schema(query=Query, mutation=Mutation)