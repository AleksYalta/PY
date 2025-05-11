from sqlalchemy import create_engine
from models import Base

DATABASE_URL = "postgresql://postgres:123456789@localhost:5432/QA"
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)
