from imgur_auth import auth
from datetime import datetime

album =' none'
image_path='1.jpg' # enter image file name which you want to upload 

def upload_image(client):

    config = {
        'name': 'test',
        'title': 'testst',
        }
    print('uploading Image...')
    image = client.upload_from_path(image_path, config=config, anon=False)
    print('done')

    return image

if __name__=="__main__":
    client = auth()
    image = upload_image(client)
    print("{0}".format(image['link']))
