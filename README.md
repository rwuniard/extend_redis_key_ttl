# Extend Redis Key TTL

A Python script that extends the TTL of all expiring keys in a Redis instance to 6 months.

## What it does

- Scans all keys in Redis using cursor-based `SCAN` (safe for production, non-blocking)
- For each key that has an existing TTL, extends it to 6 months (~15,552,000 seconds)
- Skips persistent keys (keys with no expiry set)
- Prints a summary of extended vs skipped keys

## Requirements

- Python 3.x
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- A running Redis instance

## Setup

1. Clone the repo and install dependencies:

```bash
uv sync
```

2. Copy and configure the environment file:

```bash
cp .env.example .env
```

Edit `.env`:

```
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=yourpassword
```

> Note: Do not use spaces around `=` in the `.env` file. `.env` is gitignored by default.

## Usage

```bash
uv run main.py
```

Example output:

```
Connecting to Redis at localhost:6379
Extending all keys with TTL of 15552000 seconds
Skipping key b'some-persistent-key' because it has no TTL
Done. Extended: 980, Skipped (no TTL): 20
```
