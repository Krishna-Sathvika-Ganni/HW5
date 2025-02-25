import pytest
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit):
        app.start()

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    
    def mock_input(_):
        try:
            return next(inputs)
        except StopIteration:
            return 'exit'

    monkeypatch.setattr('builtins.input', mock_input)

    app = App()
    
    with pytest.raises(SystemExit):
        app.start()
    
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out
