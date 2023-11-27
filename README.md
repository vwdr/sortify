# Automatic Image Organizer

## Overview

This Python script is designed to automatically organize downloaded images into separate folders based on their file extensions. It continuously monitors a specified download folder, identifies image files, and moves them to corresponding folders within a main directory.

## Features

- Organizes images by file extension (e.g., .jpg, .jpeg, .png).
- Monitors the download folder for new images.
- Simple and lightweight.

## Getting Started

### Prerequisites

- Python 3.x
- shutil module (included in Python standard library)

### Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/image-organizer.git
   cd image-organizer
   ```

2. Modify the script with your folder paths:

   ```python
   download_folder = '/path/to/your/download/folder'
   main_folder = '/path/to/your/main/folder'
   ```

3. Run the script:

   ```bash
   python image_organizer.py
   ```

## Customization

You can customize the script to support additional file extensions by modifying the following line in the script:

```python
image_files = [file for file in all_files if os.path.splitext(file)[1].lower() in ['.jpg', '.jpeg', '.png']]
```

Add or remove file extensions as needed.

## Contributing

If you'd like to contribute to this project, feel free to open an issue or submit a pull request.

## Acknowledgments

- Thanks to the open-source community for inspiration and support.

---
