Author: Jacques Francois Joubert

Email: jacques@quantsportal.com

Date: 7 May 2018 

# Create Financial Data Structures: Time, Tick, Volume, and Dollar Bars

Version of Pycharm Professional Edition: 2017.3

Version of Python: 3.6.5

## Description

This program is to help users create structured financial data from unstructured data, in the form of time, tick, volume, and dollar bars.

The user passes tick data to the create_bars(data, units=1000, type='tick') function and it returns the desired structured data.
Everything can be found in the main.py file. I left lots of comments in the code. 

These bars are used throughout the text book (*Advances in Financial Machine Learning, By Marcos Lopex de Prado, 2018, pg 25*)
to build the more interesting features for predicting financial time series data.

A great paper to read more about how the tick, volume, and dollar bars have better statistical properties to standard time sampled data is:
[The Volume Clock: Insights into the high frequency paradigm, Lopez de Prado, et al](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2034858)

Note: Please make sure you unzip the ES_Trades.csv.zip found in raw_tick_data, it was too big to upload without zipping it first.

## Installation Windows

Ha-Ha be serious, Quants don't use windows. You can download a real operating system here: https://www.ubuntu.com/download/desktop
You can also buy a real computer here: https://www.apple.com/shop/buy-mac/macbook-pro

## Installation on Mac OS X

Make sure you install the latest version of the Anaconda 3 distribution which must include an IDE like Spyder.
To do this you can follow the install and update instructions found on this link: https://www.anaconda.com/download/#mac

To install the package dependency run: pip install -r pip_requirements.txt

From Spyder or Pycharm IDE: Open the file main.py and run it.

From Terminal: 

1. Go to the directory where you have saved the file, example: cd Desktop/bars/awesome/
2. pip install -r pip_requirements.txt
3. Run the file: main.py (python main.py)

## Installation on Ubuntu Linux

Make sure you install the latest version of the Anaconda 3 distribution which must include an IDE like Spyder.
To do this you can follow the install and update instructions found on this link: https://www.anaconda.com/download/#linux

To install the package dependency run: pip install -r pip_requirements.txt

From Spyder or Pycharm IDE: Open the file main.py and run it.

From Terminal: 

1. Go to the directory where you have saved the file, example: cd Desktop/bars/awesome/
2. pip install -r pip_requirements.txt
3. Run the file: main.py (python main.py)

## Packages Used
Packages can all be installed by running the following command in the terminal (project working directory): "pip install -r pip_requirements.txt" 
* numpy==1.14.2
* pandas==0.22.0
* Cython==0.28.2

## Notes: 
* This program was built using a MacBook Pro on OS X.
* Python 3.6.5 was used
* Tested Successfully on both Mac OS X and Linux Ubuntu

## License (MIT)
The MIT License (MIT)

Copyright (c) 2018 Jacques Joubert

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
