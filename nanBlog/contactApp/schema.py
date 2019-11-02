import graphene

from graphene_django.types import DjangoObjectType

from .models import *
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay, ObjectType

class NewsletterNode(DjangoObjectType):
    class Meta:
        model = Newsletter
        filter_fields = ['email']
        interfaces = (relay.Node, )
        
class CreateNewsletter(graphene.Mutation):
       
    email= graphene.String()
   

    
    class Arguments:
   
        email = graphene.String()

    
    def mutate(self, info, email):
        
        newsletter = Newsletter(email=email)
        newsletter.save()

        return CreateNewsletter(
        
            email = Newsletter(email=email)
        )


class  MessageNode(DjangoObjectType):
    class Meta:
        model =  Message
        filter_fields = ['nom','message']
        interfaces = (relay.Node, )
        
class CreateMessage(graphene.Mutation):
       
    nom= graphene.String()
    message= graphene.String()
   

    
    class Arguments:
   
        nom = graphene.String()
        message= graphene.String()

    
    def mutate(self, info, email):
        
        
        message =  Message(nom=nom,message=message,)
        message.save()

        return CreateMessage(
        
            email =  Message(email=email)
        )


class Query(graphene.ObjectType):
    newsletter = relay.Node.Field(NewsletterNode)
    all_newsletter = DjangoFilterConnectionField(NewsletterNode)
    message = relay.Node.Field(MessageNode)
    all_message = DjangoFilterConnectionField(MessageNode)

class Mutation(graphene.ObjectType):
    create_CreateNewsletter = CreateNewsletter.Field()
    create_CreateMessage = CreateMessage.Field()