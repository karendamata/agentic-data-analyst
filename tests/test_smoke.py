import duckdb

import agentic_data_analyst


def test_package_imports() -> None:
    assert agentic_data_analyst is not None


def test_db_fixture(db: duckdb.DuckDBPyConnection) -> None:
    row = db.execute("SELECT SUM(amount) FROM sales WHERE region = 'north'").fetchone()
    assert row is not None
    assert row[0] == 150.0
