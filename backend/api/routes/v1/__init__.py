from fastapi import APIRouter

from . import authentication, follow, user

router = APIRouter(prefix='/v1')

router.include_router(authentication.router)
router.include_router(user.router)
router.include_router(follow.router)
