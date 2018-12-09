import requests
import shutil
import os

def download_file(url, destination):
    """
    Downloads a given URL to the given destination path
    :param url: The URL of the file to download
    :param destination: The destination path on the filesystem
    """
    print ("Downloading mod...")
    r = requests.get(url, stream=True)
    with open(destination, "wb") as output_file:
        shutil.copyfileobj(r.raw, output_file)

def extract_mod(zip, extract_dir):
    print ("Extracting mod...")
    shutil.unpack_archive(zip, extract_dir, format="zip")

if __name__=='__main__':
    download_file("https://github.com/DDLC-TSC/TSC-code/archive/master.zip", "TSC.zip")
