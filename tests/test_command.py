import pytest
from app import App

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    inputs = iter(['greet', 'exit'])

    def mock_input(_):
        try:
            return next(inputs)
        except StopIteration:
            return 'exit'

    monkeypatch.setattr('builtins.input', mock_input)

    app = App()
    with pytest.raises(SystemExit):
        app.start()

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'menu' command."""
    inputs = iter(['menu', 'exit'])

    def mock_input(_):
        try:
            return next(inputs)
        except StopIteration:
            return 'exit'

    monkeypatch.setattr('builtins.input', mock_input)

    app = App()
    with pytest.raises(SystemExit):
        app.start()

def test_app_add_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'add' command."""
    inputs = iter(['add', 'exit'])

    def mock_input(_):
        try:
            return next(inputs)
        except StopIteration:
            return 'exit'

    monkeypatch.setattr('builtins.input', mock_input)

    app = App()
    with pytest.raises(SystemExit):
        app.start()

def test_app_sub_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'sub' command."""
    inputs = iter(['sub', 'exit'])

    def mock_input(_):
        try:
            return next(inputs)
        except StopIteration:
            return 'exit'

    monkeypatch.setattr('builtins.input', mock_input)

    app = App()
    with pytest.raises(SystemExit):
        app.start()

def test_app_mul_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'mul' command."""
    inputs = iter(['mul', 'exit'])

    def mock_input(_):
        try:
            return next(inputs)
        except StopIteration:
            return 'exit'

    monkeypatch.setattr('builtins.input', mock_input)

    app = App()
    with pytest.raises(SystemExit):
        app.start()

def test_app_div_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'div' command."""
    inputs = iter(['div', 'exit'])

    def mock_input(_):
        try:
            return next(inputs)
        except StopIteration:
            return 'exit'

    monkeypatch.setattr('builtins.input', mock_input)

    app = App()
    with pytest.raises(SystemExit):
        app.start()
