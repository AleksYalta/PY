from sqlalchemy import (
    Table, Column, Integer, String, Boolean
)
from db import metadata

students = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("email", String, nullable=False, unique=True),
    Column("is_deleted", Boolean, default=False)
)
