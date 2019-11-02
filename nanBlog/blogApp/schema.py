import graphene

from graphene import relay, ObjectType, Connection, Node, Int
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django_filters import FilterSet, OrderingFilter
from django.contrib.auth.models import User
from comptesApp.schema import UserType

from .models import *

# Graphene will automatically map the Article model's fields onto the ArticleNode.
# This is configured in the ArticleNode's Meta class (as you can see below)
class ExtendedConnection(Connection):
    class Meta:
        abstract = True

    total_count = Int()
    edge_count = Int()

    def resolve_total_count(root, info, **kwargs):
        return root.length
    def resolve_edge_count(root, info, **kwargs):
        return len(root.edges)



class CategorieNode(DjangoObjectType):
    class Meta:
        model = Categorie
        filter_fields = ['titre', 'articles']
   
      
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection

class TagNode(DjangoObjectType):
    class Meta:
        model = Tag
        # Allow for some more advanced filtering here
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'tag_article__titre':['exact','icontains', 'istartswith'],
            
        }
        interfaces = (relay.Node, )


class ArticleNode(DjangoObjectType):
    class Meta:
        model = Article
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
            'titre_slug': ['exact', 'icontains', 'istartswith'],
            'commentaires':['exact'],
            'categorie_id': ['exact',],
            'categorie_id__titre': ['exact'],
        }
        order_by = OrderingFilter(
            fields=(
                ('date_add','date_add'),
                ('vues','vues'),
            )
        )
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection






class CommentaireNode(DjangoObjectType):
    class Meta:
        model = Commentaire
        # Allow for some more advanced filtering here
        filter_fields = {
            'contenu': ['exact', 'icontains', 'istartswith'],
            'article_id':['exact',],
            'username':['exact',],
          
        }
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection


class ReplyNode(DjangoObjectType):
    class Meta:
        model = Reply
        # Allow for some more advanced filtering here
        filter_fields = {
            'contenu': ['exact', 'icontains', 'istartswith'],
            'commentaire_id':['exact',],
            'username':['exact',],
          
        }
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection

class LikeNode(DjangoObjectType):
    class Meta:
        model = Like
        filter_fields = ['date_add',]
        interfaces = (relay.Node, )
        connection_class = ExtendedConnection




# ...code
# Change the CreateLink mutation
class CreateC(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()
    posted_by = graphene.Field(UserType)

    class Arguments:
        url = graphene.String()
        description = graphene.String()

    def mutate(self, info, url, description):
        user = info.context.user or None

        link = Link(
            url=url,
            description=description,
            posted_by=user,
        )
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
            posted_by=link.posted_by,
        )

class Query(ObjectType):
    Categorie = relay.Node.Field(CategorieNode)
    all_Categories = DjangoFilterConnectionField(CategorieNode)
    
    Tag = relay.Node.Field(TagNode)
    all_Tags = DjangoFilterConnectionField(TagNode)

    Article = relay.Node.Field(ArticleNode)
    all_Articles = DjangoFilterConnectionField(ArticleNode)

    Commentaire = relay.Node.Field(CommentaireNode)
    all_Commentaires = DjangoFilterConnectionField(CommentaireNode)


    Like = relay.Node.Field(LikeNode)
    all_Likes = DjangoFilterConnectionField(LikeNode)
    
    Reply = relay.Node.Field(ReplyNode)
    all_Reply = DjangoFilterConnectionField(ReplyNode)