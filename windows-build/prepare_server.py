from pathlib import Path

root = Path(__file__).resolve().parent.parent
source = root / "server" / "server.py"
target_dir = root / "build" / "server"
target_dir.mkdir(parents=True, exist_ok=True)
target = target_dir / "server_windows.py"
original = source.read_text(encoding="utf-8")
text = original.replace(
    'Path(__file__).with_name("players.json")',
    'Path(os.environ.get("NFS13_DATA_DIR", Path(sys.executable).resolve().parent)) / "players.json"',
)
text = text.replace(
    'Path(__file__).with_name("license_plates.json")',
    'Path(os.environ.get("NFS13_DATA_DIR", Path(sys.executable).resolve().parent)) / "license_plates.json"',
)
if text == original:
    raise SystemExit("Expected persistent-data paths were not found; refusing to create a potentially broken build.")
target.write_text(text, encoding="utf-8")
print(f"Prepared {target}")
