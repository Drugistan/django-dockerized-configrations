#!/bin/bash

# Get list of staged files
STAGED_FILES=$(git diff --cached --name-only)

# Check if any models.py file was modified
MODELS_CHANGED=$(echo "$STAGED_FILES" | grep -E "models\.py")

# Check if any migration file was added
MIGRATIONS_ADDED=$(echo "$STAGED_FILES" | grep -E "migrations/.*\.py" | grep -v "__init__.py")

if [[ -n "$MODELS_CHANGED" && -z "$MIGRATIONS_ADDED" ]]; then
  echo "❌ You have modified a models.py file but didn't add a migration."
  echo "➡️ Please run: python manage.py makemigrations"
  exit 1
fi

exit 0
