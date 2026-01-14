#!/usr/bin/env python3
import json
import sys
from pathlib import Path


WINDOW_MS = 24 * 60 * 60 * 1000
GPT4_TRAIN_KWH = 62318750


def load_points(payload):
    if isinstance(payload, list):
        if payload and isinstance(payload[0], dict) and "data" in payload[0]:
            series = payload[0]["data"]
        else:
            series = payload
    elif isinstance(payload, dict) and "data" in payload:
        series = payload["data"]
    else:
        raise ValueError("Unsupported JSON structure for userdata.json")

    points = []
    for entry in series:
        if not isinstance(entry, (list, tuple)) or len(entry) != 2:
            raise ValueError("Each data point must be [timestamp_ms, concurrent_users]")
        ts, value = entry
        points.append((int(ts), float(value)))
    return points


def time_weighted_average(points, window_ms):
    if not points:
        raise ValueError("No data points to average")

    points.sort(key=lambda item: item[0])
    end_ts = points[-1][0]
    start_ts = end_ts - window_ms

    # Find the first point in or after the window start.
    idx = 0
    while idx < len(points) and points[idx][0] < start_ts:
        idx += 1

    if idx == 0:
        prev_value = points[0][1]
    else:
        prev_value = points[idx - 1][1]

    current_ts = start_ts
    weighted_total = 0.0

    for j in range(idx, len(points)):
        ts, value = points[j]
        if ts > end_ts:
            break
        if ts > current_ts:
            weighted_total += prev_value * (ts - current_ts)
            current_ts = ts
        prev_value = value

    if end_ts > current_ts:
        weighted_total += prev_value * (end_ts - current_ts)

    return weighted_total / window_ms


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("userdata.json")
    with path.open() as handle:
        payload = json.load(handle)

    points = load_points(payload)
    avg_concurrent = time_weighted_average(points, WINDOW_MS)

    active_players = avg_concurrent * 0.5  # Estimate of logged-in users actively playing.
    avg_gpu_kwh_per_hour = active_players * 0.2  # 0.2 kWh per hour (~0.2 kW) per active player.
    total_kwh_24h = avg_gpu_kwh_per_hour * 24

    ratio = total_kwh_24h / GPT4_TRAIN_KWH

    rows = [
        ("Steam games (24h)", f"{round(total_kwh_24h):,} kWh"),
        ("GPT-4 training", f"{GPT4_TRAIN_KWH:,} kWh"),
        ("Ratio", f"{ratio:,.6f}"),
    ]
    label_width = max(len(label) for label, _ in rows)
    value_width = max(len(value) for _, value in rows)

    for label, value in rows:
        print(f"{label:<{label_width}}: {value:>{value_width}}")


if __name__ == "__main__":
    main()
