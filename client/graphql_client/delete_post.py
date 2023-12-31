# Generated by ariadne-codegen
# Source: ./gql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class DeletePost(BaseModel):
    delete_post: "DeletePostDeletePost" = Field(alias="deletePost")


class DeletePostDeletePost(BaseModel):
    success: bool
    errors: Optional[List[Optional[str]]]
    post: Optional["DeletePostDeletePostPost"]


class DeletePostDeletePostPost(BaseModel):
    id: str
    title: str
    description: str


DeletePost.model_rebuild()
DeletePostDeletePost.model_rebuild()
DeletePostDeletePostPost.model_rebuild()
