# Pre-Flight Security Checklist
- [ ] RLS enabled on all tables in public schema
- [ ] SELECT/INSERT/UPDATE/DELETE policies bound to auth.uid()
- [ ] Rate-limiting enabled on public API routes
- [ ] No private keys or service tokens in NEXT_PUBLIC_ variables
