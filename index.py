import sys
from pathlib import Path

# 將 src 資料夾加入路徑，讓 Python 認得 gemini_mcp
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from gemini_mcp.server import mcp

# 導出給 Vercel 使用
app = mcp.sse_app()
