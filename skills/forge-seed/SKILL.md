---
name: forge-seed
description: >-
  Generates realistic, relational synthetic mock data and database seed scripts
  matching the schema from forge-architect. Populates the app with lifelike users,
  transactions, edge cases, timestamps, and relations so the UI feels alive during
  build and test. Use when the user says "seed the database", "generate mock data",
  "add dummy records", "populate test data", "seed users", or after forge-backend.
---

# forge-seed

An empty app feels dead. Testing an empty app hides layout bugs, pagination breaks,
and edge cases. `forge-seed` inspects your database schema or ORM models and generates
realistic, relational synthetic seed data so the UI looks and behaves like an active,
real-world product from day one.

Output goes in the user's project:

```
forge/seed.sql         executable SQL insert statements for PostgreSQL/Supabase/SQLite
prisma/seed.ts         (if using Prisma) executable TypeScript seeder script
forge/mock-data.json   JSON fixtures for API mocking or frontend state
```

## The rules

- **Relational integrity first.** Foreign keys must resolve. A comment belongs to a real post; a transaction belongs to a real user; an expense belongs to a real group.
- **Edge cases by design.** Don't just generate "John Doe 1". Generate long names, Unicode, emojis, negative and extreme values.
- **Zero external pip packages.** Uses the standard library only.
