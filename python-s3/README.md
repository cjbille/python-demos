# Python S3
> S3 Python Project

## Create Python Venv
```shell
# create venv
python3 -m venv .venv

# activate venv
source .venv/bin/activate

# upgrade pip
pip install --upgrade pip

# leave venv
deactivate
```

## Install Dependencies
```shell
# dependencies + dev dependencies
pip install -e ".[dev]"

# prod only dependencies
pip install .
```

## Test
```shell
pytest
```