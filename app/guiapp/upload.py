#!/usr/bin/env python3

'''
	Here's how you upload an image. For this example, put the cutest picture
	of a kitten you can find in this script's folder and name it 'Kitten.jpg'

	For more details about images and the API see here:
		https://api.imgur.com/endpoints/image
'''

from datetime import datetime

album = None # You can also enter an album ID here
image_path = 'Kitten.jpg'

def upload_kitten(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''

    # Here's the metadata for the upload. All of these are optional, including
    # this config dict itself.
    config = {
        'album': album,
        'name':  'Catastrophe!',
        'title': 'Catastrophe!',
        'description': 'Cute kitten being cute on {0}'.format(datetime.now())
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

    return image


# If you want to run this as a standalone script
if __name__ == "__main__":
    from imgurpython import ImgurClient

    # If you already have an access/refresh pair in hand
    client_id = 'YOUR CLIENT ID' #a7413ed3a8b2d82
    client_secret = 'YOUR CLIENT SECRET' #1e4964e6592f9a640de2b833f1666609d11bd116
    access_token = 'USER ACCESS TOKEN' #18395f8597e66529c9d67a018ea389f3e3666e2d
    refresh_token = 'USER REFRESH TOKEN' #d5163636534f2835d8f5d8f5e185d6a7564ac46a

    # Note since access tokens expire after an hour, only the refresh token is required (library handles autorefresh)
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)
    image = upload_kitten(client)

    print("Image was posted! Go check your images you sexy beast!")
    print("You can find it here: {0}".format(image['link']))