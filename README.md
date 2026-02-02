# Parkey - Secure Password Manager

**Parkey** is a student-built password manager developed as a learning project. We're creating a real, secure tool to help people manage their passwords effortlessly while mastering software development and security principles.

##  Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Releasing](#releasing)

##  Features
-  **Secure Master Password** - Your passwords are protected by a single master password
-  **Encrypted Storage** - All passwords are encrypted using industry-standard algorithms
-  **User-Friendly Interface** - Clean GUI built with Python
-  **Password Organization** - Store, view, and manage multiple passwords
-  **Learning Project** - Built by students to understand security and software development

##  Requirements

### **System Requirements**
- Python 3.8 or higher
- pip package manager
- 100MB free disk space

### **Python Packages**
- `cryptography` - For encryption and security
- `Pillow` - For GUI image handling
- Additional dependencies (specified in requirements.txt)

## Installation

### **Option 1: Using Git**
```bash
# Clone the repository
git clone https://github.com/slnquangtran/Parkey.git

# Navigate to project directory
cd Parkey

# Install dependencies
pip install -r requirements.txt

# Run the app
python parkey/main.py
```

## Releasing

Releases are created automatically when you push a version tag.

1. **Update version** in `parkey/version.py` (e.g. `__version__ = "1.0.0"`).
2. **Update** `CHANGELOG.md` with the new version and changes.
3. **Commit and push** your changes, then create and push a tag:

   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

4. GitHub Actions will create a **Release** with notes from `CHANGELOG.md` and attach a source zip. Check the **Actions** tab, then **Releases** on your repo.
