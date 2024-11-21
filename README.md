# 📄 URL/PDF/DOCX to Markdown Converter

Welcome to the **URL/PDF/DOCX to Markdown Converter**! 🚀 This web application allows you to effortlessly convert web pages, PDF documents, and DOCX files into well-structured Markdown format. Whether you're a developer, writer, or anyone needing to transform documents, this tool has got you covered!

## 🌟 Features

- **Convert URLs to Markdown** 🌐: Transform any webpage into Markdown with just a few clicks.
- **Upload and Convert PDF Files** 📄: Use a powerful PDF parser (`pdfplumber`) for accurate text extraction.
- **Upload and Convert DOCX Files** 📝: Easily convert Word documents into Markdown format.
- **Download Markdown Files** 💾: Save your converted Markdown files directly to your device.
- **Copy Functionality** 📋: Quickly copy the original Markdown or rendered HTML content to your clipboard.
- **User-Friendly Interface** 🎨: Clean and responsive design for an optimal user experience.
- **Error Handling** ❗: Receive clear error messages for unsupported file types or conversion issues.
- **Loading Indicator** ⏳: Visual feedback during the conversion process.

## 🛠️ Technologies Used

- **Backend**:
  - [FastAPI](https://fastapi.tiangolo.com/) - A modern, fast web framework for building APIs with Python.
  - [pdfplumber](https://github.com/jsvine/pdfplumber) - Extract text from PDF files.
  - [python-docx](https://python-docx.readthedocs.io/) - Manipulate DOCX files.
  - [Markdownify](https://github.com/matthewwithanm/python-markdownify) - Convert HTML to Markdown.
  - [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Parse HTML content.
- **Frontend**:
  - HTML, CSS, JavaScript
  - [marked.js](https://github.com/markedjs/marked) - A Markdown parser and compiler.
- **Others**:
  - [Uvicorn](https://www.uvicorn.org/) - A lightning-fast ASGI server.

## 📁 Project Structure

```
markdown_converter/
├── main.py
├── templates/
│   └── index.html
├── static/
│   ├── styles.css
│   └── marked.min.js
├── downloads/
├── requirements.txt
└── README.md
```

- **main.py**: The main FastAPI application handling routes and conversion logic.
- **templates/index.html**: The HTML template for the frontend interface.
- **static/**: Contains static files like CSS and JavaScript.
- **downloads/**: Temporary storage for generated Markdown files available for download.
- **requirements.txt**: Python dependencies required for the project.
- **README.md**: This documentation file.

## 🏁 Getting Started

### Prerequisites

- **Python 3.7+**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
- **pip**: Python package installer. It usually comes with Python.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/DanielZhui/py-2-md
   cd py-2-md
   ```

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

- The `--reload` flag enables auto-reloading on code changes.
- Access the application by navigating to `http://127.0.0.1:8000` in your web browser.

## 🎨 Usage

1. **Convert a URL**

   - Enter the desired URL in the "Enter URL" field.
   - Click the **Convert** button.
   - View the original Markdown and the rendered content side by side.
   - Use the **Copy** buttons to copy content to your clipboard or **Download** the Markdown file.

2. **Convert a PDF/DOCX File**

   - Click on the file input to upload a PDF or DOCX document.
   - Click the **Convert** button.
   - Similar to URL conversion, view and manage your Markdown content.

## 📸 Screenshots

### Home Page

![Home Page](https://imgfans.com/_Xavph)

### Conversion Result

![conversion image](https://imgfans.com/_Q3adv)


![conversion image](https://imgfans.com/_wM316)

*Replace the placeholder links with actual screenshots of your application.*

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project, please follow these steps:

1. **Fork the Repository**

2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add your feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

Provide a clear description of your changes and the problem they solve.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🛡️ Security

- **Input Validation**: Ensure that only valid URLs and supported file types (PDF, DOCX) are processed.
- **File Handling**: Temporary files are stored securely and can be periodically cleaned to prevent unauthorized access.
- **HTTPS**: For production deployments, ensure that the application is served over HTTPS to secure data transmission.

## 🔗 Useful Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [pdfplumber GitHub](https://github.com/jsvine/pdfplumber)
- [python-docx Documentation](https://python-docx.readthedocs.io/)
- [marked.js GitHub](https://github.com/markedjs/marked)
---

✨ **Happy Converting!** ✨