""" UnitConversion.py

Collection of functions to perform unit conversions

Author: Jeremy Dunne
Date: October 2021

"""

"""! convert inches to milimeters
@param inch (float) to convert
@return float with the converted milimeters
"""
def inch_to_milimeter(inch):
    return inch * 25.4

"""! convert inches to meters
@param inch (float)
"""
def inch_to_meter(inch):
    return inch * 25.4 / 1000

def inch_to_kilometer(inch): 
