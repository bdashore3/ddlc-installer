import requests
import shutil

def download_file(url, destination):
    """
    Downloads a given URL to the given destination path
    :param url: The URL of the file to download
    :param destination: The destination path on the filesystem
    """
    r = requests.get(url, stream=True)
    with open(destination, "wb") as output_file:
        shutil.copyfileobj(r.raw, output_file)

if __name__=='__main__':
    print("Downloading TSC")
    download_file(link, "TSC.zip")