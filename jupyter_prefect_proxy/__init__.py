"""
Return config on servers to start for prefect

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import shutil


def setup_prefect():
    def _prefect_command():
        full_path = shutil.which("prefect")
        if not full_path:
            raise FileNotFoundError("Can not find Prefect executable in $PATH")
        return ["prefect", "server", "start"]

    return {
        "command": _prefect_command(),
        "environment": {},
        "launcher_entry": {
            "title": "prefect",
            "icon_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "icons",
                "prefect.svg",
            ),
        },
    }
