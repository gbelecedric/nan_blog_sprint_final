from django.contrib.auth import get_user_model
from .models import *
import graphene
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        name = graphene.String(required=True)

    def mutate(self, info, username, password, email, name):
        user = get_user_model()(
            username=username,
            email=email,
            name=name,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)

class CreateProfile(graphene.Mutation):
    profile = graphene.Field(Profile)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        image = Upload(required=True)


    def mutate(self, info, username, password, email,image ):
        profile = Profile(
            user=username,
            email=email,
            image = image
        )
        profil.set_password(password)
        Profil.save()

        return CreateProfile(profil=profil)

class Mutation(graphene.ObjectType):
    create_profile = CreateProfile.Field()

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    
class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    
class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    
class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return get_user_model().objects.all()