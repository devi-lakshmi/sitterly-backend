## Getting Started

Start Postgres on port 5446 in a Docker container called `sitterdb`.

```bash
$ docker run --name sitterdb -d -p 5446:5432 -e POSTGRES_PASSWORD=secret postgres
```

Init and activate your virtual environment

```bash
$ python -m venv .venv
$ source .venv/bin/activate
```

Install the dependencies

```bash
$ pip install pipenv
$ pipenv install
```

Create your `.env` file

```bash
# .env
DATABASE_URL=postgresql://postgres:secret@localhost:5446/postgres
# Generate a new secret with `openssl rand -hex 32`
JWT_SECRET_KEY=271d3260a43e49d2be57499a530c55e0029618f33d2342862a7cb636624e9db3
```

Now, run the migrations

```bash
$ pipenv run alembic revision --autogenerate -m "First revision"
$ pipenv run alembic upgrade head
```

That's it!
