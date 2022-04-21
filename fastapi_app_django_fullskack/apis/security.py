from fastapi import Cookie, HTTPException, status

from django.contrib.sessions.models import Session
from django.contrib import auth
from django.utils.crypto import constant_time_compare

# https://docs.djangoproject.com/ja/2.2/_modules/django/contrib/auth/

def get_user(sessionid):
    try:
        logined = Session.objects.get(session_key=sessionid).get_decoded()
        user_id = logined['_auth_user_id']
        backend_path = logined['_auth_user_backend']
        backend = auth.load_backend(backend_path)
        user = backend.get_user(user_id)

        # Verify the session
        if hasattr(user, 'get_session_auth_hash'):
            session_hash = logined['_auth_user_hash']
            session_hash_verified = session_hash and constant_time_compare(
                session_hash,
                user.get_session_auth_hash()
            )
            if not session_hash_verified:
                return None

        return {
            # date_joined: "2022-04-01T10:04:33.202141+00:00"
            "email": user.email,
            "first_name": user.first_name,
            "id": user.id,
            "is_active": user.is_active,
            "is_staff": user.is_staff,
            "is_superuser": user.is_superuser,
            "last_name": user.last_name,
            "username": user.username,
        }
    except Exception as e:
        return None

def get_current_user(sessionid: str = Cookie(None)):
    if not sessionid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not logged in"
        )
    user = get_user(sessionid)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authentication"
        )
    return user
