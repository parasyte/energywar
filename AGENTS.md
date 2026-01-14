# Repository Guidelines

## Project Structure & Module Organization
- `steam_power.py` contains the calculation logic for estimating 24-hour power usage.
- `userdata.json` is a local snapshot of Steam concurrent user data (timestamp/value pairs).
- `README.md` provides high-level context and data-source links.

This repository is intentionally small and script-centric; there are no subpackages or assets.

## Build, Test, and Development Commands
- `python3 steam_power.py` runs the calculation using `userdata.json` in the repo root.
- `python3 steam_power.py path/to/userdata.json` runs the calculation on a different dataset.

There is no separate build step or dependency installation for the current script.

## Coding Style & Naming Conventions
- Python code uses 4-space indentation.
- Use descriptive, lower_snake_case variable names (e.g., `avg_gpu_kwh_per_hour`).
- Keep comments short and focused on assumptions or units.
- Prefer standard library only; add dependencies only if essential.

## Testing Guidelines
- No test suite is currently defined.
- If you add tests, prefer `pytest` and keep tests alongside the script (e.g., `test_steam_power.py`).
- Name tests to reflect intent (e.g., `test_time_weighted_average_handles_gaps`).

## Commit & Pull Request Guidelines
- No Git history is present in this workspace, so commit conventions are unknown.
- If you introduce a commit style, keep messages short and imperative (e.g., "Add time-weighted averaging").
- For PRs, include a brief description of assumptions (e.g., units and multipliers) and sample output.

## Data & Assumptions
- `userdata.json` is expected to contain an array of `[timestamp_ms, concurrent_users]` points.
- The script computes a 24-hour rolling window anchored to the latest timestamp in the file.
- Assumptions such as active-user fractions or kWh/hour rates should be documented inline.
