from fastapi import Body, Depends, FastAPI, Form, Request
from fastapi.responses import PlainTextResponse, Response

from commons import Logger as LOG
from handlers import MessageEventHandler, ThanksActionHandler, ThanksCommandHandler
from models import BlockActiona, MessageEvent, VerificationChallenge

thankified = FastAPI()

@thankified.get("/")
async def home():
    return {"message": "Welcome to Thankified!"}

# Handle all events
@thankified.post("/event")
async def handle_event(event: MessageEvent, messageEventHandler: MessageEventHandler = Depends()):
    LOG.debug("request received: " + event.event.text)
    result =  await messageEventHandler.handle_message(event)
    return PlainTextResponse(content=result, status_code=200)

# User interaction with the bot buttons. menus, etc
@thankified.post("/reaction")
async def handle_forms(payload: str = Form(...), blockActioHandler: ThanksActionHandler = Depends()):
    LOG.debug("request received")
    blockActions = BlockActiona.model_validate_json(payload)
    result = await blockActioHandler.handle_actions(blockActions)
    return PlainTextResponse(content=result, status_code=200)

# Call back to handle /thank-you command - For fitire use
@thankified.post("/slash_command")
async def handle_forms(team_id:str = Form(...), channel_id: str = Form(...), command:str = Form(...), text:str = Form(default=""), commandHandler: ThanksCommandHandler = Depends()):
    LOG.debug("request received")
    result = await commandHandler.handle_command(team_id, channel_id)
    return {
        "response_type": "in_channel" if text.strip().lower() == "publish" and result != "" else "ephemeral",
        # "text": result if result != "" else "No data since last week, please check back later",
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Thankified Report"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": result if result != "" else "No data since last week, please check back later"
                }
            }
        ]
    }
