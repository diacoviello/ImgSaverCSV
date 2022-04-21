
import os
import pandas as pd
import urllib.request



# # ##---THIS IS FOR HTML URL LINKS-----------------------
def url_to_jpg(i, data, file_path):
    
    df_name = data[0]
    # print(df_name)

    filename = df_name + '.jpg'.format(i)
    full_path = '{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(data[1], full_path)

    # print('{} has been saved!'.format(filename))

   
    return None

# # #------------------------


# Constants:
# this is where you path to your .csv 
FILE = '/Users/Dave/Documents/Development stuff/MyProjects/ImgUrlNameSave/IMGSDIR.csv'
# this is where you path to where you want the stored files to go
FILE_PATH = '/Users/Dave/Desktop/pokedexPics/'
os.chdir(FILE_PATH)
print(FILE_PATH)

# Read list of URLS and apply name based on image subject
data = pd.read_csv(FILE, delimiter=",")

df = pd.DataFrame(data)

# print(df)

# Save images to directory by iterating through entire list

for i, data in enumerate(data.values):
    url_to_jpg(i, data, FILE_PATH)

print(data.values)