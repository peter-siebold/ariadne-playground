# Generated by ariadne-codegen
# Source: ./gql/queries.graphql

from typing import Any, Dict

from .all_posts import AllPosts
from .async_base_client import AsyncBaseClient
from .create_new_post import CreateNewPost
from .delete_post import DeletePost
from .get_post import GetPost
from .update_post import UpdatePost


def gql(q: str) -> str:
    return q


class Client(AsyncBaseClient):
    async def all_posts(self, **kwargs: Any) -> AllPosts:
        query = gql(
            """
            query AllPosts {
              listPosts {
                success
                errors
                post {
                  id
                  title
                  description
                  created_at
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(query=query, variables=variables, **kwargs)
        data = self.get_data(response)
        return AllPosts.model_validate(data)

    async def get_post(self, id: str, **kwargs: Any) -> GetPost:
        query = gql(
            """
            query GetPost($id: ID!) {
              getPost(id: $id) {
                post {
                  id
                  title
                  description
                }
                success
                errors
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id}
        response = await self.execute(query=query, variables=variables, **kwargs)
        data = self.get_data(response)
        return GetPost.model_validate(data)

    async def create_new_post(
        self, title: str, description: str, **kwargs: Any
    ) -> CreateNewPost:
        query = gql(
            """
            mutation CreateNewPost($title: String!, $description: String!) {
              createPost(title: $title, description: $description) {
                post {
                  id
                  title
                  description
                  created_at
                }
                success
                errors
              }
            }
            """
        )
        variables: Dict[str, object] = {"title": title, "description": description}
        response = await self.execute(query=query, variables=variables, **kwargs)
        data = self.get_data(response)
        return CreateNewPost.model_validate(data)

    async def update_post(
        self, id: str, title: str, description: str, **kwargs: Any
    ) -> UpdatePost:
        query = gql(
            """
            mutation UpdatePost($id: ID!, $title: String!, $description: String!) {
              updatePost(id: $id, title: $title, description: $description) {
                post {
                  id
                  title
                  description
                }
                success
                errors
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "id": id,
            "title": title,
            "description": description,
        }
        response = await self.execute(query=query, variables=variables, **kwargs)
        data = self.get_data(response)
        return UpdatePost.model_validate(data)

    async def delete_post(self, id: str, **kwargs: Any) -> DeletePost:
        query = gql(
            """
            mutation DeletePost($id: ID!) {
              deletePost(id: $id) {
                success
                errors
                post {
                  id
                  title
                  description
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id}
        response = await self.execute(query=query, variables=variables, **kwargs)
        data = self.get_data(response)
        return DeletePost.model_validate(data)
