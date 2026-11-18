-- forge-seed template for relational PostgreSQL / Supabase
INSERT INTO profiles (id, full_name, email, created_at) VALUES
  ('a0000000-0000-0000-0000-000000000001', 'Sarah Connor', 'sarah.connor@example.com', NOW() - INTERVAL '60 days'),
  ('a0000000-0000-0000-0000-000000000002', 'Marcus Wright', 'marcus.wright@example.com', NOW() - INTERVAL '45 days'),
  ('a0000000-0000-0000-0000-000000000003', 'Dr. Alexander Montgomery-Vanderbilt III 🚀', 'dr.alexander@example.com', NOW() - INTERVAL '10 days')
ON CONFLICT (id) DO NOTHING;
