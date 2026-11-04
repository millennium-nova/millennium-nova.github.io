#!/usr/bin/env python3
"""Run inside the OLD container before its first rebuild with persistent mounts."""
import os
from pathlib import Path
import shutil
import sqlite3
import stat
import tempfile

root = Path(__file__).resolve().parent / "state"
root.mkdir(mode=0o700, exist_ok=True)
root.chmod(0o700)

for name, source in (("codex", Path.home() / ".codex"),
                     ("vscode-server", Path.home() / ".vscode-server")):
    target = root / name
    if not source.is_dir():
        print(f"Skip {name}: source does not exist")
        continue
    if target.exists() and os.path.samefile(source, target):
        print(f"{name}: already persistent")
        continue

    # Never copy live SQLite WAL/SHM files. Use SQLite's consistent backup API.
    databases = []
    def ignore(directory, names):
        ignored = []
        for entry in names:
            path = Path(directory) / entry
            if path.is_symlink():
                continue
            if stat.S_ISSOCK(path.stat().st_mode):
                ignored.append(entry)
            elif path.is_file() and path.suffix in (".sqlite", ".vscdb"):
                databases.append(path)
                ignored.append(entry)
            elif entry.endswith(("-wal", "-shm", "-journal")):
                ignored.append(entry)
        return ignored

    staging = Path(tempfile.mkdtemp(prefix=f".{name}-", dir=root))
    try:
        shutil.copytree(source, staging, symlinks=True, dirs_exist_ok=True, ignore=ignore)
        for database in databases:
            destination = staging / database.relative_to(source)
            with sqlite3.connect(database.as_uri() + "?mode=ro", uri=True) as src:
                with sqlite3.connect(destination) as dst:
                    src.backup(dst)
            shutil.copystat(database, destination)
        # Keep the previous snapshot until the new one has finished copying.
        previous = root / f".{name}-previous"
        if previous.exists():
            shutil.rmtree(previous)
        if target.exists():
            target.rename(previous)
        staging.rename(target)
        if previous.exists():
            shutil.rmtree(previous)
    except BaseException:
        if staging.exists():
            shutil.rmtree(staging)
        raise
    print(f"Saved {name} to {target}")

print("Snapshot complete. Run again just before rebuilding to capture later conversations.")
