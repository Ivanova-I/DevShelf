# DevShelf

A personal developer learning library, built as a Django Basics exam project.

DevShelf helps you organize development resources (articles, videos, courses,
documentation, books) by technology, group them into structured learning paths,
keep notes tied to the resources you're studying, and track your progress.

## What makes DevShelf original

Most bookmark tools only store links. DevShelf connects the whole learning
process: a resource belongs to a technology and carries tags, resources are
grouped into learning paths with a calculated total study time, every user
keeps personal notes on a resource, and a personal progress record shows what
is not started, in progress or completed.

## Features

- **Resource library**: browse resources, filter them by technology and sort
  them by title, rating or duration
- **Embedded videos**: YouTube resources play directly on the detail page
  through a custom template filter
- **Technologies and tags**: organize resources around what you're learning
- **Learning paths**: group resources into a structured sequence; the detail
  page shows the total study time, calculated from the resources by a custom
  template tag
- **Short resources**: resources of 15 minutes or less get a "Short" badge
- **Progress tracking**: mark any resource as not started, in progress or
  completed from its detail page
- **My Learning**: a personal page listing the resources you have started or
  finished, with the latest activity first
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
| `resources` | Resources, notes and progress, plus the `resource_extras` template filter and tag |
| `learning` | Learning paths |
| `accounts` | Registration and login |

Shared templates live in the top-level `templates/` folder. Reusable partials
(`resource_card.html`, `form_actions.html`) are in `templates/partials/`.

## Code overview

- **Models**: `Resource` (many-to-one to `Technology`, many-to-many to `Tag`),
  `Note`, `Progress` (with a unique constraint per user and resource),
  `Technology`, `Tag` and `LearningPath` (many-to-many to `Resource`).
  `Resource` has a default ordering and an `is_short` property.
- **Forms**: model forms with custom labels, help texts, placeholders and error
  messages, field-level validation (`clean_` methods), and a disabled field in
  the note edit form.
- **Views**: function-based views with redirects after saving, delete
  confirmation pages, and handling of protected deletions (a technology, tag or
  resource that is still in use cannot be deleted).
- **Templates**: one base template, reusable partials included with
  `{% include %}`, built-in filters, and a custom filter and tag in
  `resources/templatetags/resource_extras.py`:
  - `youtube_video` (filter) converts a YouTube link into an embeddable address
  - `path_total_time` (tag) adds up the minutes of a learning path's resources

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
2. Create a **Tag** and a **Technology** from the Catalog pages.
3. Create a **Resource**. It needs a technology and at least one tag.
4. Open the resource and use the progress buttons to mark it as in progress or
   completed. Your resources are listed on the **My Learning** page.
5. Create a **Learning Path** and add resources to it.
6. Create a **Note** for a resource. Notes can only be edited or deleted by
   their author.

Anonymous visitors can browse the catalog, resources and learning paths but
cannot change anything. Progress tracking and My Learning need a login.

The Django admin is optional. To use it, create a superuser:

```bash
python manage.py createsuperuser
```

## Custom 404 page

The custom 404 page is shown only when `DEBUG = False` in `settings.py`. With
`DEBUG = True` (the default in this project) Django shows its own debug 404
page instead. To see the custom page, set `DEBUG = False`, make sure
`ALLOWED_HOSTS` contains `127.0.0.1`, and start the server with
`python manage.py runserver --insecure` so that the stylesheet is still served.

## Author

Created by Iva Ivanova as a Django Basics course exam project.