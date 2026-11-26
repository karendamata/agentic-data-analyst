from collections.abc import Iterator

import duckdb
import pytest


@pytest.fixture
def db() -> Iterator[duckdb.DuckDBPyConnection]:
    """A small in-memory DuckDB database for testing SQL helpers."""
    conn = duckdb.connect(":memory:")
    conn.execute(
        """
        CREATE TABLE sales (
            id INTEGER PRIMARY KEY,
            region VARCHAR NOT NULL,
            amount DOUBLE NOT NULL
        );
        INSERT INTO sales VALUES
            (1, 'north', 100.0),
            (2, 'south', 250.0),
            (3, 'north', 50.0);
        """
    )
    yield conn
    conn.close()
