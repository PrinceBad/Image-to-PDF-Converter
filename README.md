🖼️ Image to PDF Converter 📄
This is a simple, stylish desktop application for Windows to convert multiple images into a single PDF document. It was built with Python and Tkinter, featuring a modern dark theme for a comfortable user experience.

✨ Key Features
🎨 Intuitive Dark Theme UI: A clean, modern interface that's easy on the eyes.

🗂️ Bulk Image Processing: Select and convert multiple images at once.

📐 Smart Scaling: Automatically preserves the aspect ratio of your images to fit them perfectly on each PDF page without distortion.

💻 Cross-Platform Potential: Built with Tkinter, the code is cross-platform and can run on macOS and Linux with minimal adjustments.

🚀 Lightweight & Fast: No heavy dependencies, just a straightforward tool that gets the job done quickly.

🛠️ Tech Stack
Language: Python 3

GUI Framework: Tkinter

Core Libraries: Pillow (for image processing) & ReportLab (for PDF creation)

🚀 Getting Started
Follow these steps to get the application running on your local machine.

Prerequisites
Python 3.6+: Make sure Python is installed on your system. You can download it from python.org.

pip: Python's package installer, which usually comes with Python.

Installation & Setup

Clone the repository:
Open your terminal or command prompt and run:

git clone https://github.com/YOUR_USERNAME/image-to-pdf-converter.git
cd image-to-pdf-converter

Don't forget to replace YOUR_USERNAME with your actual GitHub username.

Create and activate a virtual environment (Recommended):
This isolates the project's dependencies from your system's global Python environment.

# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install the required libraries:
The requirements.txt file lists all the necessary packages.

pip install -r requirements.txt

Usage
With your virtual environment activated and dependencies installed, run the following command in your terminal:

python converter_dark.py

How it works:

Click "Select Images" to choose your image files (.jpg, .png, etc.).

Your selected images will appear in the listbox.

Click "Convert to PDF".

Choose where you want to save your new PDF file.

A success message will pop up once your PDF is ready!

🤝 Contributing
Contributions are welcome! If you have ideas for new features or improvements, feel free to fork the repository and submit a pull request.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is licensed under the MIT License. See the LICENSE file for more details
