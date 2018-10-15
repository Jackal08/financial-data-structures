# Author: Jacques Joubert
# Email: jacques@quantsportal.com

"""
Advances in Financial Machine Learning
Marcos Lopez De Prado

Chapter 2: Financial Data Structures
In order to build any of the projects mentioned in the book, we must first
create the various types of structured data from the unstructured data provided.

Many of the projects going forward will require Dollar and Volume bars.

I implemented some speed improvements in the code but feel that there is still
room for improvement, pull requests are welcomed! :)
"""


import numpy as np
import pandas as pd
from math import ceil
import cython_loops


# --------------------------
# Functions
def __pre_process(data):
    # Create an date time
    data['Date_Time'] = data['Date'] + ' ' + data['Time']
    data = data.drop(['Date', 'Time'], axis=1)

    # Calculate the transaction value
    data['Transaction'] = data['Price'] * data['Volume']

    return data


def __extract_data(data):
    # Extract data
    date_time = data[['Date_Time', 'Group']].groupby('Group')['Date_Time'].last()
    ohlc = data[['Price', 'Group']].astype(float).groupby('Group')['Price'].ohlc()
    volume = data[['Volume', 'Group']].astype(float).groupby('Group').sum()
    vwap = pd.DataFrame(data[['Transaction', 'Group']].astype(float).groupby('Group').sum().values / volume.values)

    # Create DataFrame
    bars = pd.concat([date_time, ohlc, volume, vwap], axis=1)
    bars.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'vwap']

    return bars


def __time_bars(data, units):
    # Set the time frame
    duration = str(units) + 'T'

    # Extract data
    data.index = pd.to_datetime(data['Date_Time'])
    ohlc = data.resample(duration, label='right')['Price'].ohlc()
    date_time = pd.DataFrame(ohlc.index, index=ohlc.index)
    volume = data.resample(duration, label='right')['Volume'].sum()
    vwap = data.resample(duration, label='right')['Transaction'].sum().values / volume

    # Create DataFrame
    data = pd.concat([date_time, ohlc, volume, vwap], axis=1)
    data.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'vwap']

    return data


def __dollar_bars(data, units):
    # Dollar metric
    data['CumDollars'] = data['Transaction'].cumsum()
    col_names = data.columns

    # Set the relevant group for each row
    data = cython_loops.set_row_groups(units, np.array(data))
    data = pd.DataFrame(data, columns=col_names)
    data = __extract_data(data)

    return data


def __volume_bars(data, units):
    # Volume metric
    data['CumVol'] = data['Volume'].cumsum()
    col_names = data.columns

    # Set the relevant group for each row
    data = cython_loops.set_row_groups(units, np.array(data))
    data = pd.DataFrame(data, columns=col_names)
    data = __extract_data(data)

    # Todo: Add 1/50 of the daily traded volume
    return data


def __tick_bars(data, units):
    # Create groups based on number of tick bars
    group_index = data.index % units == 0
    group_size = ceil(data.shape[0] / float(units))
    groups = np.array(range(0, int(group_size)))

    # Fill in group values
    data.loc[group_index, 'Group'] = groups
    data['Group'] = data['Group'].ffill()
    data = __extract_data(data)

    return data


def create_bars(data, units=1000, type='tick'):
    """
    Creates the desired bars. 4 different types:
    1. Time Bars
    2. Tick Bars
    3. Volume Bars
    4. Dollar Bars

    See book for more info:
    Marcos Prado (2018), Advances in Financial Machine Learning, pg 25

    :param data: Pandas DataFrame of Tick Data from TickData.com
    :param units: Number of units in a bar.
                  Time Bars: Number of minutes per bar
                  Tick Bars: Number of ticks per bar
                  Volume Bars: Number of shares traded per bar
                  Dollar Bars: Transaction size traded per bar

    :param type: String of the bar type, ('tick', 'volume', 'dollar', 'time')
    :return: Pandas DataFrame of relevant bar data
    """
    data = __pre_process(data)

    # Create an empty column
    data['Group'] = np.nan

    print('Creating {type} bars'.format(type=type))
    if type == 'tick':
        bars = __tick_bars(data, units)
    elif type == 'volume':
        bars = __volume_bars(data, units)
    elif type == 'dollar':
        bars = __dollar_bars(data, units)
    elif type == 'time':
        bars = __time_bars(data, units)
    else:
        raise ValueError('Type must be: tick, volume, dollar, or time')

    return bars


# ------------------------
# Body
if __name__ == '__main__':
    # Read in tick data:
    # https://s3-us-west-2.amazonaws.com/tick-data-s3/downloads/ES_Sample.zip
    data = pd.read_csv('raw_tick_data/ES_Trades.csv')

    # Create bars
    # time_bars = create_bars(data, units=600, type='time')  # Time bars take long to run since I have not optimised them.
    tick_bars = create_bars(data, units=5000, type='tick')
    volume_bars = create_bars(data, units=21731, type='volume')
    dollar_bars = create_bars(data, units=35638840, type='dollar')

    # Write to csv
    # time_bars.to_csv('saved_data/time_bars.csv', index=False)
    tick_bars.to_csv('saved_data/tick_bars.csv', index=False)
    volume_bars.to_csv('saved_data/volume_bars.csv', index=False)
    dollar_bars.to_csv('saved_data/dollar_bars.csv', index=False)
