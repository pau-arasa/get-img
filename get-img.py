import os
import requests

print("   ______ ________ _________     _____ ____    ____  ______   \n"
       " .' ___  |_   __  |  _   _  |   |_   _|_   \\  /   _.' ___  |  \n"
       "/ .'   \\_| | |_ \\_|_/ | | \\_______| |   |   \\/   |/ .'   \\_|  \n"
       "| |   ____ |  _| _    | |  |______| |   | |\\  /| || |   ____  \n"
       "\\ `.___]  _| |__/ |  _| |_       _| |_ _| |_\\/| |\\ `.___]  | \n"
       " `._____.|________| |_____|     |_____|_____||_____`._____.'  \n"
       "                                                              \n");

while True:
    try:
        n_images = int(input("Number of images: "))
        break
    except ValueError:
        print("Enter an int")

#Default image size
width=800
height=600

response = input("Specify image size? [Y/n]: ").strip().lower()

if response in ('y', 'yes', ''):
    while True:
        try:
            size_input = input("Specify size [width height], e.g., 1024 768: ")
            width_str, height_str = size_input.strip().split()
            width = int(width_str)
            height = int(height_str)
            break
        except ValueError:
            print("Enter two integers separated by a space (e.g., 800 600).")
else:
    print("Image size will use default.")


dir = input("Specify directory: ")

os.makedirs(dir, exist_ok=True)
api_url = f"https://picsum.photos/{width}/{height}"

# Download loop
for i in range(n_images):
    print(f"Downloading image {i+1}...")
    response = requests.get(api_url)

    if response.status_code == 200:
        image_path = os.path.join(dir, f"get-img_{i+1}.jpg")
        with open(image_path, "wb") as f:
            f.write(response.content)
        print(f"Saved to {image_path}")
    else:
        print(f"Failed to download image {i+1}: {response.status_code}")