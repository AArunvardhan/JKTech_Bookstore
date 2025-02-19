# Bookstore Test Suite

## Testing Strategy
- **Unit Tests**:
  - Mocked external dependencies (e.g., JWT token verification).
  - Focused on utility functions and middleware.
  - Achieved 85% coverage using pytest-cov.

- **Integration Tests**:
  - Real MongoDB instance in Docker.
  - Async HTTP requests using `httpx.AsyncClient`.
  - Full CRUD operation validation.

## Running Tests
```bash
# Install dependencies
pip install -r requirements.txt

# Unit tests with coverage
pytest tests/unit --cov

# Integration tests (requires running MongoDB)
docker-compose up -d mongo
pytest tests/integration