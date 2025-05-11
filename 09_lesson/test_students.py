import pytest
from sqlalchemy import create_engine, Table, MetaData, insert, update, select
from sqlalchemy.orm import sessionmaker
from uuid import uuid4

DATABASE_URL = "postgresql://postgres:123456789@localhost:5432/QA"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
metadata = MetaData()
students = Table("students", metadata, autoload_with=engine)


@pytest.fixture
def db_session():
    session = Session()
    yield session
    session.rollback()
    session.close()


def generate_email(base):
    return f"{base}_{uuid4().hex[:8]}@example.com"


def test_create_student(db_session):
    email = generate_email("ivan")
    stmt = insert(students).values(name="Иван Иванов", email=email)
    result = db_session.execute(stmt)
    db_session.commit()

    student_id = result.inserted_primary_key[0]
    query = select(students).where(students.c.id == student_id)
    student = db_session.execute(query).fetchone()

    assert student is not None
    assert student.name == "Иван Иванов"


def test_update_student(db_session):
    email = generate_email("maria")
    stmt = insert(students).values(
        name="Мария Смирнова", email=email)
    result = db_session.execute(stmt)
    student_id = result.inserted_primary_key[0]

    upd = update(students).where(students.c.id == student_id).values(
        name="Мария Иванова")
    db_session.execute(upd)
    db_session.commit()

    query = select(students).where(students.c.id == student_id)
    updated = db_session.execute(query).fetchone()

    assert updated.name == "Мария Иванова"


def test_soft_delete_student(db_session):
    email = generate_email("alex")
    stmt = (insert(students).values(
        name="Алексей Кузнецов", email=email))
    result = db_session.execute(stmt)
    student_id = result.inserted_primary_key[0]

    soft_del = update(students).where(
        students.c.id == student_id
    ).values(is_deleted=True)

    db_session.execute(soft_del)
    db_session.commit()

    query = select(students).where(students.c.id == student_id)
    student = db_session.execute(query).fetchone()

    assert student.is_deleted is True
