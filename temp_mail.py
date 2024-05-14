from requests import Session

from .objects import *

class TempMail:
    _url = 'https://web2.temp-mail.org/{}'.format
    _headers = {
        "user-agent": "Mozilla/5.0 (Linux; U; Linux x86_64; en-US) AppleWebKit/600.8 (KHTML, like Gecko) Chrome/47.0.1452.400 Safari/536",
        "x-requested-with": "XMLHttpRequest"
    }

    @classmethod
    def __method_request(cls, method: str, url: str, data: dict = None):
        session = Session()

        if method == 'get': req = session.get(url = url, headers = cls._headers)
        else: req = session.post(url = url, data = data, headers = cls._headers)

        return req if req.status_code == 200 else print(f'Error : {req.json()["errorMessage"]}'), exit()

    @classmethod
    def mailbox(cls) -> MailBox:
        req = MailBox(**cls.__method_request(method = 'post', url = cls._url('mailbox')).json())
        cls._headers['Authorization'] = f'Bearer {req.token}'
        return req

    @classmethod
    def messages(cls) -> Messages:
        return Messages(**cls.__method_request(method = 'get', url = cls._url('messages')).json())