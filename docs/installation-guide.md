# Installation Guide — Agentic AI with NeqSim (Community)

This guide gets you from a fresh machine to running the public **NeqSim community
agents and skills** (thermodynamics, process simulation, flow assurance, field
development, energy systems) inside VS Code with GitHub Copilot.

Human review is always required for engineering conclusions. Agents help you
screen, organize, calculate, and draft — they do not replace engineering judgement.

---

## 1. What you are installing

Community agents and skills build on the NeqSim library and live in three public
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
- **GitHub Copilot** subscription.
- **[Visual Studio Code](https://code.visualstudio.com/)** with the **GitHub
  Copilot** and **GitHub Copilot Chat** extensions.
  - Cloud alternative: **GitHub Codespaces** (no local install needed).
- When working locally, also install:
  - **[Git](https://git-scm.com/downloads)**
  - **[Python 3.8+](https://www.python.org/downloads/)** (check *Add python.exe to PATH*)
  - **[Java (JDK)](https://adoptium.net/)** — required for NeqSim calculations and builds

You do **not** need to install Maven separately. The NeqSim repository includes
the Maven Wrapper (`mvnw` / `mvnw.cmd`).

> **Tip:** A Python virtual environment keeps the CLI isolated and avoids most
> PATH problems. The commands below create one inside the cloned repository.

---

## 3. Install (Windows, VS Code terminal)

Run these from a VS Code terminal (PowerShell) or `cmd.exe`.

### 3.1 Clone NeqSim and run the installer

```powershell
git clone https://github.com/equinor/neqsim
cd neqsim
py -3 -m venv .venv
\.\.venv\Scripts\Activate.ps1
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
neqsim doctor
```

`neqsim doctor` should finish with all required checks passing. If `neqsim` is
still not found, use `python -m neqsim_cli --help` from the activated environment
and see Troubleshooting.

### 3.2 Install the community agents into VS Code

The public community catalog requires no login or private catalog registration.
Select it explicitly so previously registered private catalogs cannot affect this
public installation:

```powershell
neqsim agent install --all --source community --vscode --force
```

- `--all --source community` installs all agents in the public community catalog.
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

Verify the exported agents and their required skills:

```powershell
neqsim agent doctor --target vscode --source community
```

Success means the install command exits with code `0` and doctor reports
`Result: PASS`. Do not use a fixed expected agent count: the public catalog grows
over time.

---

## 4. macOS / Linux equivalents

```bash
git clone https://github.com/equinor/neqsim
cd neqsim
python3 -m venv .venv
source .venv/bin/activate
./install.sh
# restart the terminal so `neqsim` is on PATH

neqsim doctor
neqsim agent install --all --source community --vscode --force
neqsim agent doctor --target vscode --source community
```

---

## 5. Use the agents in VS Code

1. Open the **Copilot Chat** panel in VS Code.
2. Type `@` to see installed agents, or reference one directly, for example:
  - `@pvt-agent` — fluid characterization and phase-behavior guidance
  - `@process-engineer-agent` — early process-engineering screening
  - `@flow-assurance-engineer-agent` — hydrate and wax margin screening
  - `@process-safety-agent` — relief and depressurization screening
  - `@asset-economics-agent` — concept-level cost and value screening
3. Describe your task in plain language. The agent selects the right skills,
   runs NeqSim calculations, and produces a draft for your review.

For agentic task-solving (task folders, notebooks, reports), the NeqSim code repo
provides the full workflow — see `AGENTS.md` and
`docs/development/TASK_SOLVING_GUIDE.md` in the cloned repo. Workspace-local core
agents such as `@solve.task` are available when that NeqSim workspace is open;
they are distinct from the globally exported community agents listed above.

---

## 6. Keeping up to date

```powershell
cd neqsim
git pull
.\install.cmd                       # refresh devtools if updated
neqsim agent install --all --source community --vscode --force
neqsim agent doctor --target vscode --source community
```

---

## 7. Troubleshooting

| Symptom | Fix |
|---------|-----|
| `neqsim` not recognized in VS Code terminal | Activate `.venv`, then fully **quit and reopen VS Code** (PATH is captured at launch). Or use `python -m neqsim_cli ...`. |
| `install.cmd` can't find Python | Install Python 3.8+ and check *Add python.exe to PATH*, then re-run. |
| PowerShell blocks `.venv` activation | Open `cmd.exe`, run `.venv\Scripts\activate.bat`, then run `install.cmd`. The installer itself is pure batch. |
| Agent install exits with code `1` | Read the final `Failed agents:` line. Re-run with `--source community` to exclude registered private catalogs, then resolve any named community failure. |
| Agents not visible in Copilot | Re-run `neqsim agent install --all --source community --vscode --force`, run `neqsim agent doctor --target vscode --source community`, then use **Developer: Reload Window** in VS Code. |
| Installation and export locations | Internal packages live under `~/.neqsim/`. VS Code user exports live under `~/.copilot/agents/` and `~/.copilot/skills/` (`%USERPROFILE%` on Windows). |

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
