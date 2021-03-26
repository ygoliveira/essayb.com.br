from fastapi import APIRouter

from .models.follow import CheckFollowerResponse
from ...modules.v1.follow import check_follower_by_username, check_follower_by_id

router = APIRouter(prefix='/follows', tags=['Follow'])


@router.get('/follower/{username_or_id_user_follower}/{username_or_id_user_following}/check', summary='Check follower by ID or username', status_code=200,
            response_model=CheckFollowerResponse)
def _check_follower_username(username_or_id_user_follower: str, username_or_id_user_following: str):
    if username_or_id_user_follower.isdigit() and username_or_id_user_following.isdigit():
        is_following = check_follower_by_id(int(username_or_id_user_follower), int(username_or_id_user_following))
    else:
        is_following = check_follower_by_username(username_or_id_user_follower, username_or_id_user_following)
    return {'is_following': is_following}
