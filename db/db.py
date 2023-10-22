from sqlalchemy import create_engine
from commons import Config
from sqlalchemy.orm import sessionmaker

Db = create_engine(Config.db_connection, echo=True)
Session = sessionmaker(bind=Db)