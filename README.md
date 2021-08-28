# LastName

Lookup last names appearing in the 2010 US Census data.

See:
```
https://www.census.gov/topics/population/genealogy/data/2010_surnames.html
```

This module makes it convenient to do quick lookups on last names. The
results are derived from the CSV downloaded from the above site. The CSV
data is loaded into a sqllite database. 

# Usage

```
    from lastname import LastName

    ln = LastName()

    result = ln.lookup('George')
```

The result will look something like:
```
   {'name': 'GEORGE',
    'rank': '235',
    'count': '128625',
    'prop100k': '43.6',
    'cum_prop100k': '24861.54',
    'pctwhite': '66.47',
    'pctblack': '18.46',
    'pctapi': '7.62',
    'pctaian': '2.24',
    'pct2prace': '2.04',
    'pcthispanic': '3.16'}
```
