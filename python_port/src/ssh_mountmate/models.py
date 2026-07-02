from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class MountConfig:
    id: str
    name: str
    source: str
    host_alias: str
    host: str
    user: str
    port: str = "22"
    remote_path: str = ""
    mountpoint: str = ""

    @property
    def display_mountpoint(self) -> str:
        return self.mountpoint or "Auto"
