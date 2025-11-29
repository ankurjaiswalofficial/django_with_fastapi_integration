# django-with-fastapi-integration

Unified **Django + FastAPI** project running under a single **ASGI** application using **Granian** and managed with **UV** and **Taskipy**.

This guide explains how to set up the project cleanly on **Linux**, **macOS**, and **Windows**, using the fastest Python toolchain available.

---

# **1. Install UV (Required)**

UV replaces Poetry/pipenv/virtualenv and provides extremely fast installs & isolated envs.

### **Linux / macOS**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### **Windows (PowerShell)**

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

Verify installation:

```bash
uv --version
```

---

# **2. Create & Activate the Virtual Environment**

Inside your project folder:

```bash
uv venv
```

Activate the venv:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows (PowerShell)

```powershell
.venv\Scripts\activate
```

---

# **3. Install Dependencies**

```bash
uv sync
```

This installs all project + dev dependencies defined in `pyproject.toml`.

---

# ⚙**4. Project Commands (Taskipy)**

All commands are defined in:

```
[tool.taskipy.tasks]
```

Run any task using:

```bash
uv run <task>
```

### **Available Commands**

| Task                    | Description                                      |
| ----------------------- | ------------------------------------------------ |
| `uv run dev`            | Run Granian ASGI server (Django + FastAPI)       |
| `uv run django`         | Run Django default dev server                    |
| `uv run uv`             | Run ASGI via Uvicorn                             |
| `uv run makemigrations` | Create new migrations                            |
| `uv run migrate`        | Apply migrations                                 |
| `uv run collectstatic`  | Collect static files                             |
| `uv run setup`          | Run all Django setup steps (migrations + static) |

---

# **5. Start Development Servers**

### **Option A — Full ASGI (Granian)**

(Recommended for combined Django + FastAPI routes)

```bash
uv run dev
```

### **Option B — Django only**

```bash
uv run django
```

### **Option C — ASGI via Uvicorn**

```bash
uv run uv
```

---

# **6. Database Operations**

### Create migrations:

```bash
uv run makemigrations
```

### Apply migrations:

```bash
uv run migrate
```

---

# **7. Static Files**

```bash
uv run collectstatic
```

---

# **8. Full Project Setup**

Run all essential setup commands:

```bash
uv run setup
```

This will:

1. Generate migrations
2. Apply migrations
3. Collect static files

---

# **9. Project Structure Overview**

```
poc-django-with-fastapi/
│ pyproject.toml
│ README.md
│ manage.py
│
├── config/
│   ├── asgi.py
│   ├── settings.py
│   └── urls.py
│
└── app(s) …
```

Django + FastAPI are unified inside `config/asgi.py`.

---

# **10. Notes**

* Python **3.10–3.12** recommended
* Granian currently **does not support Python 3.13**
* UV automatically handles the virtual environment & installation
* Taskipy provides clean, simple npm-style commands

___
### How FastAPI is integrated with Django:

The project runs FastAPI and Django together inside a single ASGI application using Granian. The integration is implemented in three places:

1. FastAPI app creation (`config/fastapi_init.py`)
   - A `FastAPI()` instance (usually named `app`) is created.
   - Application routers from `apps/core/api/routers.py` are included into that FastAPI instance using `app.include_router(...)`.

2. API code (`apps/core/api/routers.py` and `apps/core/api/schemas.py`)
   - Routes and endpoints live in `apps/core/api/routers.py`.
   - Pydantic request/response models are defined in `apps/core/api/schemas.py`.

3. ASGI composition (`config/asgi.py`)
   - Django's ASGI application is obtained with `django.core.asgi.get_asgi_application()`.
   - The FastAPI `app` from `config/fastapi_init.py` is imported.
   - Granian is used to compose both ASGI apps so they run under one process. This makes FastAPI endpoints available alongside Django views.

How to run
- `uv run dev` starts the combined ASGI app (Django + FastAPI) via Granian.
- `uv run django` runs Django-only.
- `uv run uv` runs the ASGI app via Uvicorn.

Quick reference — files to inspect
- `config/fastapi_init.py` \- creates and configures the FastAPI app.
- `apps/core/api/routers.py` \- FastAPI routes.
- `apps/core/api/schemas.py` \- Pydantic schemas.
- `config/asgi.py` \- composes Django and FastAPI apps with Granian.

Typical code patterns (see the actual files for exact code):
- In `config/fastapi_init.py` you will see a `FastAPI()` instance and `app.include_router(...)` calls to register application routes.
- In `config/asgi.py` you will see imports of Django's `get_asgi_application()`, the FastAPI `app`, and Granian being used to create the unified ASGI app.

Check those files directly for the exact prefixes and Granian call used in this project.

# Done!

Your Django + FastAPI hybrid project is now fully configured using **UV**, **Taskipy**, and **Granian** for a modern, high-performance development experience.
