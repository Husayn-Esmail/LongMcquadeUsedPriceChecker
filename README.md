# Long and Mcquade Price Checker


## Details

This project is used to help make more educated purchasing decisions when buying audio visual equipment. For most uses, I think used gear is a great, economical way to get practicing the skills and buying from a trusted retailer is a way to get the peace of mind of buying new (with warranty's and support) while also sometimes getting a pretty good deal. This program takes a search query (note it must be pretty close to exact or return a single result) and returns the prices from lowest to highest in all stores across Canada.


## Setup

```bash
python3 -m venv venv
. venv/bin/activate
python3 -m pip install requirements.py
```


## Usage
Note that you do need a virtual environment to use this project. Please see the setup section first.
Also note that the program may fail sometimes, if that occurs, just run it until you get results. it works eventually (I think it fails sometimes due to internet connection or cache but eventually I'll work on a fix). It functions for now and that's good enough.

``` bash
python3 main.py "[search query]" # to gather data and run the full operations
python3 -f [filename] # use this if the data was gathered, the file created, but output didn't show properly or to check previous runs -- just summarizes the data basically

``` 

![demo of program](./demo.gif)

Author: Husayn Esmail
Created on: sometime in January 2025.
Completed on: January 25th, 2025. (I think)
