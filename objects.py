from pydantic import BaseModel

class MailBox(BaseModel):
    token: str
    mailbox: str

class Messages(BaseModel):
    mailbox: str
    messages: list