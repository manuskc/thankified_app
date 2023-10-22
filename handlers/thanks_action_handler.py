from slack_sdk.webhook.async_client import AsyncWebhookClient
from models import BlockActiona
from commons import Logger as LOG
from models import Awards

from db import MessageDAO

class ThanksActionHandler(object):
    def __init__(self) -> None:
        pass

    async def handle_actions(self, payload: BlockActiona) -> None:
        response_parts = payload.actions[0].value.split('|')
        award = response_parts[0]
        ids = [int(id) for id in response_parts[1].split(',')]

        if (award != Awards.NONE.id):
            MessageDAO.update(ids, award)
        slack = AsyncWebhookClient(payload.response_url)
        await slack.send_dict({
            "delete_original": "true"
        })
        return "OK"