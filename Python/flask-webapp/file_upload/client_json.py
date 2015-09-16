import requests

files = {'file1': ('file1.png', open('file1.png', 'rb'), 'image/png'),
         'file2': ('file2.png', open('file2.png', 'rb'), 'image/png')
         }

crop_info = {'data':
             # Has to be valid JSON
             '{"file1" : {"x": 10, "y": 10, "crop_width": 400, "crop_height": 200},'
             '"file2" : {"x": 10, "y": 10, "crop_width": 400, "crop_height": 200}}'}
url = 'http://127.0.0.1:8000'
r = requests.post(url, data=crop_info, files=files)
