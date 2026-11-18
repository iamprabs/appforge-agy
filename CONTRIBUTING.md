# Contributing to AppForge

Thank you for your interest in contributing to **AppForge for Antigravity**!

AppForge is an open-source suite of skills designed to help Antigravity developers reverse-engineer, architect, build, AI-supercharge, test, rebrand, and deploy clean-room software.

---

## Design Principles

1. **Clean-Room Development Only:**
   AppForge rebuilds *what an app does, never what it owns*. No skills should ever encourage scraping copyrighted code, downloading proprietary assets, bypass auth protections, or copying trademarked brand identity.
2. **Zero-Dependency Python Tools:**
   All Python utilities bundled in `skills/` must use the Python Standard Library only (`sys`, `json`, `urllib`, `random`, `re`, `argparse`, etc.). Users should not need to run `pip install` to use any tool.
3. **Antigravity-First:**
   Ensure all `SKILL.md` frontmatters include valid `name` and descriptive `description` blocks optimized for Antigravity progressive disclosure.
4. **Resilient Defaults:**
   Scripts should gracefully handle missing files, empty lines, and UTF-8 characters across Windows, macOS, and Linux.

---

## Adding a New Skill

1. Create a new directory under `skills/forge-<skill-name>/`.
2. Add a `SKILL.md` file with YAML frontmatter:
   ```markdown
   ---
   name: forge-<name>
   description: >-
     A concise explanation of when Antigravity should trigger this skill.
   ---
   ```
3. Document the step-by-step procedure and clear inputs/outputs.
4. If the skill uses a helper script, write a standalone Python script in the skill folder.
5. Update `rules/AGENTS.md`, `plugin.json`, and `README.md` to reference the new skill.

---

## Submitting Pull Requests

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/amazing-skill`).
3. Commit your changes with clear messages (`git commit -m 'feat(skill): add forge-cache'`).
4. Push to your branch (`git push origin feature/amazing-skill`).
5. Open a Pull Request with a clear description and testing evidence.
