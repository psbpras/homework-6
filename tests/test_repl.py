"""Unit tests for the REPL module."""

from unittest.mock import patch
from app.repl import repl

@patch("builtins.input", side_effect=["menu", "add 3 4", "exit"])
@patch("builtins.print")
def test_repl(mock_print, mock_input):
    """Tests the REPL's ability to process user input and display results."""
    _ = mock_input  # Suppress unused argument warning
    repl()
    mock_print.assert_any_call("Result:", 7)
