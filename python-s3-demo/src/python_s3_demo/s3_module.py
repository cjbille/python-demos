import io
import logging
import os
import uuid
from typing import Annotated

import boto3
import uvicorn
from fastapi import FastAPI, Request, Header, status, HTTPException
from fastapi.concurrency import run_in_threadpool

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

APPLICATION_TAR = "application/x-tar"
S3_BUCKET = os.getenv("S3_BUCKET", "coffee")

s3_client = boto3.client("s3")

app = FastAPI()

@app.post("/upload/s3", status_code=status.HTTP_202_ACCEPTED)
async def upload_file(request: Request, file_name_header: Annotated[str | None, Header(alias="filename")] = None):
    file_name = build_file_name(file_name_header)
    try:
        logger.info(f"Received filename: {file_name}")
        body_bytes = await request.body()
        file_obj = io.BytesIO(body_bytes)
        def s3_upload_task():
            s3_client.upload_fileobj(
                Fileobj=file_obj,
                Bucket=S3_BUCKET,
                Key=file_name,
                ExtraArgs={"ContentType": APPLICATION_TAR}
            )
        await run_in_threadpool(s3_upload_task)
        return {"message": "Upload accepted"}
    except Exception as e:
        logger.error(f"FAIL | fileName={file_name} | exception={e.__class__.__name__} | message={str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred during the upload."
        )

def build_file_name(header_name: str | None) -> str:
    file_name = header_name if header_name else str(uuid.uuid4())
    return f"{file_name}.tar"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8100)
