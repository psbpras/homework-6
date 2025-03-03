import importlib
import pkgutil
import app.commands

def load_plugins():
    """Dynamically loads plugins (command modules)."""
    plugins = {}
    for _, module_name, _ in pkgutil.iter_modules(app.commands.__path__, "app.commands."):
        module = importlib.import_module(module_name)
        if hasattr(module, "register_command"):
            module.register_command(plugins)
    return plugins
