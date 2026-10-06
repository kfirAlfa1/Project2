# Agent notes

- This is a Tkinter desktop app (easygui), not a web app. `docker-compose.base44.yml` runs it in Xvfb and streams it via noVNC on port 3000 (`/` redirects to `vnc.html?autoconnect=1`).
- Entry point: `src/gui.py` (run from `src/`, imports `api`). It is relaunched in a loop when closed, so code edits apply on the next launch.
- The OpenWeatherMap API key is hardcoded in `src/api.py`; no secrets are needed.
- Verify: open the preview, type an Israeli city (e.g. "Haifa"), press OK; a forecast window with date buttons appears.
