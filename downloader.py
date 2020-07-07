from bs4 import BeautifulSoup
import requests
import os
import shutil

base_url = "https://uhdwallpapers.org"


def downloader(urls, resolution):
    '''
    This method clears all the files inside the folder destination and  then downloads the supplied urls according to the resolution given
    '''
    counter = 1
    file_list = [x for x in os.listdir("script_downloads")]
    os.chdir("script_downloads")
    for x in file_list:
        os.remove(x)
    print("Deleting initial files")
    for url in urls:
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
        except:
            print("Skipping this photograph as some error occured")


def get_urls(category, pics):
    '''
    This method scrapes all the urls from the category and page number supplied and returns the list
    '''
    url_list = []
    for i in range(1, (int(pics)//16)+2):
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
            print("Could not find the page, check connectivity,category or page number")

    return url_list


if __name__ == "__main__":
    urls = get_urls(category="travel", pics="37")
    print(len(urls))
    downloader(urls, resolution="1920x1080")
