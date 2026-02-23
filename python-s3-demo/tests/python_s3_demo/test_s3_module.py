from fastapi.testclient import TestClient

# 1. Create the FastAPI test client (like Java's MockMvc)
client = TestClient(app)

# 2. Setup standard fake AWS credentials to prevent accidental live uploads
@pytest.fixture(scope="function")
def aws_credentials():
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
    os.environ["S3_BUCKET"] = "test-bucket"

# 3. Create the fake S3 bucket in RAM before the test runs
@pytest.fixture(scope="function")
def s3_mock(aws_credentials):
    with mock_aws():
        # Create a real boto3 client, but it talks to Moto!
        s3 = boto3.client("s3", region_name="us-east-1")
        # We must create the bucket in the fake AWS account first
        s3.create_bucket(Bucket="test-bucket")
        yield s3

# 4. The actual test
def test_successful_s3_upload(s3_mock):
    # The dummy file content
    fake_file_content = b"Hello, this is a fake tar file!"

    # Send the fake HTTP POST request
    response = client.post(
        url="/upload/s3",
        content=fake_file_content,
        headers={"filename": "my-test-file.tar"} # Our custom header!
    )

    # Assert the HTTP response
    assert response.status_code == 202
    assert response.json() == {"message": "Upload accepted"}

    # Assert the file ACTUALLY made it into the fake S3 bucket
    saved_object = s3_mock.get_object(Bucket="test-bucket", Key="my-test-file.tar")
    saved_body = saved_object["Body"].read()

    assert saved_body == fake_file_content
