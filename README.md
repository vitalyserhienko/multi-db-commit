SQLAlchemy 1.4 [Enabling Two-Phase Commit](https://docs.sqlalchemy.org/en/14/orm/session_transaction.html#enabling-two-phase-commit) PoC

### Setup

```bash
pip install -r requirements.txt
```

- to run two DBs:
```bash
make run
```
- to clean DBs:
```bash
make clean
```

- to stop DBs:

```bash
make stop
```

- DDLs:

```bash
python init_schema.py --help
```

- The script:

```bash
python main.py --help
```

### Break schema
:warning: required for 1st strategy (combined session)

This command will create different schema for Account (`name` replaced with `full_name`) in second database. When you try to commit regular Account with field `name` it'll throw an error because `account` table does not have such column.
```
python init_schema.py --break-schema
```

### Flow example

#### Happy path :white_check_mark:
- for first run
```bash
make run
```
- if it's already been run
```bash
make clean
python init_schema.py
python main.py --strategy 1
```

#### Error case :x:

- for first run
```bash
make run
```
- if it's already been run
```bash
make clean
python init_schema.py --break-schema
python main.py --strategy 1
```