# PancakeSwap.finance Price Scraper

#``INSTALLATION INSTRUCTIONS: ``

Please note in order to use this repo out of the box, you'll need to download the latest version of chrome driver that the current setup is using by default. 
Further, installation requires implementation of your database of choice, for the simplicity, Firebase Realtime Database was chosen, each day has its own parent node (YYYYMMDD) format with child nodes (HHMM) that have child nodes (seconds).
```Data Format
{
    "CAKE/BUSD": {
        "20210402": {
            "00:44": {
                "15": {
                    'time': '04/02/2021, 00:44:15', 
                    'value': '17.059'
                }
            }
        }
    }
}
```

Get chrome driver: https://chromedriver.chromium.org/downloads 

After downloading Chrome Driver, place it inside the project directory, to folder ./drivers/chromedriver.exe

``Firebase Integration:``

Download service account key from Firebase dashboard, place it in home directory of the project './serviceAccountKey.json'

#``Packages used:``
``selenium`` 
