"""Practice: Rain

The city of Portland has rain gauges that keep track of rainfall.

[A website](http://or.water.usgs.gov/non-usgs/bes/) has text data tables the history of all the daily measurements at these gauges.

Python gives you a module called `urllib.request` you can use a function `urllib.request.urlopen(url)` which returns a file-like object.

Look at [the docs](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) for that module.

One little difference is the file-like object doesn't return strings, it returns **bytes**.

Use the following code snippet to make it return strings.






​

Use that module to read [the history of the gauge at Sunnyside School](http://or.water.usgs.gov/non-usgs/bes/sunnyside.rain). It looks like:

TEXT HEADER...

​

            Daily  Hourly data -->

   Date     Total    0   1

--------------------------

25-MAR-2016     0    0   0

24-MAR-2016     6    0   1

MORE...

The amounts are in hundredths of inches.


* Parse and store the **daily total** data for each day.

Find and print out the specific date with the most rain.

* Find and print out the year with the most rain.

​

## Advanced

* Find and print the day of the year with the most rain on average.

E.g. December 30th has 1" of rain on average.

* Allow someone to type in a date in the future and, using the average value predict the amount of rain."""

import urllib.request
import statistics

with urllib.request.urlopen('http://www.gutenberg.org/ebooks/1342.txt.utf-8') as pride_and_prejudice_file:

  lines = [byte_line.decode('utf-8') for byte_line in pride_and_prejudice_file]

with urllib.request.urlopen('https://raw.githubusercontent.com/selassid/codeguild/master/sunnyside.rain') as rain_gauge_file:

	rain_stuff = [byte_line.decode('utf-8') for byte_line in rain_gauge_file]

print(rain_stuff)



