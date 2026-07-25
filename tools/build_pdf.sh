#!/bin/sh
# Build the working-draft PDF of the white paper.
# Requires: brew install tectonic pandoc (installed 2026-07-25).
cd "$(dirname "$0")/.." || exit 1
mkdir -p build
exec pandoc README.md book/0*.md -s --toc \
  -M title="Minimal Evolving Systems — working draft (v0.0)" \
  -M date="$(date +%Y-%m-%d)" \
  --pdf-engine=tectonic \
  -V mainfont="STIX Two Text" -V monofont="Menlo" \
  -V geometry:margin=1.1in \
  -H tools/pdf_header.tex \
  -o build/whitepaper.pdf "$@"
