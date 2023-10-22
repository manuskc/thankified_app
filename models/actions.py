"""
JSON: 
{
  "type": "block_actions",
  "user": {
    "id": "U04SX7G6C",
    "username": "manuskc",
    "name": "manuskc",
    "team_id": "T04SX7G6A"
  },
  "api_app_id": "A05QTBD9QER",
  "token": "ljgdgnq66XGNHHAMRwHBYeQN",
  "container": {
    "type": "message",
    "message_ts": "1694575016.002400",
    "channel_id": "C05JDB0A4UU",
    "is_ephemeral": true
  },
  "trigger_id": "5900190966369.4915254214.024e6fd48e45a2722768c77918d74679",
  "team": {
    "id": "T04SX7G6A",
    "domain": "codiots"
  },
  "enterprise": null,
  "is_enterprise_install": false,
  "channel": {
    "id": "C05JDB0A4UU",
    "name": "eva-dev-public"
  },
  "state": {
    "values": {}
  },
  "response_url": "https://hooks.slack.com/actions/T04SX7G6A/5884632347733/kyNlTGDGITdskpywIXcuFFJo",
  "actions": [
    {
      "action_id": "acZn8",
      "block_id": "QPDL",
      "text": {
        "type": "plain_text",
        "text": "Helped Me :tada:",
        "emoji": true
      },
      "value": "10",
      "type": "button",
      "action_ts": "1694578211.304396"
    }
  ]
}
"""

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: str
    username: str
    name: str
    team_id: str

class Container(BaseModel):
    type: str
    message_ts: str
    channel_id: str
    is_ephemeral: bool

class Team(BaseModel):
    id: str
    domain: str

class Channel(BaseModel):
    id: str
    name: str

class State(BaseModel):
    values: dict

class ActionText(BaseModel):
    type: str
    text: str
    emoji: bool

class Action(BaseModel):
    action_id: str
    block_id: str
    text: ActionText
    value: str
    type: str
    action_ts: str

class BlockActiona(BaseModel):
    type: str
    user: User
    api_app_id: str
    token: str
    container: Container
    trigger_id: str
    team: Team
    enterprise: Optional[str] = None
    is_enterprise_install: bool
    channel: Channel
    state: State
    response_url: str
    actions: list[Action]