'''This is the test_app file'''
import pytest
import importlib
import pkgutil
from app import App

def test_app_start_exit_command(monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit):
        app.start()

def test_plugin_load_success_and_failure(capsys, monkeypatch):
    """Test plugin loading, ensuring successful and failed imports are handled properly."""
    
    def mock_import_module(name):
        """Mock import_module to simulate a broken plugin."""
        if 'broken_plugin' in name:
            raise ImportError("Mock import error")
        return importlib.import_module(name)  # Properly return the requested module

    
    # Simulating a working plugin and a failing one
    monkeypatch.setattr(pkgutil, 'iter_modules',
                        lambda _: [('', 'working_plugin', ''), ('', 'broken_plugin', '')])
    monkeypatch.setattr(importlib, 'import_module', mock_import_module)

    _ = App()  # Instantiating App triggers plugin loading

    captured = capsys.readouterr()
    assert "Failed to load plugin broken_plugin" in captured.out

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('name.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "unknown_command : Command not found" in captured.out, "App should notify user of unknown command"