import pandas as pd
import urllib.request



##--------------------------
def url_to_jpg(i, data, file_path):

    filename = 'icon-{}.jpg'.format(i)
    full_path = '{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(data, full_path)

    print('{} has been saved!'.format(filename))

   
    return None

#------------------------


# Constants
FILE = './IMGSURL.csv'
FILE_PATH = '../LegendsDexTrack/images/'

# Read list of URLS and apply name based on image subject
data = pd.read_csv(FILE, delimiter=",")

df = pd.DataFrame(data, columns=[['Name','URL']])



# Save images to directory by iterating through entire list
for i, data in enumerate(data.values):
    url_to_jpg(i, data[1], FILE_PATH)

# print(data.values)