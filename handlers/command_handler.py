from typing import Optional
from commons import Config, Logger as LOG
from slack_sdk.web.async_client import AsyncWebClient
from slack_sdk.models.blocks import PlainTextObject

from db import MessageDAO
from models import Awards

class ThanksCommandHandler(object):
    def __init__(self) -> None:
        pass

    
    async def handle_command(self, team: str, channel: str) -> str:
        slack_token = InstallationInfoDAO.get(team)
        slack = AsyncWebClient(token=slack_token)
        result = await slack.conversations_members(channel=channel)
        output = ""
        if result['ok']:
            users = [ '<@' + user + '>' for user in result['members']]
            scores = MessageDAO.getScores(team, users)
            score_map = {}
            for score in scores:
                user_map = score_map[score.user] if score.user in score_map else {}
                user_map[score.award] = score.total
                score_map[score.user] = user_map
            
            response = ""
            for user in score_map:
                user_map = score_map[user] if user in score_map else {}
                response += f"{Awards.NONE.emoji}` {user_map.get(Awards.NONE.id, 0):<4} `"
                response += f"{Awards.HELPS_ME.emoji}` {user_map.get(Awards.HELPS_ME.id, 0):<4} `"
                response += f"{Awards.OUR_TEAM.emoji}` {user_map.get(Awards.OUR_TEAM.id, 0):<4} `"
                response += f"{Awards.OUR_USERS.emoji}` {user_map.get(Awards.OUR_USERS.id, 0):<4} `"
                response += f"{Awards.ABOVE_BEYOND.emoji}` {user_map.get(Awards.ABOVE_BEYOND.id, 0):<4} `"
                response += user + "\n"

            if response != "":
                output = response
            
        # else no action
        return output
        