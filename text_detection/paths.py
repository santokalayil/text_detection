from pathlib import Path

TESSERACT_PATH = Path(r"/opt/homebrew/bin/tesseract")

MAIN_DIR = Path(__file__).parent.parent
DATA_DIR = MAIN_DIR / "data"
