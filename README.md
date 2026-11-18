# AppForge (appforge-agy)

<p align="center">
  <strong>Seventeen modular skills for Google Antigravity that forge any app.</strong><br>
  <em>Reverse-engineer, architect, AI-supercharge, test, rebrand, and deploy clean-room software.</em>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/platform-Antigravity%20%7C%20AGY-orange.svg" alt="Platform: Antigravity">
  <img src="https://img.shields.io/badge/skills-17%20Modular%20Skills-green.svg" alt="17 Skills">
  <img src="https://img.shields.io/badge/dependencies-Zero%20pip%20installs-brightgreen.svg" alt="Zero Dependencies">
</p>

---

## What is AppForge?

**AppForge** is a production-grade suite of 17 modular skills and agents built specifically for **Google Antigravity**. 

One skill reverse-engineers the app you want to recreate. One architects the stack and SQL schema. One generates original design tokens. Another writes the code screen by screen. And others inject AI superpowers, audit database security, seed realistic test records, find what the original app's users hate in real reviews, rebrand it, and deploy it live to your domain.

> **Clean-Room Engineering Guarantee:**  
> AppForge rebuilds **what an app does, never what it owns**. UX flows and functional architecture, clean-room style. Not proprietary code, copyrighted graphics, private APIs, or brand assets.

---

## Installation in Antigravity

### Option 1: Global Plugin (Recommended)

Clone directly into your global Antigravity plugins directory:

```bash
git clone https://github.com/iamprabs/appforge-agy.git ~/.gemini/config/plugins/appforge-agy
```

*(On Windows PowerShell):*
```powershell
git clone https://github.com/iamprabs/appforge-agy.git "$env:USERPROFILE\.gemini\config\plugins\appforge-agy"
```

Once cloned, Antigravity automatically discovers `plugin.json` and loads all 17 skills across all your workspaces.

---

### Option 2: Project-Local (`.agents/skills/`)

If you want AppForge available only inside a specific repository, copy the skills folder into your project root:

```bash
git clone https://github.com/iamprabs/appforge-agy.git /tmp/appforge
cp -r /tmp/appforge/skills/* ./your-project/.agents/skills/
cp /tmp/appforge/rules/AGENTS.md ./your-project/.agents/rules/AGENTS.md
```

---

## The 17 Skills

AppForge structures application development into 5 distinct phases:

### Phase 1: Discovery & Recon
| Skill | Command | What It Does |
| :--- | :--- | :--- |
| **Recon** | `/forge-recon` | Reverse-engineers target app: screens, user flows, component tree, and feature matrix from public docs, screenshots, and account usage. |
| **Entrepreneur** | `/forge-entrepreneur` | Analyzes real App Store & Trustpilot reviews to rank user complaints and establish your product's competitive angle. |

### Phase 2: Architecture & Design
| Skill | Command | What It Does |
| :--- | :--- | :--- |
| **Architect** | `/forge-architect` | Plans modern tech stack, relational PostgreSQL schema, API routes, and defines thin vertical build slices. |
| **Design** | `/forge-design` | Generates original design tokens (color roles, typography, spacing, radius) and validates WCAG contrast via bundled Python utility. |

### Phase 3: Core Implementation
| Skill | Command | What It Does |
| :--- | :--- | :--- |
| **Build** | `/forge-build` | Rebuilds the frontend screen by screen from the recon map with full state management. |
| **Backend** | `/forge-backend` | Implements authentication, database migrations, Stripe payments, background jobs, and official API integrations. |
| **Seed** | `/forge-seed` | Generates realistic, relational synthetic test data and edge-case cohorts (unicode, emojis, extreme values) to bring the app to life. |
| **AI Supercharge** | `/forge-ai` | Implements high-leverage AI features (semantic search with `pgvector`, OCR receipt/document scanning, smart categorization, streaming Copilot). |
| **Mobile** | `/forge-mobile` | Configures Progressive Web App (PWA) manifest, service workers for offline caching, and Capacitor native iOS/Android wrappers. |

### Phase 4: Quality & Validation
| Skill | Command | What It Does |
| :--- | :--- | :--- |
| **Security** | `/forge-security` | Audits PostgreSQL Row-Level Security (RLS) leaks, OWASP top 10 risks, rate-limiting, and privacy compliance (GDPR export/delete). |
| **Test** | `/forge-test` | Creates test plans, writes Playwright E2E tests, and logs reproduction steps for bugs. |
| **Diff** | `/forge-diff` | Calculates a parity score against the target app and produces layout diffs via zero-dependency image analysis. |

### Phase 5: Brand, Growth & Deployment
| Skill | Command | What It Does |
| :--- | :--- | :--- |
| **Brand** | `/forge-brand` | Generates distinct candidate names, voice guide, palette, and runs a sweep tool to eliminate any leftover competitor terms. |
| **Analytics** | `/forge-analytics` | Wires up privacy-first product telemetry (PostHog, Plausible) to track activation, referral, and paywall funnels. |
| **SEO** | `/forge-seo` | Configures dynamic OpenGraph preview cards, sitemaps, structured JSON-LD schemas, and programmatic comparison pages. |
| **Launch** | `/forge-launch` | Writes landing page copy, pricing tiers, and App Store / Google Play listings checked against store policy rules. |
| **Deploy** | `/forge-deploy` | Runs preflight gates, sets production env vars, configures custom domain DNS, and triggers live deployment. |

---

## Recommended Workflow

Each skill reads what previous skills wrote, storing structured artifacts in your project's `forge/` folder:

```
forge-recon ───────► forge-entrepreneur
     │
     ▼
forge-architect ───► forge-design
     │
     ▼
forge-build ───────► forge-backend ───► forge-seed ───► forge-ai ───► forge-mobile
                                                            │
                                                            ▼
forge-diff ◄─────── forge-test ◄─────── forge-security
     │
     ▼
forge-brand ───────► forge-analytics ─► forge-seo ────► forge-launch ─► forge-deploy
```

---

## Zero-Dependency Python Utilities

All bundled helper tools require **Python 3.8+** and use **only standard library modules**. Nothing to `pip install`:

- `skills/forge-diff/parity.py` - Parses `features.csv` and outputs weighted parity scores.
- `skills/forge-diff/imgdiff.py` - Compares original vs clone layout screenshots ignoring color variations.
- `skills/forge-design/contrast.py` - WCAG 2.1 AA/AAA contrast ratio calculator for design tokens.
- `skills/forge-entrepreneur/reviews.py` - Clusters and ranks customer review complaints by frequency and sentiment.
- `skills/forge-brand/sweep.py` - Scans your entire codebase to ensure no competitor names or logos leaked through.
- `skills/forge-launch/listing.py` - Lints app store titles, subtitles, and descriptions against character limits and store policies.
- `skills/forge-seed/seed.py` - Generates randomized relational seed records and SQL statements.

---

## Example Usage

Start in Antigravity chat by pointing the agent at an app you want to study:

```text
/forge-recon https://cal.com
```

Or trigger with natural language:
- *"I want to build a modern, clean alternative to Splitwise."*
- *"Use forge-entrepreneur to find what users hate about Notion."*
- *"Audit my database RLS policies with forge-security."*
- *"Generate realistic mock users and groups with forge-seed."*
- *"Add receipt OCR scanning using forge-ai."*

---

## Clean-Room Rules & Ethics

AppForge is designed for ethical, clean-room software development:

1. **Public Sources & User Accounts Only:** Never scrape behind paywalls, bypass authentication, or inspect private internal networks.
2. **Never Copy Code:** All code is written fresh by Antigravity to solve functional requirements.
3. **No Trademark Infringement:** Always run `forge-brand` and `sweep.py` before launching to ensure your product has a unique identity, logo, and brand name.

---

## Contributing

Contributions from the Antigravity and open-source agent community are warmly welcomed! Please check [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding skills and improvements.

---

## License & Credits

- Licensed under the **[MIT License](LICENSE)**.
- Created by **[Pradeep Landge](https://github.com/iamprabs)**.
