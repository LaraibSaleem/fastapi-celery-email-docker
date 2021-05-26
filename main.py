from fastapi import FastAPI, BackgroundTasks, UploadFile, File, Form
from starlette.responses import JSONResponse
from starlette.requests import Request
from pydantic import BaseModel, EmailStr
from typing import List
from celery_tasks import send_email

class EmailSchema(BaseModel):
    email: List[EmailStr]

app = FastAPI()


@app.post("/email")
async def add_email(e: EmailSchema):

    # use delay() method to call the celery task
    send_email.delay(e.email)

    return {"message": "Emails Sent! Thank you for your patience."}