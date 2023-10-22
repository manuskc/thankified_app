from sqlalchemy import select, update, func, and_
from .db import Session
from .schemas import MessageTable
from commons import Logger as LOG
from datetime import timedelta, datetime

class MessageDAO(object):
    def create(team: str, users: list[str], sender: str, award: str):
        results = []
        with Session() as session, session.begin():
            messages = [MessageTable(team=team, user=user, sender=sender, award=award) for user in users]
            session.add_all(messages)
            session.flush()
            results = [message.id for message in messages]
        return results
    
    def update(ids: list[int], award: str):
        with Session() as session, session.begin():
            query = update(MessageTable).where(MessageTable.id.in_(ids)).values(award=award, updated_at=func.now())
            session.execute(query)

    def getScores(team: str, users: list[str]):
        ago =  (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')
        with Session() as session, session.begin():
            query = select(MessageTable.user, MessageTable.award, func.count().label('total')).where(and_(MessageTable.team == team, MessageTable.user.in_(users), MessageTable.updated_at > ago)).group_by(MessageTable.user, MessageTable.award).order_by(MessageTable.user)
            return session.execute(query)