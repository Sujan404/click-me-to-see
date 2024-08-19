
import graphene
import graphql_jwt
from blog import models, types
from graphene_file_upload.scalars import Upload

import logging


logger = logging.getLogger("mylog")

  
class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(types.UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)
      
# Mutation sends data to the database
class CreateUser(graphene.Mutation):
    user = graphene.Field(types.UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        """Do some work"""
        user = models.User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)
 
logger = logging.getLogger("updateUserProfile")
 # working on updating user info
class UpdateUserProfile(graphene.Mutation):
     logger.info("lasdjfkldf")
     user = graphene.Field(types.UserType)
     
     class Arguments:
         user_id = graphene.ID(required = True)
         first_name = graphene.String(required=False)
         last_name = graphene.String(required=False)
         avatar = Upload(required=False, description="Avatar of the user")
         bio = graphene.String(required=False)
         location = graphene.String(required=False)
         website = graphene.String(required=False)
         logger.info(user_id)
         
     def mutate(self, info, user_id, first_name='', last_name='', avatar='', bio='', location='', website=''):
        user = models.User.objects.get(pk=user_id)
        logger.info(avatar)
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if avatar:
            user.avatar.save("avatar user", avatar, save=True)
        if bio:
            user.bio = bio
        if location:
            user.location = location
        if website:
            user.website = website
        
        user.save()
        logger.info("abcdef")
        
        return UpdateUserProfile(user=user)   
     
    #comment create
class CreateComment(graphene.Mutation):
    comment = graphene.Field(types.CommentType)
    class Arguments:
        content = graphene.String(required=True)
        user_id = graphene.ID(required=True)
        post_id = graphene.ID(required=True)

    def mutate(self, info, content, user_id, post_id):
        comment = models.Comment(
            content=content,
            user_id=user_id,
            post_id=post_id,
        )
        comment.save()

        return CreateComment(comment=comment)
     
class Mutation(graphene.ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    
    create_user = CreateUser.Field()
    update_user_profile = UpdateUserProfile.Field()
    create_comment = CreateComment.Field()