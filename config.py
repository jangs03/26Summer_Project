"""
전역 설정값 모음.
- 카테고리, 저장 경로, 임베딩 모델 등을 한 곳에서 관리합니다.
"""

from pathlib import Path

# ── 수집 대상 카테고리 ──────────────────────────────────────
CATEGORIES = ["cs.RO", "cs.CV", "cs.CL"]

# ── 저장 경로 ────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

SQLITE_PATH = DATA_DIR / "papers.db"
CHROMA_DIR = DATA_DIR / "chroma"  # 서버를 띄우는 쪽(호스트)에서만 사용됨
COLLECTION_NAME = "arxiv_papers"

# ── Chroma 접속 모드 ─────────────────────────────────────
# "http"       : 팀 공유 서버(HttpClient)로 접속. 팀원 전원이 같은 DB를 봄.
# "persistent" : 로컬 파일(PersistentClient)로 접속. 개인 테스트/오프라인 작업용.
CHROMA_MODE = "http"  # "http" 또는 "persistent"

# CHROMA_MODE == "http" 일 때 사용.
# 서버를 띄운 사람(또는 항상 켜져 있는 공유 머신)의 주소로 채워 넣기.
# 사내망/VPN(Tailscale 등)으로 묶여있다면 사설 IP나 Tailscale 호스트명을 그대로 써도 됨.
CHROMA_HOST = "localhost"   # 예: "100.101.102.103" (Tailscale IP) 또는 팀 공유 서버 IP
CHROMA_PORT = 8000

# ── 임베딩 모델 ──────────────────────────────────────────
# 로컬에서 무료로 돌아가는 sentence-transformers 모델.
# 영어 초록 검색 품질 대비 속도가 좋아 기본값으로 추천.
# 더 높은 품질이 필요하면 "BAAI/bge-base-en-v1.5" 로 교체 가능(속도는 느려짐).
EMBEDDING_MODEL_NAME = "BAAI/bge-small-en-v1.5"
EMBEDDING_BATCH_SIZE = 64

# ── arXiv API 호출 관련 ───────────────────────────────────
# 라이브러리 내부적으로 페이지당 결과 수. 너무 크게 잡으면 API가 종종 끊기므로 100 권장.
ARXIV_PAGE_SIZE = 100
# 연속 호출 사이 대기시간(초). arXiv 정책상 3초 이상 권장.
ARXIV_DELAY_SECONDS = 3.0
ARXIV_NUM_RETRIES = 3

# 마지막 수집 시각을 기록해두는 파일(매일 증분 수집 시 사용)
LAST_RUN_PATH = DATA_DIR / "last_run.json"
