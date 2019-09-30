''' user authentication validator '''
import re
from ..utils.messages import error_messages

def validate_name(name):
    ''' validate user name input '''
    name_signature = re.compile('[a-zA-Z]')
    length = len(name)

    if name_signature.match(name) is None:
        return [False, error_messages['invalid-name']]

    if length > 50:
        return [False, error_messages['invalid-length']]

    return [True, '']

def validate_password(password, confirm_password):
    ''' validate user password input '''
    length = len(password)

    if length < 8:
        return [False, error_messages['invalid-password']]

    if password != confirm_password:
        return [False, error_messages['password-mismatch']]

    return [True, '']

def validate_email(email):
    ''' validate user password input '''
    email_signature = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

    if email_signature.match(email) is None:
        return [False, error_messages['invalid-email']]

    return [True, '']
