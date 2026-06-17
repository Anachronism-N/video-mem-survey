#!/usr/bin/env python3
"""Download arXiv PDFs according to papers/download_manifest.tsv.

Usage:
  python scripts/download_papers.py --manifest papers/download_manifest.tsv --root .
"""
import argparse, csv, time, urllib.request
from pathlib import Path

def download(url: str, out: Path, retries: int = 3, sleep: float = 2.0) -> bool:
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists() and out.stat().st_size > 1024:
        print(f"[skip] {out}")
        return True
    for i in range(retries):
        try:
            print(f"[download] {url} -> {out}")
            req = urllib.request.Request(url, headers={"User-Agent":"video-mem-survey/0.2"})
            with urllib.request.urlopen(req, timeout=60) as r, open(out, 'wb') as f:
                f.write(r.read())
            if out.stat().st_size < 1024:
                raise RuntimeError("downloaded file too small")
            return True
        except Exception as e:
            print(f"[warn] attempt {i+1}/{retries} failed for {url}: {e}")
            time.sleep(sleep)
    return False

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--manifest', default='papers/download_manifest.tsv')
    ap.add_argument('--root', default='.')
    args = ap.parse_args()
    root = Path(args.root)
    ok = fail = 0
    with open(root / args.manifest, encoding='utf-8') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            target = root / row['target_path']
            if download(row['pdf_url'], target): ok += 1
            else: fail += 1
    print(f"done: ok={ok}, fail={fail}")
