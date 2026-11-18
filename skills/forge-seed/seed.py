#!/usr/bin/env python3
import argparse, json, random, sys, uuid
from datetime import datetime, timedelta

FIRST_NAMES = ["Sarah", "Marcus", "Elena", "Liam", "Sophia", "Lucas", "Priya", "Carlos"]
LAST_NAMES = ["Connor", "Wright", "Rostova", "Chen", "Patel", "Montgomery-Vanderbilt III"]
DOMAINS = ["example.com", "mailtest.org", "demoapp.dev"]

def generate_users(count=5):
    users = []
    for i in range(count):
        fn, ln = random.choice(FIRST_NAMES), random.choice(LAST_NAMES)
        uid = f"a0000000-0000-0000-0000-{i+1:012d}"
        email = f"{fn.lower()}.{ln.lower()[:6]}@{random.choice(DOMAINS)}"
        users.append({"id": uid, "name": f"{fn} {ln}", "email": email})
    return users

def to_sql(users, table_name="profiles"):
    sql = [f"INSERT INTO {table_name} (id, full_name, email) VALUES"]
    rows = [f"  ('{u['id']}', '{u['name'].replace(\"'\", \"''\")}', '{u['email']}')" for u in users]
    return "\n".join(sql) + "\n" + ",\n".join(rows) + ";\n"

if __name__ == '__main__':
    u = generate_users(5)
    print(to_sql(u))
