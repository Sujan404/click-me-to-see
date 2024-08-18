
import graphene
import graphql_jwt
from blog import models, types
from graphene_file_upload.scalars import Upload
import logging

logger = logging.getLogger("mylog")

  
class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    logger.debug("hello heoo I am hit from frontend")
    """Hello hello hello hello hello"""
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
 
 # working on updating user info
class UpdateUserProfile(graphene.Mutation):
     user = graphene.Field(types.UserType)
     
     class Arguments:
         user_id = graphene.ID(required = True)
         first_name = graphene.String(required=False)
         last_name = graphene.String(required=False)
         avatar = Upload(required=False)
         bio = graphene.String(required=False)
         location = graphene.String(required=False)
         website = graphene.String(required=False)
         
     def mutate(self, info, user_id, first_name='', last_name='', avatar='', bio='', location='', website=''):
        user = models.User.objects.get(pk=user_id)
        
        user.first_name = first_name
        user.last_name = last_name
        user.avatar = avatar
        user.bio = bio
        user.location = location
        user.website = website
        
        user.save()
        
        return UpdateUserProfile(user=user)    
     
class Mutation(graphene.ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    
    create_user = CreateUser.Field()
    update_user_profile = UpdateUserProfile.Field()