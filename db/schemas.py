from sqlalchemy import Integer, String, DateTime, Boolean, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from .db import Db


class Base(DeclarativeBase):
    pass

class MessageTable(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement= True)
    team: Mapped[str] = mapped_column(String)
    user: Mapped[str] = mapped_column(String, index=True)
    sender: Mapped[str] = mapped_column(String, index=True)
    award: Mapped[String] = mapped_column(String, index=True)
    created_at: Mapped[int] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[int] = mapped_column(DateTime, server_default=func.now())

    def __repr__(self):
        return "<Message(id='%s', team='%s', user='%s', sender='%s', message='%s', score='%s', created_at='%s', updated_at='%s')>" % (
            self.id, self.team, self.user, self.sender, self.message, self.score, self.created_at, self.updated_at)

# Emit the DDL to the database to create all tables above
Base.metadata.create_all(Db)
