Tool for mass downloading csv files from https://promo.betfair.com/betfairsp/prices

#### Setup:
Setup a virtual environment and install the requirements.

Edit the file_filter variable inside the betfair.py script to define the files you are interested in.

#### Run the script:
```bash
scrapy runspider betfair.py
```

The downloaded files will be saved in ./downlaods/