# Practical 10 — Ruby on Rails Task Board
**Aim:** Create a task-list web app demonstrating Rails MVC, routes, forms, validation, and database persistence.

Requirements: Ruby, Rails 7.1-compatible environment, and SQLite3.

## Important setup note
This folder contains the application-specific files, not all Rails-generated boilerplate. Create a full Rails shell first, then copy these files into it:

```bash
rails new task_board -d sqlite3
cd task_board
```

Copy this folder's `Gemfile`, `config/routes.rb`, `app/models/task.rb`, `app/controllers/tasks_controller.rb`, `app/views/layouts/application.html.erb`, `app/views/tasks/index.html.erb`, and migration file into the corresponding paths in the generated app. Then run:

```bash
bundle install
bin/rails db:migrate
bin/rails server
```

Open `http://localhost:3000`. If the generated app uses a newer Rails version, retain its generated Gemfile and migration version, and adapt the provided files as needed.
