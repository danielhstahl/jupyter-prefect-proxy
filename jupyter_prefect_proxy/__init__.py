"""
Return config on servers to start for prefect

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import shutil
import logging

logger = logging.getLogger(__name__)
logger.setLevel("INFO")
PORT = 4200
def setup_prefect():
    def _prefect_command(port, base_url): 
        logger.info(f"Using base_url {base_url} and port {port}")
        full_path = shutil.which("prefect")
        if not full_path:
            raise FileNotFoundError("Can not find Prefect executable in $PATH")
        return ["prefect", "server", "start", "--port", str(port)]

    return {
        "command": _prefect_command,
        #"environment": {"PREFECT_UI_API_URL": "{base_url}/api"}, # PREFECT_UI_SERVE_BASE
        "new_browser_tab": False,
        #"absolute_url": False,
        "port": PORT, # default for prefect
        "launcher_entry": {
            "title": "prefect",
            "icon_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "icons",
                "prefect.svg",
            ),
        },
    }
