# Installation Guide — Agentic AI with NeqSim (Community)

This guide gets you from a fresh machine to running the public **NeqSim community
agents and skills** (thermodynamics, process simulation, flow assurance, field
development, energy systems) inside VS Code with GitHub Copilot.

Human review is always required for engineering conclusions. Agents help you
screen, organize, calculate, and draft — they do not replace engineering judgement.

---

## 1. What you are installing

Community agents and skills build on the NeqSim library and live in two public
repositories:

| Repository | What it holds |
|------------|---------------|
| [equinor/neqsim](https://github.com/equinor/neqsim) | **NeqSim library + code repo.** Contains the `neqsim` CLI installer. |
| [equinor/neqsim-community-agents](https://github.com/equinor/neqsim-community-agents) | **Community agents** — reusable engineering assistants. |
| [equinor/neqsim-community-skills](https://github.com/equinor/neqsim-community-skills) | **Community skills** — reusable engineering methods. |

**Dependency direction:** `NeqSim core → core skills → community skills → community agents`.
Higher layers may use lower ones; never the reverse.

> **Enterprise use:** companies can build their own private **enterprise agent and
> skill pages** on top of these public repositories — adding organization-specific
> integrations, data sources, and governance — while reusing every community skill
> and agent. Keep company-specific detail in those private repositories and keep
> community content generic and plant-agnostic. See the
> [Enterprise Agent and Skill Repositories guide](https://github.com/equinor/neqsim/blob/master/docs/integration/enterprise_agent_skill_repos.md).

---

## 2. Prerequisites

Install these tools (the ones referenced in the *Tools used in this workflow* slide):

- **GitHub account.**
- **GitHub Copilot** subscription with access to a modern LLM (e.g. GPT‑5.x,
  Claude 4.x, or Gemini 3).
- **[Visual Studio Code](https://code.visualstudio.com/)** with the **GitHub
  Copilot** and **GitHub Copilot Chat** extensions.
  - Cloud alternative: **GitHub Codespaces** (no local install needed).
- When working locally, also install:
  - **[Git](https://git-scm.com/downloads)**
  - **[Python 3.8+](https://www.python.org/downloads/)** (check *Add python.exe to PATH*)
  - **[Java (JDK)](https://adoptium.net/)** — required to run NeqSim
  - **[Maven](https://maven.apache.org/download.cgi)** — for building NeqSim from source

> **Tip:** A Python virtual environment avoids most PATH problems (see Troubleshooting).

---

## 3. Install (Windows, VS Code terminal)

Run these from a VS Code terminal (PowerShell) or `cmd.exe`.

### 3.1 Clone NeqSim and run the installer

```powershell
git clone https://github.com/equinor/neqsim
cd neqsim
.\install.cmd
```

`install.cmd` is a pure-batch installer (works on locked-down machines where
PowerShell script execution is blocked). It finds a working Python, installs the
NeqSim **devtools** package, and puts the `neqsim` command on your PATH.

**Restart your terminal now** — PATH changes only apply to newly opened terminals.
In VS Code, fully **quit and reopen** VS Code (a new integrated terminal alone is
not enough, because VS Code captures PATH at launch).

Verify the CLI:

```powershell
neqsim --help
```

If `neqsim` is still not found, use `python -m neqsim_cli --help` and see Troubleshooting.

### 3.2 Install the community agents into VS Code

The public community catalog is used by default — no login or private catalog
registration is required.

```powershell
neqsim agent install --all --vscode --force
```

- `--all` installs all community agents.
- `--vscode` exports them so they appear in **GitHub Copilot Chat**.
- Installing an agent **automatically installs the skills** it declares in
  `required_skills` — so a separate skill-install step is not needed for the
  agent workflow.
- `--force` overwrites existing exports (safe to re-run after updates).

Browse and install individually:

```powershell
neqsim agent list                       # list available community agents
neqsim skill list                       # list available community skills
neqsim agent install <name> --vscode    # install a single agent
neqsim skill install <name> --vscode    # install a single skill (standalone)
```

---

## 4. macOS / Linux equivalents

```bash
git clone https://github.com/equinor/neqsim
cd neqsim
./install.sh
# restart the terminal so `neqsim` is on PATH

neqsim agent install --all --vscode --force
```

---

## 5. Use the agents in VS Code

1. Open the **Copilot Chat** panel in VS Code.
2. Type `@` to see installed agents, or reference one directly, for example:
   - `@solve.task` — end-to-end engineering task solving with a report
   - `@thermo.fluid` — build thermodynamic fluids and phase envelopes
   - `@process.model` — build and run process simulations
   - `@flow.assurance` — hydrate / wax / corrosion / pipeline screening
   - `@pvt.simulation` — PVT lab tests (CME, CVD, separator tests)
3. Describe your task in plain language. The agent selects the right skills,
   runs NeqSim calculations, and produces a draft for your review.

For agentic task-solving (task folders, notebooks, reports), the NeqSim code repo
provides the full workflow — see `AGENTS.md` and
`docs/development/TASK_SOLVING_GUIDE.md` in the cloned repo.

---

## 6. Keeping up to date

```powershell
cd neqsim
git pull
.\install.cmd                       # refresh devtools if updated
neqsim agent install --all --vscode --force   # re-export latest agents + skills
```

---

## 7. Troubleshooting

| Symptom | Fix |
|---------|-----|
| `neqsim` not recognized in VS Code terminal | Fully **quit and reopen VS Code** (PATH is captured at launch). Or use `python -m neqsim_cli ...`. A Python virtualenv avoids this. |
| `install.cmd` can't find Python | Install Python 3.8+ and check *Add python.exe to PATH*, then re-run. |
| PowerShell blocks scripts (execution policy) | Use `install.cmd` (pure batch — no PowerShell needed). |
| Agents not visible in Copilot | Re-run `neqsim agent install --all --vscode --force` and reload VS Code. |
| Catalog location | Installed agents/skills live under `~/.neqsim/` (`%USERPROFILE%\.neqsim\` on Windows). |

---

## 8. Governance & safety

- Agents orchestrate approved **skills**; engineering methods live in skills, not
  in agent definitions.
- Keep community content generic and plant-agnostic; company-specific detail
  belongs in private enterprise repositories.
- All engineering conclusions, and any decision affecting assets, people,
  environment, or production, **require human review**.

---

## 9. References

- NeqSim library & code repo — <https://github.com/equinor/neqsim>
- Community agents — <https://github.com/equinor/neqsim-community-agents>
- Community skills — <https://github.com/equinor/neqsim-community-skills>
- Enterprise agent & skill repositories guide — <https://github.com/equinor/neqsim/blob/master/docs/integration/enterprise_agent_skill_repos.md>
