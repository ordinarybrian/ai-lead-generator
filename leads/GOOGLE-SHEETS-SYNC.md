# Google Sheets sync

`lead-index.csv` can sync in both directions with a Google Sheet. Local-only
changes are pushed, Sheet-only changes are pulled, and competing changes stop
with a conflict instead of overwriting data.

## One-time setup

1. Create a Google Cloud service account, enable the Google Sheets API, and
   download its JSON key outside this project.
2. Create the spreadsheet and share it as an editor with the service account's
   email address (the `client_email` in the JSON key).
3. Create the Python environment:

   ```sh
   python3 -m venv .venv
   .venv/bin/pip install -r requirements-sync.txt
   ```

4. Export the three settings shown in `.env.lead-index.example`, then run:

   ```sh
   .venv/bin/python scripts/sync_lead_index.py
   ```

The configured tab name is `Sheet1`; the script creates it when needed. On the
first run, an empty Sheet is populated from the CSV. Because this CSV currently
has only a header, a populated Sheet with the same header is pulled locally.

## Continuous sync on macOS

Copy `scripts/com.seniorcenter.lead-index-sync.plist.example` to
`~/Library/LaunchAgents/com.seniorcenter.lead-index-sync.plist`, replace all
placeholders with absolute paths/values, and load it:

```sh
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.seniorcenter.lead-index-sync.plist
```

It checks every 60 seconds. To stop it, use `launchctl bootout` with the same
plist path.

## Conflicts

When both sides changed since the last successful sync, inspect both and choose
the version to keep:

```sh
.venv/bin/python scripts/sync_lead_index.py --prefer local
.venv/bin/python scripts/sync_lead_index.py --prefer sheet
```

The local sync marker is `.sync/lead-index-state.json`; it contains only a
content hash, not credentials or lead data.
