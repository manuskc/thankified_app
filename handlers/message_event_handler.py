from models import MessageEvent
from commons import Config
from commons import Logger as LOG
import re
from models import Awards

from slack_sdk.web.async_client import AsyncWebClient
from slack_sdk.models.blocks import ButtonElement , ActionsBlock, Block, MarkdownTextObject, SectionBlock, TextObject

from db import MessageDAO

class MessageEventHandler(object):
    
    USER_ID = '<@U[0-9A-Z]+>'
    
    def __init__(self) -> None:
        pass

    def _response(self, sender: str, thanked_users: list[str], ids: list[int]) -> list[Block]:
        
        message = "Send a virtual gift to " + ','.join(thanked_users) + " for their great work!"
        info = SectionBlock(text=message)
        ids_str = ','.join(str(id) for id in ids)
        
        awards = [Awards.HELPS_ME, Awards.OUR_TEAM, Awards.OUR_USERS, Awards.ABOVE_BEYOND]
        buttons = [ButtonElement(text=f"{award.description} {award.emoji}", value=f"{award.id}|{ids_str}") for award in awards]
        
        dismiss = ButtonElement(text="Dismiss", value=f"{Awards.NONE.id}|0", style="danger")
        buttons.append(dismiss)

        actions = ActionsBlock(elements=buttons)
        
        # rating_form
        return [info, actions]

    async def handle_message(self, message: MessageEvent) -> None:
        sender = message.event.user
        sent_message = message.event.text

        # Check if the message is a thank you message
        words = set(sent_message.lower().split(' '))
        
        thanked_users = []
        for user in re.findall(MessageEventHandler.USER_ID, sent_message):
            if user != '<@' + sender + '>' :
                thanked_users.append(user)

        if 'thank' in words or 'thanks' in words and len(thanked_users) > 0:
            # Create slack client
            slack_token = Config.slack_token
            slack = AsyncWebClient(token=slack_token)

            # Update the database
            ids = MessageDAO.create(message.team_id, thanked_users, '<@' + sender + '>', Awards.NONE.id)
            response = self._response(sender, thanked_users, ids)

            # Send the response
            await slack.chat_postEphemeral(channel=message.event.channel, user=message.event.user, blocks=response)
        # else no-op
        return "OK"