from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from PyPDF2 import PdfReader
import io

app = FastAPI()

# 挂载静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 设置模板目录
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "markdown": ""})

@app.post("/convert", response_class=HTMLResponse)
async def convert_markdown(
    request: Request,
    url: str = Form(None),
    file: UploadFile = File(None)
):
    if url:
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            # 可根据需要提取特定内容
            text = md(str(soup))
            return templates.TemplateResponse("index.html", {"request": request, "markdown": text})
        except Exception as e:
            return templates.TemplateResponse("index.html", {"request": request, "markdown": f"URL 解析错误: {e}"})
    elif file:
        try:
            contents = await file.read()
            pdf_reader = PdfReader(io.BytesIO(contents))
            text = ""
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            # 简单的文本转 Markdown
            markdown_text = text.replace("\n\n", "\n\n")
            return templates.TemplateResponse("index.html", {"request": request, "markdown": markdown_text})
        except Exception as e:
            return templates.TemplateResponse("index.html", {"request": request, "markdown": f"PDF 解析错误: {e}"})
    else:
        return templates.TemplateResponse("index.html", {"request": request, "markdown": "请提供 URL 或上传 PDF 文件。"})