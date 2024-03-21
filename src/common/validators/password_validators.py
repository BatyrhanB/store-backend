import re

from common.exceptions import IncorrectPasswordException

PASSWORD_RE = re.compile(r"[\w.-]{6,}")


def validate_user_password(password: str, conf_password: str) -> str:
    """
    Validate user password
    :args
        password (str): _user's password_
        conf_password (str): _confirm password_
    :raises
        IncorrectPasswordException: _return statusCode about incorrect password_
    :returns
        str: _return password_
    """
    if not PASSWORD_RE.match(password):
        raise IncorrectPasswordException(
            # "Password min lenght is 6, and it must contains A-Z, a-z, 0-9"
            {"message": "Password min lenght is 6, and it must contains A-Z, a-z, 0-9"}
        )
    if password != conf_password:
        raise IncorrectPasswordException(
            {"message": "Password and confirm password must be same"}
        )
    return password
