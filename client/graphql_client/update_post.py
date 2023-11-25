# Generated by ariadne-codegen
# Source: ./gql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class UpdatePost(BaseModel):
    update_post: "UpdatePostUpdatePost" = Field(alias="updatePost")


class UpdatePostUpdatePost(BaseModel):
    post: Optional["UpdatePostUpdatePostPost"]
    success: bool
    errors: Optional[List[Optional[str]]]


class UpdatePostUpdatePostPost(BaseModel):
    id: str
    title: str
    description: str


UpdatePost.model_rebuild()
UpdatePostUpdatePost.model_rebuild()
UpdatePostUpdatePostPost.model_rebuild()
