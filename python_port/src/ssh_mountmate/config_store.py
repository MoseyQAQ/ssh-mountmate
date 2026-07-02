from __future__ import annotations

import json

from .models import MountConfig
from .paths import servers_file


def load_configs() -> list[MountConfig]:
    path = servers_file()
    if not path.exists():
        return []
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []
    configs: list[MountConfig] = []
    for item in raw if isinstance(raw, list) else []:
        if not isinstance(item, dict):
            continue
        configs.append(
            MountConfig(
                id=str(item.get("id") or ""),
                name=str(item.get("name") or item.get("id") or ""),
                source=str(item.get("source") or item.get("mode") or "manual"),
                host_alias=str(item.get("host_alias") or ""),
                host=str(item.get("host") or ""),
                user=str(item.get("user") or ""),
                port=str(item.get("port") or "22"),
                remote_path=str(item.get("remote_path") or ""),
                mountpoint=str(item.get("mountpoint") or ""),
            )
        )
    return configs
