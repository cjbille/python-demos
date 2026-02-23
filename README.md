# Python Demos
> A project consisting of Python projects related so AWS and serverless

## Create Python Venv
```shell
# cd to individual project
cd <project-name>

# create venv
python3.14 -m venv .venv

# upgrade pip
pip install --upgrade pip

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
