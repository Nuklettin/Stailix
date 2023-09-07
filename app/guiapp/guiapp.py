import subprocess
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from imgurpython import ImgurClient
import re
import webbrowser
from datetime import datetime

links = []
image_path = ''


def open_links_in_browser(link_array):
    for link in link_array:
        webbrowser.open(link)


def choose_image():
    global image_path
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if file_path:
        image_path = file_path
        load_and_display_image(file_path)


def load_and_display_image(file_path):
    try:
        image = Image.open(file_path)
        image.thumbnail((200, 200))
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo  # To prevent garbage collection
        m.update()
        print(image_path)
    except Exception as e:
        image_path.set("Error loading image")


def get_link(text):
    link_list = []
    hash_values = re.findall("hash: .*$", text, flags=re.MULTILINE)
    hash_value = hash_values[0].__str__()
    kek= hash_value.split("'")
    keks = kek[1]
    link_1 = "https://cdn.midjourney.com/" + keks + "/0_0.png"
    link_2 = "https://cdn.midjourney.com/" + keks + "/0_1.png"
    link_3 = "https://cdn.midjourney.com/" + keks + "/0_2.png"
    link_4 = "https://cdn.midjourney.com/" + keks + "/0_3.png"
    link_list.append(link_1)
    link_list.append(link_2)
    link_list.append(link_3)
    link_list.append(link_4)
    return link_list


def upload_imgur():
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''

    # Here's the metadata for the upload. All of these are optional, including
    # this config dict itself.
    config = {
        'album': None,
        'name':  'Catastrophe!',
        'title': 'Catastrophe!',
        'description': 'Cute kitten being cute on {0}'.format(datetime.now())
    }

    client_id = 'a7413ed3a8b2d82' #a7413ed3a8b2d82
    client_secret = '1e4964e6592f9a640de2b833f1666609d11bd116' #1e4964e6592f9a640de2b833f1666609d11bd116
    access_token = '18395f8597e66529c9d67a018ea389f3e3666e2d' #18395f8597e66529c9d67a018ea389f3e3666e2d
    refresh_token = 'd5163636534f2835d8f5d8f5e185d6a7564ac46a' #d5163636534f2835d8f5d8f5e185d6a7564ac46a

    # Note since access tokens expire after an hour, only the refresh token is required (library handles autorefresh)
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print("Image was posted! Go check your images you sexy beast!")
    print("You can find it here: {0}".format(image['link']))

    return image['link']


def create_image():
    reference_url = upload_imgur()
    prompt_input = prompt_entry.get("1.0", 'end-1c')
    temp_text = ''
    with open("example/imagine-ws.ts", "r") as file:
        filedata = file.read()
        filedata = re.sub('let prompt = "?(.*?)"', 'let prompt = "' + reference_url + ', ' + prompt_input + '"', filedata, flags=re.DOTALL)
    with open("example/imagine-ws.ts", "w") as file:
        file.write(filedata)
    with subprocess.Popen('npx tsx example/imagine-ws.ts', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True) as process:
        for line in process.stdout:
            line = line.decode()  # defaulting to system encoding
            #print(line)
            temp_text += line
            process.poll()
    process.wait()
    global links
    links = get_link(temp_text)
    print(links)
    open_links_in_browser(links)



m = Tk()
m.title("Stailix")

choose_button = Button(m, text="Referans Görsel Yükle", command=choose_image)
choose_button.grid(row=0,column=0)

image_label = Label(m)
image_label.grid(row=0, column=1)

Label(m, text='Prompt').grid(row=1, column=0)

prompt_entry = Text(m, width=50, height=3)
prompt_entry.grid(row=1, column=1)

create_button = Button(m, width=20, text='Create', command=create_image)
create_button.grid(row=2, column=1)


m.mainloop()
