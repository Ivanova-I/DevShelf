# DevShelf

A personal developer learning library — built as a Django exam project.

DevShelf helps you organize development resources (articles, videos, courses,
documentation) by technology, group them into structured learning paths, and
keep notes tied to the resources you're studying.

## Features

- **Resource library** — browse, filter, and sort resources by technology,
  difficulty, and rating
- **Technologies & tags** — organize resources around what you're actually
  learning
- **Learning paths** — group resources into a structured sequence
- **Notes** — personal notes tied to specific resources, visible only to
  their author
- **User accounts** — register, log in, and manage your own notes and
  learning progress
- **Dark / light theme toggle**, with the choice remembered between visits
- **Role-based permissions** — shared library content (resources,
  technologies, learning paths) can only be created or edited by staff;
  notes can only be edited by the user who wrote them

## Tech stack

- Python, Django 6.1.1
- SQLite (development database)
- Vanilla HTML/CSS/JS — no frontend framework

## Setup

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/Ivanova-I/DevShelf.git
cd DevShelf
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate   # macOS/Linux
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations and run the development server:

```bash
python manage.py migrate
python manage.py runserver
```

The site will be available at `http://127.0.0.1:8000/`.

To access the Django admin, create a superuser first:

```bash
python manage.py createsuperuser
```

## Author

Created by Iva Ivanova as a Django Basics course exam project.