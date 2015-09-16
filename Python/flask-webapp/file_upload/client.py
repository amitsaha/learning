import requests

files = {'file1': ('file1.png', open('file1.png', 'rb'), 'image/png'),
         'file2': ('file2.png', open('file2.png', 'rb'), 'image/png')
         }

crop_info = {'file1.x': 10,
             'file1.y': 10,
             'file1.crop_width': 400,
             'file1.crop_height': 200,
             'file2.x': 10,
             'file2.y': 10,
             'file2.crop_width': 400,
             'file2.crop_height': 200,
           }

url = 'http://127.0.0.1:8000'
r = requests.post(url, data=crop_info, files=files)
