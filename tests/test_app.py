'''This is the test_app file'''
import importlib
import pytest
from app import App

def test_app_start_exit_command(monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit):
        app.start()

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

def test_plugin_load_success_and_failure(capsys, monkeypatch):
    """Test both successful and failed plugin loading."""
    def mock_import_module(name):
        """Mock import_module to handle both success and failure cases."""
        if 'broken_plugin' in name:
            raise ImportError("Mock import error")
        return importlib.__import__('builtins')  # Return a real module for success case
    # Mock pkgutil.iter_modules to return both a working and broken plugin
    monkeypatch.setattr('pkgutil.iter_modules',
                       lambda _: [('', 'working_plugin', ''), ('', 'broken_plugin', '')])
    # Mock importlib.import_module
    monkeypatch.setattr('importlib.import_module', mock_import_module)

    # Create app instance which will trigger plugin loading
    _ = App()

    # Check that both success and failure were logged
    captured = capsys.readouterr()
    assert "Failed to load plugin broken_plugin" in captured.out

def app_command_with_args(capfd,monkeypatch):
    '''Test how the REPL handles test app command with arguments '''
    inputs=iter(['Add 2 4', 'exit'])
    monkeypatch.seattr('builtins.input', lambda _: next(inputs) )

    app=App()
    with pytest.raises(SystemExit):
        app.start()

# End
