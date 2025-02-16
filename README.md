# Super Simple Semantic Analyzer
Semantic analyzer for type-correct assignment expressions
> num five = 5 <br>
> TPYE ID ASSIGN_OP VALUE

## Supported types
- **TXT:** strings between quote marks
  <br> *"this is text"*
- **NUM:** any integer or decimal number
  <br> *1, +2, -3, .4, +0.5, -6.7*
- **DATE:** day(DD), month(MM), year(YYYY) separated by slashes(/), dashes(-) or  dots(.)
  <br> *30/1/2020*
- **CARDINAL:** cardinal and ordinal compass directions
  <br> *north, southwest, east*
