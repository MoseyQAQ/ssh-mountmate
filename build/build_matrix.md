# Build Matrix Plan

True cross-compilation is not the primary plan. Build the same source on each
target platform instead.

| Target | Builder | Expected artifact |
| --- | --- | --- |
| Windows x64 | `windows-latest` | `SSHMountMate.exe` |
| macOS arm64/x64 | `macos-latest` | `SSHMountMate` or `.app` bundle |
| Linux x64 | `ubuntu-latest` | `SSHMountMate` tarball/AppImage candidate |

CI installs `.[build]` and runs:

```bash
python build/build_local.py
```

The build script downloads the official rclone zip for the runner platform and
embeds the extracted binary with PyInstaller. Runtime fallback can still
download rclone into a managed per-user bin directory when the bundled binary is
unavailable.
