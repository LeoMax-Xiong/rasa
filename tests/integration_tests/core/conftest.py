import os
from typing import Iterator, Text

import pytest
import sqlalchemy as sa

from rasa.core.lock_store import RedisLockStore
from rasa.core.tracker_store import RedisTrackerStore
from rasa.shared.core.domain import Domain

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)
POSTGRES_USER = os.getenv("POSTGRES_USER", "")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")
POSTGRES_DEFAULT_DB = os.getenv("POSTGRES_DEFAULT_DB", "postgres")
POSTGRES_TRACKER_STORE_DB = "tracker_store_db"
POSTGRES_LOGIN_DB = "login_db"


@pytest.fixture
def redis_lock_store() -> Iterator[RedisLockStore]:
    # we need one redis database per worker, otherwise
    # tests conflicts with each others when databases are flushed
    pytest_worker_id = os.getenv("PYTEST_XDIST_WORKER", "gw0")
    redis_database = int(pytest_worker_id.replace("gw", ""))
    lock_store = RedisLockStore(REDIS_HOST, REDIS_PORT, redis_database)
    try:
        yield lock_store
    finally:
        lock_store.red.flushdb()


@pytest.fixture
def postgres_login_db_connection() -> Iterator[sa.engine.Connection]:
    engine = sa.create_engine(
        sa.engine.url.URL(
            "postgresql",
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            username=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            database=POSTGRES_DEFAULT_DB,
            query={},
        )
    )

    conn = engine.connect()
    conn.execution_options(isolation_level="AUTOCOMMIT")
    try:
        _create_login_db(conn)
        yield conn
    finally:
        _drop_db(conn, POSTGRES_LOGIN_DB)
        _drop_db(conn, POSTGRES_TRACKER_STORE_DB)
        conn.close()
        engine.dispose()


def _create_login_db(connection: sa.engine.Connection) -> None:
    connection.execute(sa.text(f"CREATE DATABASE {POSTGRES_LOGIN_DB}"))


def _drop_db(connection: sa.engine.Connection, database_name: Text) -> None:
    connection.execute(sa.text(f"DROP DATABASE IF EXISTS {database_name}"))


@pytest.fixture
def redis_tracker_store(domain: Domain) -> Iterator[RedisTrackerStore]:
    # we need one redis database per worker, otherwise
    # tests conflicts with each others when databases are flushed
    pytest_worker_id = os.getenv("PYTEST_XDIST_WORKER", "gw0")
    redis_database = int(pytest_worker_id.replace("gw", ""))
    tracker_store = RedisTrackerStore(domain, db=redis_database)
    try:
        yield tracker_store
    finally:
        tracker_store.red.flushdb()
