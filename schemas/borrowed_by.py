from pydantic import BaseModel

class BorrowedBy(BaseModel):
    student_id: str
    book_code: str
    issue_date: str
    return_date: str