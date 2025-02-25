'''This is the test_app file'''
import pytest
from app import App
import importlib

# Testing that the REPL exits correctly on 'exit' command
def test_app_start_exit_command(monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit):
        app.start()

# Testing how the REPL handles an unknown command before exiting
def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "unknown_command : Command not found" in captured.out, "App should notify user of unknown command"


# Testing executing a command with arguments
def test_app_command_with_args(capfd, monkeypatch):
    """Test executing a command with arguments."""
    # Simulate user entering a command with arguments, then exit
    inputs = iter(['add 5 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    # Catch the SystemExit to test the exit behavior
    with pytest.raises(SystemExit):
        app.start()
