Project Setup Details


Git Hooks
check-for-migrations.sh
A pre-push Git hook script used to check for Django migration files before pushing code to GitHub. This helps ensure that all necessary database schema changes are included.

.pre-commit-config.yaml
Configuration file for pre-commit hooks. It is used to:

Format Python code

Remove trailing whitespaces

Eliminate unused imports

Docker Files
Dockerfile
A text file containing instructions to build a Docker image for the application.

docker-compose.yml
A configuration file used to define and run multi-container Docker applications. Useful when your project includes multiple services (e.g., web server, database, etc.).
