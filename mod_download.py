import requests
import shutil
import os

def download_file(url, destination):
    """
    Downloads a given URL to the given destination path
    :param url: The URL of the file to download
    :param destination: The destination path on the filesystem
    """
    r = requests.get(url, stream=True)
    with open(destination, "wb") as output_file:
        shutil.copyfileobj(r.raw, output_file)

def extract_mod(zip):
    print ("Downloading mod...")
    cwd = os.getcwd()
    shutil.unpack_archive(zip, extract_dir=cwd, format="zip")

if __name__=='__main__':
    download_file(link, "TSC.zip")
