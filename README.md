# DevShelf

A personal developer learning library, built as a Django Basics exam project.

DevShelf helps you organize development resources (articles, videos, courses,
documentation, books) by technology, group them into structured learning paths,
and keep notes tied to the resources you're studying.

## Features

- **Resource library**: browse, filter and sort resources by technology,
  difficulty and rating
- **Embedded videos**: YouTube resources play directly on the detail page
  through a custom template filter
- **Technologies and tags**: organize resources around what you're learning
- **Learning paths**: group resources into a structured sequence
- **Notes**: personal notes tied to specific resources, editable only by
  their author
- **User accounts**: register, log in and log out
- **Dark / light theme toggle**, with the choice remembered between visits
- **Custom 404 page**

## Tech stack

- Python, Django 6.1.1
- SQLite
- Vanilla HTML, CSS and JavaScript, with no frontend framework

## Project structure

| App | Responsibility |
|---|---|
| `catalog` | Technologies and tags |
| `resources` | Resources and notes, plus the `resource_extras` template filters |
| `learning` | Learning paths |
| `accounts` | Registration and login |

## Setup

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/Ivanova-I/DevShelf.git
cd DevShelf
python -m venv .venv
.venv\Scripts\activate         # Windows
# source .venv/bin/activate    # macOS / Linux
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Apply the migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
```

The site is available at `http://127.0.0.1:8000/`.

### Environment variables and credentials

None are required. The project runs with its default settings and an SQLite
database file that is created by `migrate`.

## Using the app

The database starts empty and no admin access is needed.

1. Click **Register** in the navigation and create an account. Registered
   users can create, edit and delete content.
2. Create a **Technology** from the Catalog page.
3. Create a **Resource**, which needs a technology, and optionally add tags.
4. Create a **Learning Path** and add resources to it.
5. Create a **Note** for a resource. Notes can only be edited or deleted by
   their author.

Anonymous visitors can browse every page but cannot change anything.

The Django admin is optional. To use it, create a superuser:

```bash
python manage.py createsuperuser
```

## Author

Created by Iva Ivanova as a Django Basics course exam project.