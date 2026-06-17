# v0.4 Full Notes Archive Restore Guide

This archive directory is intended to store the complete v0.4 note bundle generated from the local assistant workspace.

## Current state

The full note bundle exists in the downloadable local artifact:

```text
video-mem-survey_v0.4_webread_2026-06-17.zip
```

Inside it:

```text
notes/paper_notes/WEB_READ_INDEX_v0.4.md
notes/paper_notes/WEB_READ_NOTES_ALL_v0.4.md
notes/paper_notes/WEB_READ_STATUS_v0.4.csv
notes/paper_notes/web_read_all_v0.4/*.md
```

The assistant environment cannot currently perform a normal `git clone && git push` because DNS resolution for `github.com` fails inside the execution container. The GitHub connector can create text files, but it is not efficient for expanding 100+ note files one by one.

## Recommended complete push from local checkout

After downloading or extracting the v0.4 artifact locally, run:

```bash
git clone https://github.com/Anachronism-N/video-mem-survey.git
cd video-mem-survey
cp -r /path/to/video-mem-survey/notes/paper_notes/* notes/paper_notes/
git add notes/paper_notes
git commit -m "Add full v0.4 web-read paper notes"
git push origin main
```

## Archive parts

If archive parts are present in this directory, reconstruct with:

```bash
cat web_read_notes_v0.4_all.tar.xz.b64.part* > web_read_notes_v0.4_all.tar.xz.b64
base64 -d web_read_notes_v0.4_all.tar.xz.b64 > web_read_notes_v0.4_all.tar.xz
tar -xJf web_read_notes_v0.4_all.tar.xz
```

This will recover `notes/paper_notes/` from the compressed archive.
