# FoodResQ

Intelligent food surplus redistribution and logistics platform.

## Monorepo
- `apps/web` — React, TypeScript, Vite, Tailwind, Leaflet
- `apps/api` — Express, TypeScript, MongoDB, Socket.IO
- `services/ai` — FastAPI assistance service
- `packages/shared` — shared domain contracts

## Status
Initial implementation scaffold. See `docs/ARCHITECTURE.md` and `docs/API.md`.

## Local development
Copy `.env.example` to `.env`, configure MongoDB and optional Cloudinary/OpenAI credentials, then run `docker compose up --build`.

AI outputs are suggestions only. Food safety remains the responsibility of the donor and applicable local rules; images cannot certify freshness or safety. Routing durations are estimates, not delivery guarantees.
