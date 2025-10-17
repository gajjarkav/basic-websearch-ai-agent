from pydantic import BaseModel, EmailStr, Field

class SendMailSchema(BaseModel):
    to_email: EmailStr = Field(description="The recipient's email address.")
    subject: str = Field(description="The subject line of the email.")
    body: str = Field(description="The content/body of the email.")