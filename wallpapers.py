from bs4 import BeautifulSoup
import requests
import os
import shutil
import argparse
from tqdm import tqdm

base_url = "https://uhdwallpapers.org"


def downloader(urls, resolution, folder,window,pics):
    '''
    This method clears all the files inside the folder destination and  then downloads the supplied urls according to the resolution given
    '''
    counter = 1
    if folder in os.listdir():
        file_list = [x for x in os.listdir(folder)]
        os.chdir(folder)
        for x in file_list:
            os.remove(x)
        print("Deleting initial files")
    else:
        os.mkdir(folder)
        os.chdir(folder)
        print(f"creating a folder called {folder}")
    print("Downloading images")
    for url in tqdm(urls):
        try:
            modified_url = url+'/'+resolution
            res = requests.get(modified_url)
            soup = BeautifulSoup(res.content, "html.parser")
            img_div = soup.find(class_="wpFullImage")
            img = img_div.img
            img_url = base_url+img.attrs["src"]
            img_data = requests.get(img_url)
            f = open(f"./pic{counter}.png", "wb")
            f.write(img_data.content)
            f.close()
            counter += 1
            percent=(counter/pics)*100
            window.progressBar.setProperty("value", percent)
        except:
            print("Skipping this photograph as some error occured")
    window.progressBar.setProperty("value",100)
    window.pushButton.setEnabled(True)



def get_urls(category, pics):
    '''
    This method scrapes all the urls from the category and page number supplied and returns the list
    '''
    url_list = []
    print("Getting image urls")
    for i in tqdm(range(1, (int(pics)//16)+2)):
        payload = {"page": i}
        url = base_url+'/category/'+category
        res = requests.get(url, params=payload)
        if res.status_code == 200:
            soup = BeautifulSoup(res.content, "html.parser")
            lis = soup.find_all(class_='item')
            if len(lis) == 0:
                print("No more images available")
                break
            for li in lis:
                url_list.append(li.figure.a.attrs["href"])
                if len(url_list) >= int(pics):
                    break
        else:
            print(
                "Could not find the page, check connectivity,category or resolution given")

    return url_list


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(
#         description="Wallpaper downloader script use command `python downloader.py` to run with default options"
#     )
#     parser.add_argument(
#         "--category", type=str, help="Enter the category of wallpapers you want to download")
#     parser.add_argument("--pics", type=int,
#                         help="Enter number of pictures you want to download")
#     parser.add_argument(
#         "--folder", type=str, help="**DANGEROUS**:This is the name of folder where you want to store the images, but any files previously inside this folder will be deleted")
#     parser.add_argument(
#         "--resolution", type=str, help="Choose the resolution fit for your desktop, demo resoltion : 1920x1080")
#     args = parser.parse_args()

#     category, pics, folder, resolution = "nature", "10", "script_downloads", "1920x1080"
#     if args.category:
#         category = args.category
#     if args.pics:
#         pics = args.pics
#     if args.folder:
#         folder = args.folder
#     if args.resolution:
#         resolution = args.resoltion
#     urls = get_urls(category=category, pics=pics)
#     downloader(urls, resolution=resolution, folder=folder)
