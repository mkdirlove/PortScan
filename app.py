import requests
import zipfile
import os

def download_file(url, dest_filename):
    # Send a GET request to the URL
    response = requests.get(url, stream=True)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Open the destination file in write-binary mode and write the content to it
        with open(dest_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"File downloaded successfully: {dest_filename}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        return False
    return True

def unzip_file(zip_filename, extract_to):
    # Unzipping the file
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"File unzipped successfully to: {extract_to}")

def remove_file(file_path):
    # Removing the ZIP file
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File removed: {file_path}")
    else:
        print(f"File not found: {file_path}")

# URL to the ZIP file
url = "https://github.com/mkdirlove/PortScan/releases/download/v1.0-dev/PortScan.zip"
# Destination file name
zip_filename = "PortScan.zip"
# Directory to extract the contents of the ZIP file
extract_to = "./PortScan"

# Download the file
if download_file(url, zip_filename):
    # Unzip the file
    unzip_file(zip_filename, extract_to)
    
    # Remove the ZIP file
    remove_file(zip_filename)
