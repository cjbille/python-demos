# Python S3
> S3 Python Project

## Create Python Venv
```shell
# create venv
python3.14 -m venv .venv

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

## Test with Curl
```shell
curl -i -X POST \
     -H "filename: archive" \
     --data-binary @/Users/cjbille/Documents/Projects/quarkus-demos/quarkus-s3-demo/src/test/resources/archive.tar \
     http://localhost:8100/upload/s3
```