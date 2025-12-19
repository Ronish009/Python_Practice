from fastapi import FastAPI,Path,UploadFile,File,HTTPException,Form
from typing import Union, Annotated

from fastapi.params import Body
from pydantic import BaseModel,Field

class Item(BaseModel):
    name: str
    rank: int
    is_indian: Union[bool, None] = None

class stud(BaseModel):
    student_name: str
    student_id: int
    marks: int = Field(gt=0, le=100,description="The marks needs to be less than 100")
    language: str | None = Field(default=None,description="The language of Student is", max_length=20)

student =[{"student_name":"ronish", "student_id":1,"marks":90,"language":"python"},
          {"student_name":"sumit", "student_id":2,"marks":98,"language":"java"},
          {"student_name":"arghyadip", "student_id":3,"marks":80,"language":"golang"},
          {"student_name":"madhu", "student_id":4,"marks":81,"language":"c"}]
app= FastAPI()
"""
@app.get("/")
def read_root():
    return {"Welcome": "Ronish"}
    
@app.get("/{item}")
def read_root(item:int, q:Union[str,None]=None):
    return {"item_id": item, "q": q}

@app.put("/{item}")
def update_root(item:int, it:Item):
    return {"item": item, "name": it.name}
  
"""


@app.get("/student/getall")
def get_all_student():
    #get all the student
    return student

@app.get("/student/{student_id}")
def get_student_by_id(student_id:Annotated[int,Path(title="Student Id", gt=0, lt=100)]):
    #get all the student
    for s in student:
        if s["student_id"] == student_id:
            return s
    return {"error": "Student not found"}


@app.put("/student/{student_id}")
def update_student(student_id:int,student_name:str):
    #get all the student
    for s in student:
        if s["student_name"].casefold() == student_name.casefold():
            s["student_id"] = student_id
            return s
    return {"error": "Student not found"}

@app.post("/student")
def add_student(new:stud):
    #get all the student
    student.append(new.model_dump())
    return new

@app.delete("/student/{student_name}")
def delete_student(student_name:str):
    #get all the student
    for i in range(len(student)):
        if student[i]["student_name"].casefold()==student_name.casefold():
            s=student.pop(i)
            return s
    #return {"error": "Student not found"}
    raise HTTPException(status_code= 402, detail= "Name not Found")
@app.post("/File/")
def file_length(file: Annotated[bytes,File()]):
    return {"File Length":len(file)}


@app.post("/File_Details/")
def file_length(file: UploadFile):
    return {"filename": file.filename , "content_type" : file.content_type}

@app.post("/processfile")
async def process_file_data(file: UploadFile):
    s= await file.read()
    return {"File Content":s}

@app.post("/question/")
async def get_answer(
    Temperature: int,
    max_length: int,
    prompt: Annotated[str, Body()],
    user_file: Annotated[UploadFile, File(description="A file read as UploadFile")]
):
    return {
        "temperature": Temperature,
        "max_length": max_length,
        "prompt": prompt,
        "filename": user_file.filename
    }


@app.post("/upload/")
async def upload_file(
    username: Annotated[str, Form()],
    file: Annotated[UploadFile, File()]
):
    content = await file.read()

    return {
        "username": username,
        "filename": file.filename,
        "file_size": len(content)
    }

