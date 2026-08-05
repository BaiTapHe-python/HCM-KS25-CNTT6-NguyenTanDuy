from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/library_db"
engine = create_engine(DATABASE_URL)
LocalSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)

Base = declarative_base()

def get_db():
    try:
        db = LocalSession()
        yield db
    finally:
        db.close()