from dataclasses import field

from email_validator import EmailNotValidError
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, validate_email, EmailStr, validator, field_validator
import psycopg2
import re

"""
FeedBack Information
====================
1. FeedBack Id : Unique Id
2. Name : User Name
3. Email Id : User mail id
4. Age : User Age
6. PhoneNumber : User Phone Number
7. Rating : User Rating
8. FeedBack Comments : 
9. Creation Date :
10. Last Updated Date

Validation
Phone Number : it contains 10 digit, all the should be number
Feedback Comment : it should not be exceeded with 35 character
User Rating : Range is 1 tp 10
Name : it contains only alphabat
Email Id : it should be valid
Age : it should be number and greater than 0

"""


def get_db_connection():
    return psycopg2.connect(
        "postgresql://postgres:ronish@localhost:5432/postgres"
    )


query = """
        CREATE TABLE IF NOT EXISTS user_feedback
        (
            feedback_id       SERIAL PRIMARY KEY,
            user_name              TEXT NOT NULL,
            email_id          TEXT NOT NULL,
            age               INTEGER CHECK (age > 0),
            phone_number      VARCHAR(15),
            rating            INTEGER CHECK (rating BETWEEN 1 AND 10),
            feedback_comments TEXT,
            created_date      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_date      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ); \
        """
con = get_db_connection()
cur = con.cursor()
cur.execute(query)
con.commit()
con.close()
print("Table created successfully")

tags_metadata = [
    {
        "name": "Feedback",
        "description": "Operations related to user feedback"
    }
]

app = FastAPI(
    title="Feedback Management API",
    description="APIs to create, view, update and delete user feedback",
    version="1.0.0",
    openapi_tags=tags_metadata,
    docs_url="/ronish",
)


class Feedback(BaseModel):
    user_name: str
    email_id: EmailStr
    age: int
    phone_number: str
    rating: int
    feedback_comments: str

    @field_validator('age')
    def age_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Age must be a positive number")
        return v

    @field_validator("rating")
    def rating_range(cls, v):
        if not (1 <= v <= 10):
            raise ValueError("Rating must be between 1 and 10")
        return v

    @field_validator("feedback_comments")
    def comment_length(cls, v):
        if len(v) > 35:
            raise ValueError("Comments length must be <= 35")
        return v

    @field_validator("user_name")
    def validate_name(cls, v):
        if not re.fullmatch(r"[A-Za-z ]+", v):
            raise ValueError("User Name must contain only alphabets and spaces")
        return v


class FeedbackCommentUpdate(BaseModel):
    feedback_comments: str

    @field_validator("feedback_comments")
    def comment_length(cls, v):
        if len(v) > 35:
            raise ValueError("Comments length must be <= 35")
        return v


"""
def validate_feedback(feed: Feedback):
    if not (1 <= feed.rating <= 10):
        raise HTTPException(status_code=460, detail="Rating must be between 1 and 10")

    if len(feed.feedback_comments) > 35:
        raise HTTPException(status_code=460, detail="Comments length must be less than 35")

def get_feedback(feed: Feedback = Depends(validate_feedback)):

    if not feed.name.isalpha():
        raise HTTPException(status_code=460, detail="Name must contain only alphabets")

"""


@app.post("/feedback/add", tags=["Feedback"])
def add_feedback(feed: Feedback):
    user_name = feed.user_name
    email_id = feed.email_id
    age = feed.age
    phone_number = feed.phone_number
    rating = feed.rating
    comments = feed.feedback_comments
    conn = None
    cursor = None

    if not feed.phone_number.isdigit() or len(feed.phone_number) != 10:
        raise HTTPException(status_code=460, detail="Phone number must be exactly 10 digits")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        insert_query = """
                       INSERT INTO user_feedback(user_name, email_id, age, phone_number, rating, feedback_comments)
                       VALUES (%s, %s, %s, %s, %s, %s)
                       RETURNING
                           feedback_id, user_name, email_id, age, phone_number, rating,
                           feedback_comments, created_date, updated_date; \
                       """

        cursor.execute(
            insert_query,
            (
                user_name,
                email_id,
                age,
                phone_number,
                rating,
                comments
            )
        )

        inserted_row = cursor.fetchone()
        conn.commit()

        return {
            "feedback_id": inserted_row[0],
            "user_name": inserted_row[1],
            "email": inserted_row[2],
            "age": inserted_row[3],
            "phone_number": inserted_row[4],
            "rating": inserted_row[5],
            "feedback_comments": inserted_row[6],
            "created_date": inserted_row[7],
            "updated_date": inserted_row[8],
            "code":200,
            "status": "Feedback created Successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@app.get("/feedback/getAll", tags=["Feedback"])
def get_all_feedback():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
                select *
                from user_feedback \
                """
        cursor.execute(query)
        feedback = cursor.fetchall()

        result = []
        for row in feedback:
            result.append({
                "feedback_id": row[0],
                "user_name": row[1],
                "email": row[2],
                "age": row[3],
                "phone_number": row[4],
                "rating": row[5],
                "feedback_comments": row[6],
                "created_date": row[7],
                "updated_date": row[8],
            })

        return {
            "message": "Get all the Feedback",
            "code": 200,
            "count": len(result),
            "data": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@app.get("/feedback/{feedback_id}", tags=["Feedback"])
def get_feedback(feedback_id: int):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
                SELECT *
                from user_feedback
                WHERE feedback_id = %s
                ; \
                """
        cursor.execute(query, (feedback_id,))
        feedback = cursor.fetchone()

        if not feedback:
            raise HTTPException(status_code=404, detail="Feedback Not Found")

        return {
            "status": "Feedback fetched Successfully",
            "user_name": feedback[1],
            "email": feedback[2],
            "age": feedback[3],
            "phone_number": feedback[4],
            "rating": feedback[5],
            "feedback_comments": feedback[6],
            "created_date": feedback[7],
            "updated_date": feedback[8],
            "code": 200
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
@app.delete("/feedback/{feedback_id}", tags=["Feedback"])
def delete_feedback(feedback_id: int):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
                DELETE
                from user_feedback
                WHERE feedback_id = %s; \
                """
        cursor.execute(query, (feedback_id,))
        conn.commit()
        record = cursor.rowcount

        if record == 0:
            raise HTTPException(status_code=404, detail="Feedback not found")

        return {
            "status": "Feedback deleted Successfully",
            "record": record,
            "code": 200
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


@app.patch("/feedback/comment/{feedback_id}", tags=["Feedback"])
def update_feedback_comment(feedback_id: int, data: FeedbackCommentUpdate):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
                SELECT feedback_comments,user_name
                from user_feedback
                WHERE feedback_id = %s; \
                """
        cursor.execute(query, (feedback_id,))
        feedback = cursor.fetchone()
        if feedback is None:
            raise HTTPException(status_code=404, detail="Feedback not found")

        update_query = """
                   UPDATE user_feedback
                   SET feedback_comments = %s, updated_date = CURRENT_TIMESTAMP
                   where feedback_id = %s; \
                   """
        cursor.execute(update_query, (data.feedback_comments, feedback_id))
        conn.commit()
        record = cursor.rowcount
        return {
            "status": "Feedback Updated Successfully",
            "user_name": feedback[1],
            "old Feedback": feedback[0],
            "new Feedback": data.feedback_comments,
            "code": 200
         }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

