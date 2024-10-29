import requests
from bs4 import BeautifulSoup
import os
import time

base_url = "https://numismatics.org/search/results?q=portrait_facet%3A%22Hadrian%22%20AND%20imagesavailable%3Atrue%20AND%20department_facet%3A%22Roman%22&lang=pl&start="
headers = {'User-Agent': 'Mozilla/5.0'}
os.makedirs('hadrian_images', exist_ok=True)

# iteration parameters
start_range = 0
end_range = 1600
step = 20

# Loop for downloading images
for i in range(start_range, end_range + 1, step):
    # create url for each site containing next 20 images
    url = f"{base_url}{i}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # download all images by html tag
    images = soup.find_all('img')
    for j, img in enumerate(images):
        img_url = img['src']
        try:
            img_data = requests.get(img_url).content
            with open(f'hadrian_images/image_{i}_{j}.jpg', 'wb') as handler:
                handler.write(img_data)
        except:
            print(f"Failed to download {img_url}")
    
    # Status pobierania
    print(f"Page {i // step + 1} of {(end_range // step) + 1} completed.")
    time.sleep(1)  # give the server a bit of rest
print("Download completed!")