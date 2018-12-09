import requests
import shutil


def get_ddlc_url(mac):
    """
    Retrieves a download link for Doki Doki Literature Club from Itch.io
    :param mac: Whether to download the macOS version as opposed to the Windows / Linux version
    :return: The URL of the .zip file
    """
    if mac == True:
        r = requests.post("https://teamsalvato.itch.io/ddlc/file/" + ("594901"))
        return r.json()["url"]
    else:
        r = requests.post("https://teamsalvato.itch.io/ddlc/file/" + ("594897"))
        return r.json()["url"]


def download_file(url, destination):
    """
    Downloads a given URL to the given destination path
    :param url: The URL of the file to download
    :param destination: The destination path on the filesystem
    """
    r = requests.get(url, stream=True)
    with open(destination, "wb") as output_file:
        shutil.copyfileobj(r.raw, output_file)


if __name__ == '__main__':
    print("Getting download link")
    link = get_ddlc_url(False)
    print("Downloading DDLC")
    download_file(link, "ddlc.zip")
