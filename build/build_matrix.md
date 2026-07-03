# Build Matrix Plan

True cross-compilation is not the primary plan. Build the same source on each
target platform instead.

| Target | Builder | Expected artifact |
| --- | --- | --- |
| Windows x64 | `windows-latest` | `SSHMountMate-windows-x64.zip` |
| Windows arm64 | `windows-11-arm` | `SSHMountMate-windows-arm64.zip` |
| macOS x64 | `macos-15-intel` | `SSHMountMate-macos-x64.zip` |
| macOS arm64 | `macos-14` | `SSHMountMate-macos-arm64.zip` |
| Linux x64 | `ubuntu-latest` | `SSHMountMate-linux-x64.zip` |
| Linux arm64 | `ubuntu-24.04-arm` | `SSHMountMate-linux-arm64.zip` |

CI installs `.[build]` and runs:

```bash
python build/build_local.py
```

The build script downloads the official rclone zip for the runner platform and
embeds the extracted binary with PyInstaller. Runtime fallback can still
download rclone into a managed per-user bin directory when the bundled binary is
unavailable.
