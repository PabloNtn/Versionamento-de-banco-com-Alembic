# Database version control - FastAPI + SQLModel + Alembic
 

# Alembic

## Init
    alembic init <schemaname>

## Config


```[alembic.ini]
sqlalchemy.url = sqlite:///db_dq_dev.db
version_table = dq_alembic_version
```

## Create revision
    alembic revision -m "<message>"

## Changes env.py
    from sqlmodel import SQLModel
    target_metadata = SQLModel.metadata

## Changes alembic.ini
SQLModel.metadata -env, sqlalchemy.url = postgres://user:password@host:port/database?option=value

## Apply the migration:

    alembic upgrade head

## Downgrade the migration
    alembic downgrade head

## Migration version history
    alembic history --verbose



# Referencias

https://testdriven.io/blog/fastapi-sqlmodel/#alembic
https://alembic.sqlalchemy.org/en/latest/
