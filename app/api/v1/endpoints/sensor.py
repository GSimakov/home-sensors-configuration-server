from uuid import UUID

from fastapi import APIRouter, status, Depends, Query, Body, File, Response, UploadFile
from fastapi_pagination import Params
from six import BytesIO
from sqlmodel import and_, select, col, or_, text
from typing import Annotated

from app import schemas
from app import models
from app import crud

from app.schemas.response_schema import (
    IPostResponseBase,
    create_response,
    IGetResponsePaginated,
    IGetResponseBase,
    IDeleteResponseBase,
    IPutResponseBase
)

router = APIRouter()


@router.get("/list")
async def read_sensors_list(
        params: Params = Depends(),
) -> IGetResponsePaginated[schemas.ISensorRead]:
    """
    Gets a paginated list of sensors
    """
    response = await crud.sensor.get_multi_paginated(params=params)
    return create_response(data=response)




# @router.get("/list/by_role_name")
# async def read_users_list_by_role_name(
#         user_status: Annotated[
#             IUserStatus,
#             Query(
#                 title="User status",
#                 description="User status, It is optional. Default is active",
#             ),
#         ] = IUserStatus.active,
#         role_name: str = "",
#         params: Params = Depends(),
#         current_user: User = Depends(
#             deps.get_current_user(required_roles=[IRoleEnum.admin])
#         ),
# ) -> IGetResponsePaginated[IUserReadWithoutGroups]:
#     """
#     Retrieve users by role name and status.
#     Required roles:
#     - admin
#     """
#     user_status = True if user_status == IUserStatus.active else False
#     query = (
#         select(User)
#         .where(
#             and_(
#                 User.role_id == (
#                     select(Role.id).where(Role.name == role_name)
#                 ).scalar_subquery(),
#                 User.is_active == user_status
#             )
#         ).order_by(User.first_name)
#     )
#     users = await crud.user.get_multi_paginated(query=query, params=params)
#     return create_response(data=users)
#
#
# @router.get("/order_by_created_at")
# async def get_user_list_order_by_created_at(
#         params: Params = Depends(),
#         current_user: User = Depends(
#             deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
#         ),
# ) -> IGetResponsePaginated[IUserReadWithoutGroups]:
#     """
#     Gets a paginated list of users ordered by created datetime
#     Required roles:
#     - admin
#     - manager
#     """
#     users = await crud.user.get_multi_paginated_ordered(
#         params=params, order_by="created_at"
#     )
#     return create_response(data=users)
#
#
# @router.get("/{user_id}")
# async def get_user_by_id(
#         user: User = Depends(user_deps.is_valid_user),
#         current_user: User = Depends(
#             deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
#         ),
# ) -> IGetResponseBase[IUserRead]:
#     """
#     Gets a user by his/her id
#     Required roles:
#     - admin
#     - manager
#     """
#     return create_response(data=user)
#
#
# @router.get("")
# async def get_my_data(
#         current_user: User = Depends(deps.get_current_user()),
# ) -> IGetResponseBase[IUserReadWithGroups]:
#     """
#     Gets my user profile information
#     """
#     return create_response(data=current_user)
#
# @router.put("")
# async def update_my_data(
#         user: IUserUpdateForRoleUser,
#         current_user: User = Depends(deps.get_current_user()),
# ) -> IPutResponseBase[IUserReadWithGroups]:
#     """
#     Updates current user profile information
#     """
#     user_updated = await crud.user.update(obj_current=current_user, obj_new=user)
#     return create_response(data=user_updated)
#
# @router.put("/{user_id}")
# async def update_user_by_id(
#         user: IUserUpdate,
#         alterable_user: User = Depends(user_deps.is_valid_user),
#         current_user: User = Depends(
#             deps.get_current_user(required_roles=[IRoleEnum.admin, IRoleEnum.manager])
#         ),
# ) -> IPutResponseBase[IUserRead]:
#     """
#     Updates a user by his/her id
#     Required roles:
#     - admin
#     - manager
#     """
#     user_updated = await crud.user.update(obj_current=alterable_user, obj_new=user)
#     return create_response(data=user_updated)
#
# @router.post("", status_code=status.HTTP_201_CREATED)
# async def create_user(
#         new_user: IUserCreate = Depends(user_deps.user_exists),
#         current_user: User = Depends(
#             deps.get_current_user(required_roles=[IRoleEnum.admin])
#         ),
# ) -> IPostResponseBase[IUserReadWithGroups]:
#     """
#     Creates a new user
#     Required roles:
#     - admin
#     """
#     user = await crud.user.create_with_role(obj_in=new_user)
#
#     if new_user.groups_ids:
#         for group_id in new_user.groups_ids:
#             await crud.group.add_user_to_group(user=user, group_id=group_id)
#
#     return create_response(data=user)
#
# @router.delete("/{user_id}")
# async def remove_user(
#         user_id: UUID = Depends(user_deps.is_valid_user_id),
#         current_user: User = Depends(
#             deps.get_current_user(required_roles=[IRoleEnum.admin])
#         ),
# ) -> IDeleteResponseBase[IUserRead]:
#     """
#     Deletes a user by his/her id
#     Required roles:
#     - admin
#     """
#     if current_user.id == user_id:
#         raise UserSelfDeleteException()
#
#     user = await crud.user.remove(id=user_id)
#     return create_response(data=user, message="User removed")
#
#
# @router.post("/image")
# async def upload_my_image(
#         title: str | None = Body(None),
#         description: str | None = Body(None),
#         image_file: UploadFile = File(...),
#         current_user: User = Depends(deps.get_current_user()),
#         minio_client: MinioClient = Depends(deps.minio_auth),
# ) -> IPostResponseBase[IUserRead]:
#     """
#     Uploads a user image
#     """
#     try:
#         image_modified = modify_image(BytesIO(image_file.file.read()))
#         data_file = minio_client.put_object(
#             file_name=image_file.filename,
#             file_data=BytesIO(image_modified.file_data),
#             content_type=image_file.content_type,
#         )
#         media = IMediaCreate(
#             title=title, description=description, path=data_file.file_name
#         )
#         user = await crud.user.update_photo(
#             user=current_user,
#             image=media,
#             heigth=image_modified.height,
#             width=image_modified.width,
#             file_format=image_modified.file_format,
#         )
#         return create_response(data=user)
#     except Exception as e:
#         print(e)
#         return Response("Internal server error", status_code=500)
#
#
# @router.post("/{user_id}/image")
# async def upload_user_image(
#         user: User = Depends(user_deps.is_valid_user),
#         title: str | None = Body(None),
#         description: str | None = Body(None),
#         image_file: UploadFile = File(...),
#         current_user: User = Depends(
#             deps.get_current_user(required_roles=[IRoleEnum.admin])
#         ),
#         minio_client: MinioClient = Depends(deps.minio_auth),
# ) -> IPostResponseBase[IUserRead]:
#     """
#     Uploads a user image by his/her id
#     Required roles:
#     - admin
#     """
#     try:
#         image_modified = modify_image(BytesIO(image_file.file.read()))
#         data_file = minio_client.put_object(
#             file_name=image_file.filename,
#             file_data=BytesIO(image_modified.file_data),
#             content_type=image_file.content_type,
#         )
#         media = IMediaCreate(
#             title=title, description=description, path=data_file.file_name
#         )
#         user = await crud.user.update_photo(
#             user=user,
#             image=media,
#             heigth=image_modified.height,
#             width=image_modified.width,
#             file_format=image_modified.file_format,
#         )
#         return create_response(data=user)
#     except Exception as e:
#         print(e)
#         return Response("Internal server error", status_code=500)
