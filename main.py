from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import pdfplumber
from docx import Document
import io
import uuid
import os

app = FastAPI()

# 挂载静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 设置模板目录
templates = Jinja2Templates(directory="templates")

# 临时存储下载的 Markdown 文件
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "markdown": "", "error": "", "file_id": ""})

@app.post("/convert", response_class=HTMLResponse)
async def convert_markdown(
    request: Request,
    url: str = Form(None),
    file: UploadFile = File(None)
):
    markdown_text = ""
    error_message = ""
    file_id = str(uuid.uuid4())

    if url:
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            # 可根据需要提取特定内容，比如主要内容区域
            markdown_text = md(str(soup)).strip()
        except Exception as e:
            error_message = f"URL 解析错误: {e}"
    elif file:
        filename = file.filename
        try:
            file_contents = await file.read()
            if filename.lower().endswith(".pdf"):
                with pdfplumber.open(io.BytesIO(file_contents)) as pdf:
                    text = ""
                    for page in pdf.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text + "\n"
                markdown_text = text.strip()
            elif filename.lower().endswith(".docx"):
                doc = Document(io.BytesIO(file_contents))
                text = "\n".join([para.text for para in doc.paragraphs])
                markdown_text = text.strip()
            else:
                error_message = "不支持的文件类型。仅支持 PDF 和 DOCX。"
        except Exception as e:
            error_message = f"文件解析错误: {e}"
    else:
        error_message = "请提供 URL 或上传 PDF/DOCX 文件。"

    if markdown_text:
        # 将 Markdown 内容写入临时文件
        file_path = os.path.join(DOWNLOAD_DIR, f"{file_id}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(markdown_text)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "markdown": markdown_text,
        "error": error_message,
        "file_id": file_id if markdown_text else ""
    })

@app.get("/download/{file_id}", response_class=FileResponse)
async def download_markdown(file_id: str):
    file_path = os.path.join(DOWNLOAD_DIR, f"{file_id}.md")
    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename=f"converted_{file_id}.md", media_type='text/markdown')
    else:
        return {"error": "文件不存在"}