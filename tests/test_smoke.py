"""Smoke test to confirm the test runner and package import work."""

import forecasting


def test_package_imports() -> None:
    """The forecasting package should be importable."""
    assert forecasting is not None
