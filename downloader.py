import pandas as pd
import urllib.request



##--------------------------
def url_to_jpg(i, data, file_path):
    
    df_name = data[0]
    print(df_name)

    filename = df_name + '.jpg'.format(i)
    full_path = '{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(data[1], full_path)

    print('{} has been saved!'.format(filename))

   
    return None

#------------------------


# Constants
FILE = './IMGSURL.csv'
FILE_PATH = '../LegendsDexTrack/images/'

# Read list of URLS and apply name based on image subject
data = pd.read_csv(FILE, delimiter=",")

df = pd.DataFrame(data)
# df_name = pd.DataFrame(data, columns=['Name'])
# print(df_name)

# Save images to directory by iterating through entire list
for i, data in enumerate(data.values):
    url_to_jpg(i, data, FILE_PATH)

# print(data.values)