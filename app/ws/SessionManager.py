from typing import List
from app.ws.schemas import Session


class SessionManager:
    def __init__(self):
        self.sessions: List[Session] = []

    def __is_session_exists(self, session_id: str) -> bool:
        for session in self.sessions:
            if session.id == session_id:
                return True

        return False

    def __add_session(self, session_id: str, user_id: str):
        self.sessions.append(Session(
                id=session_id,
                users=[user_id]
            )
        )

    def __get_session_by_id(self, session_id: str):
        for session in self.sessions:
            if session.id == session_id:
                return session

    def __add_user(self, session_id: str, user_id: str):
        session = self.__get_session_by_id(session_id)

        if user_id not in session.users:
            session.users.append(user_id)

    def connect_user(self, session_id: str, user_id: str):
        if not self.sessions:
            self.__add_session(session_id, user_id)

        if not self.__is_session_exists(session_id):
            self.__add_session(session_id, user_id)

        self.__add_user(session_id, user_id)

    def get_session_users(self, session_id: str):
        return self.__get_session_by_id(session_id).users

    def remove_user(self, session_id: str, user_id: str):
        session = self.__get_session_by_id(session_id)
        session.users.remove(user_id)