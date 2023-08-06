"""
Return config on servers to start for prefect

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import shutil


def setup_prefect():
    def _prefect_command(port, base_url): 
        print("this is the base url: "+base_url)
        full_path = shutil.which("prefect")
        if not full_path:
            raise FileNotFoundError("Can not find Prefect executable in $PATH")
        return ["prefect", "server", "start", "--port", str(port)]

    return {
        "command": _prefect_command,
        "environment": {"PREFECT_UI_API_URL": "{base_url}/api"},
        "absolute_url": False,
        "port": 4200, # default for prefect
        "launcher_entry": {
            "title": "prefect",
            "icon_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "icons",
                "prefect.svg",
            ),
        },
    }
