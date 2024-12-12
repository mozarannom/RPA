from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def reaf_root():
    return {"Hello": "World"}

@app.get("/item")
def read_item(item_id: int, name: str = None, age: int = 0):
    return {"item_id": item_id, "name": name, "age": age}

from fastapi import Form
@app.post("/user")
async def read_user_form(name: str = Form(...), studentcode: str = Form(...), major: str = Form(...)):
    return {"msg": f"{major} {name}님 ({studentcode}) 반갑습니다."}

@app.post("/plus")
async def plus_form(num1: int=Form(...),num2:int=Form(...), num3 : int=Form(...), num4 : int= Form(...)):
    result1 = num1 + num2
    result2 = num3 + num4
    return{"msg":f"{num1} + {num2} = {result1},{num3} + {num4} = {result2}"}

from fastapi.responses import StreamingResponse
import qrcode
from io import BytesIO

@app.post("/qrcode/")
async def generate_qr(data: str = Form(...) ):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_SIZE=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    return StreamingResponse(BytesIO(img_byte_arr), media_type="image/png")

def makeXL(filename) :
    from faker import Faker
    from openpyxl import Workbook
    
    fake = Faker('ko_KR')
    wb = Workbook()
    ws = wb.active
    ws.append(['이름', '성별', '이메일', '전화번호', '주소'])
    
    for i in range(1000):
        name = fake.name()
        gender = fake.random_element(elements=('남','여'))
        email = fake.email()
        phone_number = fake.phone_number()
        address = fake.address()
        ws.append([name, gender, email, phone_number, address])
print(filename)
wb.save(filename)
@app.post("/getexcelfile/")
async def make_excel_file():
    filename = "sample.xlsx"
    save_file = "static/uploads/" + filename
    
    import os
    if os.path.exists(save_file):
        os.remove(save_file)
    
    makeXL(save_file)
    return {"filename": save_file}

wb.save('fakeinfo.xlsx')
from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level="info")

