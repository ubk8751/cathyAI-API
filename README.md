# Cathy AI API

FastAPI proxy service for AI backends (Ollama, etc.).

## Setup

1. **Clone and navigate:**
   ```bash
   cd cathyAI-API
   ```

2. **Configure environment:**
   ```bash
   cp .env.template .env
   # Edit .env with your backend URL
   ```

3. **Install dependencies:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Start backend** (e.g., Ollama):
   ```bash
   ollama serve
   ```

5. **Run proxy:**
   ```bash
   uvicorn main:app --reload
   ```

## Endpoints

- `GET /health` - Health check + backend status
- `GET /models` - List model names
- `GET /models/raw` - Raw backend models response
- `POST /api/generate` - Text generation (streaming/non-streaming)
- `POST /api/chat` - Chat completions (streaming/non-streaming)

## Configuration

`.env` variables:
- `AI_BACKEND_URL` - Backend URL (default: `http://127.0.0.1:11434`)
- `EMOTION_ENABLED` - Feature flag (default: `false`)

## Usage

```bash
# Health check
curl http://localhost:8000/health

# List models
curl http://localhost:8000/models

# Raw models data
curl http://localhost:8000/models/raw

# Generate text (streaming, default)
curl -N http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{"model":"llama2","prompt":"Hello"}'

# Generate text (non-streaming)
curl http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{"model":"llama2","prompt":"Hello","stream":false}'

# Chat (streaming, default)
curl -N http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"model":"llama2","messages":[{"role":"user","content":"Hi"}]}'

# Chat (non-streaming)
curl http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"model":"llama2","messages":[{"role":"user","content":"Hi"}],"stream":false}'
```

## Testing

```bash
python3 -m pytest test_main.py -v
```
