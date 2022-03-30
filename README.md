# ImgSaverCSV

I wanted to download a directory of images from a public Google Sheet that contained images I wanted for use in another project. This Google Sheet had all the images displayed in a specific column and the filenames were strings of characters that didn't tell me anything identifying about *what* the picture displayed. Rather than: 
</p>
    - Right-click</br>
    - Save As</br>
    - Enter unique filename in desired folder
</p>
I thought it would be a great time to play with me knew python knowledge and create a script to do that work for me.
</p>

## Problem
I would like to download a whole inventory of pictures and save them in a local directory with custom names for easy organization. My approach was: </p>

1. Use Google Sheets formula to pull the images' url links as well as what the image was of (in this case, a Pokemon) into two columns to save as a .csv file. </p>

2. Find Python resources to use that will aid in this. I chose to use Pandas and URLLIB.</p>

3. Read documentation and design a script that will loop through each row of the .cvs file and use the "Link" column to download the image from the web, and use the "Name" column to same the image under with a .jpg extension.

## Running it
Make sure you have python installed on your computer with </p>
```
$ brew install pyenv
```
if you use Mac, like I do, use python3 instead of python in the next examples.</br>
Be sure to check your version with 
```
$ python ---version
```
Mac Users, since alot of the old Mac computers came preinstalled with Python 2, installing Python 3 can get weird. I recommend calling the command 
```
$ which python
```
to ensure your computer is using the correct version. Update if needed.</br>
Be sure to install both Pandas and URLLIB with
```
$ pip install pandas
pip install urllib.request
```
*Mac Users, may have to use pip3 here*

