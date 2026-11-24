# FoodResQ

Intelligent food surplus redistribution and logistics platform.

## Monorepo
- `apps/web` — React, TypeScript, Vite responsive web app
- `apps/api` — Express, TypeScript, MongoDB, Socket.IO
- `services/ai` — FastAPI optional OpenAI listing assistant
- `packages/shared` — shared domain contracts
- `docs` — architecture and API contracts

## Implemented foundation
- Responsive public discovery landing page with live donation and analytics reads
- Donation listing and geospatial nearby API
- Explainable weighted receiver matching (30% distance, 25% quantity, 20% urgency, 15% category, 10% capacity)
- Conditional donation reservation and unique donation/receiver request index
- Request approval endpoint, Socket.IO events, analytics aggregates
- Optional editable AI listing suggestions; no food-safety claims

## Local development
Use Node 22+. Copy `.env.example` to `.env`, configure MongoDB and a strong JWT secret, then install workspace dependencies and run `npm run dev`. Docker Compose is included as a starting point. Web: localhost:5173; API: localhost:4000; AI: localhost:8000.

## Production gaps
Complete JWT registration/login and role middleware; persistent notifications, pickup and route-plan records; Cloudinary signed uploads; authenticated Socket.IO rooms; OSRM route optimizer; admin verification and audit workflow; replica-set transactions; comprehensive integration/security tests; seed 10 donors, 10 receivers and 40 demo donations; finish donor/receiver/admin UI workflows. Write APIs are not yet protected by JWT, so do not expose them publicly until auth guards are implemented.

AI cannot certify freshness, contamination, allergens or food safety. Handling notes are donor-provided. Environmental impact requires disclosed assumptions. Routing durations are estimates, not delivery guarantees.

## Deployment
Vercel root directory `apps/web`, build `npm run build`, output `dist`, and `VITE_API_URL` set to the deployed API. Deploy API and AI separately. Configure MongoDB Atlas, CORS, JWT_SECRET, OPENAI_API_KEY and Cloudinary credentials through hosting environment settings. Never commit secrets.
