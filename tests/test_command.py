import pytest
from app import App

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'menu' command."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_add_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'add' command."""
    inputs = iter(['add', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_sub_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'sub' command."""
    inputs = iter(['sub', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_mul_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'mul' command."""
    inputs = iter(['mul', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_div_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'div' command."""
    inputs = iter(['div', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"
