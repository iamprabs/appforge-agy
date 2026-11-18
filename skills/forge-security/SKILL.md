---
name: forge-security
description: >-
  Audits the application for security vulnerabilities, PostgreSQL Row-Level Security
  (RLS) leaks, OWASP top 10 risks, rate-limiting, CORS, and privacy compliance
  (GDPR/CCPA). Runs before deployment to ensure user data cannot leak between tenants.
  Use when the user says "security audit", "check RLS", "audit permissions",
  "harden app", "GDPR compliance", or before forge-deploy.
---

# forge-security

A functional app is dangerous if one tenant can view or mutate another tenant's records.
`forge-security` audits database access rules, API route authorizations, and compliance endpoints.
