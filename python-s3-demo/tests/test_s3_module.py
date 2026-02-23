import os

os.environ["AWS_ACCESS_KEY_ID"] = "test-access-key-id"
os.environ["AWS_SECRET_ACCESS_KEY"] = "test-secret-access-key"
os.environ["AWS_SECURITY_TOKEN"] = "test-security-token"
os.environ["AWS_SESSION_TOKEN"] = "test-session-token"
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
os.environ["S3_BUCKET"] = "coffee"

import boto3
import pytest
from fastapi.testclient import TestClient
from moto import mock_aws
from python_s3_demo import s3_module
from python_s3_demo.s3_module import app

client = TestClient(app)

@pytest.fixture(scope="function")
def s3_mock():
    with mock_aws():
        mock_s3_client = boto3.client("s3", region_name="us-east-1")
        mock_s3_client.create_bucket(Bucket="coffee")
        s3_module.s3_client = mock_s3_client
        yield mock_s3_client

def test_upload_file_valid_tar_returns_202(s3_mock):
    mock_file_content = "Hello, this is a mock tar file!".encode("utf-8")
    response = client.post(
        url="/upload/s3",
        content=mock_file_content,
        headers={"filename": "mock-test-file"}
    )
    assert response.status_code == 202
    assert response.json() == {"message": "Upload accepted"}
    saved_object = s3_mock.get_object(Bucket="coffee", Key="mock-test-file.tar")
    saved_body = saved_object["Body"].read()
    assert saved_body == mock_file_content
