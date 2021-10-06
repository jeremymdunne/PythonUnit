##  @file main.py
#   Simple script showing how to use the ValueWithUnits package
#
#   @author Jeremy Dunne
#   @date October, 2021


import Units

### creating and getting data
# try a blank
blank = Units.ValueWithUnits()
blank_value, blank_unit = blank.getValue()
print("Blank Value: " + str(blank_value) + ' ' + str(blank_unit))
# try a real unit
inch = Units.ValueWithUnits(12.3,'inches')
inch_value, inch_unit = inch.getValue()
print("Inch Value: " + str(inch_value) + ' ' + str(inch_unit))
# this should not raise an exception
furlong = Units.ValueWithUnits(2,'furlongs',True)
furlong_value, furlong_unit = furlong.getValue()
print("Furlong Value: " + str(furlong_value) + ' ' + str(furlong_unit))
# this should raise an exception
try:
    fortnight = Units.ValueWithUnits(3, 'fortnights')
except Units.UnsuportedUnitError as error:
    print(error)


### converting
inches = Units.ValueWithUnits(25.3, 'inches')
mm = inches.convert('mm')
inches_value, inches_units = inches.getValue()
print(inches_value, inches_units, ' is ', mm, 'mm')
