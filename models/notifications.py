from pydantic import BaseModel


class Message(BaseModel):
    type: str
    channel: str
    user: str
    text: str
    ts: float
    event_ts: float
    thread_ts: float = None
    channel_type: str


class MessageEvent(BaseModel):
    token: str
    team_id: str
    api_app_id: str
    event: Message
    type: str
    event_id: str
    event_time: int

class VerificationChallenge(BaseModel):
    challenge: str = "OK"  # For verification
