# Python Demos
> A project consisting of Python demos

## Create Python Venv
```shell
# cd to individual project
cd <project name>

# create venv
python3 -m venv .venv

# activate venv
source .venv/bin/activate

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
