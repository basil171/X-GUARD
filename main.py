from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import httpx

app = FastAPI(docs_url=None, redoc_url=None)  # إلغاء Swagger وRedoc

# ملفات CSS/JS/images
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/scan")
async def scan_api(
    api_url: str = Form(...),
    auth_type: str = Form(...),
    auth_token: str = Form(""),
    scan_type: str = Form(...)
):
    headers = {}
    # دعم أنواع التوثيق
    if auth_type.lower() == "token" and auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"
    elif auth_type.lower() == "basic" and auth_token:
        headers["Authorization"] = f"Basic {auth_token}"

    try:
        async with httpx.AsyncClient(timeout=10.0, follow_redirects=True) as client:
            response = await client.get(api_url, headers=headers)
            content = response.text
            status_code = response.status_code
    except httpx.RequestError as e:
        return JSONResponse({"status": "error", "message": f"Request failed: {e}"})

    # فحص الـ scan type
    result = "No vulnerability found."
    
    if scan_type.lower() == "xss":
        # تفحص وجود script tags كإشارة مبدئية
        if "<script>" in content.lower():
            result = "Potential XSS vulnerability found!"
    elif scan_type.lower() == "sqli":
        # فحص وجود كلمات مفتاحية شائعة للـ SQL errors
        sql_errors = ["sql syntax", "mysql", "syntax error", "unclosed quotation mark"]
        if any(err in content.lower() for err in sql_errors):
            result = "Potential SQL Injection vulnerability found!"
    elif scan_type.lower() == "status":
        # مجرد فحص status code
        result = f"API responded with status code: {status_code}"
    elif scan_type.lower() == "json_check":
        # محاولة قراءة JSON
        try:
            data = response.json()
            result = f"JSON keys: {list(data.keys())}"
        except:
            result = "Response is not JSON."
    else:
        result = "Unknown scan type."

    return JSONResponse({"status": "success", "result": result})
