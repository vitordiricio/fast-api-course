from sqlalchemy import select

from fast_api_course.models import User


def test_create_user(session):
    new_user = User(
        username="alice", email="test@example.com", password="secret"
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    result = session.scalar(select(User).where(User.username == "alice"))

    assert result.username == new_user.username
