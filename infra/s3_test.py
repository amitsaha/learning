from boto.s3.connection import S3Connection
from cStringIO import StringIO
from PIL import Image as pil

AWS_KEY="skdhfd"                                                                                                                                              
AWS_SECRET="sdfsd"
BUCKET_NAME="dfdfd"

conn = S3Connection(AWS_KEY, AWS_SECRET)
bucket = conn.get_bucket(BUCKET_NAME)

# upload
#with open("file.png", "rb") as fp:
# location = bucket.new_key("keyname")
# location.content_type = "image/png"
# location.set_contents_from_file(fp)

location = bucket.get_key("keyname")
data = location.get_contents_as_string()

with open("data.png", "wb") as f:
 f.write(data)
