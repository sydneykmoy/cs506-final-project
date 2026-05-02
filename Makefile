# ==============================================================================
# Makefile — CS506 Final Project
# ==============================================================================
# Usage:
#   make install    Install all Python dependencies
#   make run        Run the full pipeline
# ==============================================================================

PYTHON = py
PIP    = py -m pip

.PHONY: install run

# ── Install dependencies ──────────────────────────────────────────────────────
install:
	$(PIP) install -r requirements.txt

# ── Run the full pipeline ─────────────────────────────────────────────────────
run:
	$(PYTHON) main.py