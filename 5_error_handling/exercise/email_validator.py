
class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

MINIMUM_LENGTH = 5
VALID_DOMAINS = ['com', 'bg', 'org', 'net']

while True:
    email = input()
    if email == 'End':
        break
    if not '@' in email:
        raise MustContainAtSymbolError('Email must contain @')
    if len(email.split('@')[0]) < MINIMUM_LENGTH:
        raise NameTooShortError('Name must be more than 4 characters')
    email_domain = email.split('.')[1]
    if not email_domain in VALID_DOMAINS:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    print('Email is valid')