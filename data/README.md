### Dataset
This dataset is same as the dataset published on Kaggle at [this link](https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results)

The description below has been copied over as is from the download site.

> ### Context
This is a historical dataset on the modern Olympic Games, including all the Games from Athens 1896 to Rio 2016. I scraped this data from www.sports-reference.com in May 2018. The R code I used to scrape and wrangle the data is on GitHub. I recommend checking my kernel before starting your own analysis.  
> Note that the Winter and Summer Games were held in the same year up until 1992. After that, they staggered them such that Winter Games occur on a four year cycle starting with 1994, then Summer in 1996, then Winter in 1998, and so on. A common mistake people make when analyzing this data is to assume that the Summer and Winter Games have always been staggered.
> ### Content
The file `athlete_events.csv` contains 271116 rows and 15 columns. Each row corresponds to an individual athlete competing in an individual Olympic event (athlete-events). The columns are:

|Column Name |description|
|-|-|
|**ID** | Unique number for each athlete|
|**Name** | Athlete's name|
|**Sex** | M or F|
|**Age** | Integer|
|**Height** | In centimeters|
|**Weight** | In kilograms|
|**Team** | Team name|
|**NOC** | National Olympic Committee 3-letter code|
|**Games** | Year and season|
|**Year** | Integer|
|**Season** | Summer or Winter|
|**City** | Host city|
|**Sport** | Sport|
|**Event** | Event|
|**Medal** | Gold, Silver, Bronze, or NA|

The file `noc_regions.csv` has information about the country codes.

|Column Name |description|
|-|-|
|**NOC**| National Olympic Committee 3 letter code|
|**Country name**| matches with regions in map_data("world")|
|**Notes**|Extra Notes|

> ### Acknowledgements
The Olympic data on www.sports-reference.com is the result of an incredible amount of research by a group of Olympic history enthusiasts and self-proclaimed 'statistorians'. Check out their blog for more information. All I did was consolidated their decades of work into a convenient format for data analysis.
> ### Inspiration
This dataset provides an opportunity to ask questions about how the Olympics have evolved over time, including questions about the participation and performance of women, different nations, and different sports and events.
