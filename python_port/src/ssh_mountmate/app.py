from __future__ import annotations

import argparse
from pathlib import Path
from tkinter import BOTH, LEFT, RIGHT, X, Button, Frame, Label, Listbox, StringVar, Tk

from . import APP_NAME, VERSION
from .config_store import load_configs
from .platforms import current_platform
from .rclone import resolve_rclone, rclone_version


class App:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title(APP_NAME)
        self.root.geometry("720x420")
        self.status = StringVar(value="Ready")
        self.app_root = Path(__file__).resolve().parents[2]
        self.platform = current_platform()
        self.rclone_path = resolve_rclone(self.app_root)
        self.build()
        self.refresh()

    def build(self) -> None:
        top = Frame(self.root, padx=10, pady=8)
        top.pack(fill=X)
        Label(top, text=f"{APP_NAME} Python Port {VERSION}").pack(side=LEFT)
        Button(top, text="Refresh", command=self.refresh).pack(side=RIGHT)

        deps = Frame(self.root, padx=10, pady=6)
        deps.pack(fill=X)
        self.deps_label = Label(deps, anchor="w", justify=LEFT)
        self.deps_label.pack(fill=X)

        body = Frame(self.root, padx=10, pady=8)
        body.pack(fill=BOTH, expand=True)
        self.configs = Listbox(body)
        self.configs.pack(fill=BOTH, expand=True)

        bottom = Frame(self.root, padx=10, pady=8)
        bottom.pack(fill=X)
        Label(bottom, textvariable=self.status).pack(side=LEFT)

    def refresh(self) -> None:
        self.rclone_path = resolve_rclone(self.app_root)
        rclone_text = rclone_version(self.rclone_path)
        mount_dep = self.platform.mount_dependency_name
        mount_dep_status = "installed" if self.platform.mount_dependency_installed() else "missing or unchecked"
        self.deps_label.configure(
            text=(
                f"Platform: {self.platform.system}\n"
                f"rclone: {rclone_text}\n"
                f"{mount_dep}: {mount_dep_status}"
            )
        )
        self.configs.delete(0, "end")
        configs = load_configs()
        if not configs:
            self.configs.insert("end", "No configs yet.")
        for config in configs:
            self.configs.insert(
                "end",
                f"{config.name}  {config.user}@{config.host}  {config.remote_path or '~'}  {config.display_mountpoint}",
            )
        self.status.set("Refreshed")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ssh-mountmate")
    parser.add_argument("--version", action="version", version=f"{APP_NAME} Python Port {VERSION}")
    parser.parse_args(argv)
    root = Tk()
    App(root)
    root.mainloop()
    return 0
