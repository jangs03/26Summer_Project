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
CHROMA_DIR = DATA_DIR / "chroma"
COLLECTION_NAME = "arxiv_papers"

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
