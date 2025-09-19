# flask-uv-demo

A simple Flask application created with uv that provides a GET endpoint at `/v1/someone-to-talk`.

## Setup

This project uses `uv` for dependency management. To run the application:

1. Install uv (if not already installed):
   ```bash
   pip install uv
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Run the application:
   ```bash
   uv run python main.py
   ```

The server will start on `http://localhost:5000`.

## API Endpoints

- **GET** `/v1/someone-to-talk` - Returns the text "person you're talking now"

## Example Usage

```bash
curl http://localhost:5000/v1/someone-to-talk
# Response: person you're talking now
```