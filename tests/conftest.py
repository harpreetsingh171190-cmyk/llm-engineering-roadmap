import sys
from pathlib import Path

# Make the scripts/ folder importable from the tests.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
