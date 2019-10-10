''' validate service entry '''
import re
from ..utils.messages import invalid_id

def validate_id(service_id):
    ''' validate service id input '''
    id_signature = re.compile('[0-9]')

    if id_signature.match(service_id) is None:
        return [False, invalid_id]

    return [True, '']
