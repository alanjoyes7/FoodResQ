Base URL /api. Errors: {error:{code,message}}.

GET /health — health. GET /api/donations?page=1&limit=20&category= — paginated live listings. GET /api/donations/nearby?lon=&lat=&km= — geospatial search. POST /api/donations — publish. GET /api/matching/:donationId — ranked matches. POST /api/donations/:id/request — conditional reservation. PATCH /api/requests/:id/approve — approve. GET /api/analytics — live aggregates.

Socket.IO events: donation:published, request:created, request:approved.

Production must add JWT auth and role guards before exposing write routes. Persistent per-user notification records, authenticated socket rooms, pickup and route APIs are still required.