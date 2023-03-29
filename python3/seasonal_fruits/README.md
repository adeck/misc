
## What is this?

I want to know what fruits and veggies are in season in the Pacific Northwest.
Unfortunately the data are always formatted in just the worst possible way.

At first I used the list from the Spruce Eats, but that was inaccurate.
Got turned on to the list from WSU. Using that instead.

So to find out what produce are currently in season, just run:

```
./wsu_seasons.py
```

And (if you run it in April, for example) it should give you something like this:

```
For the month of April, the following produce are in season:
111111111111: Cubed, Dried, Spread
000111111110: Culinary Herbs
000111111100: Greens
111111111111: Hazelnuts
111111111111: Lingonberries
111111111111: Mushrooms
111111111111: Peppers
000110000000: Rhubarb
111111111111: Tomatoes
```

Worth noting there are three entries from the original data that are a bit weird because they're technically subcategories.
Those three are:

1. Cider -- refers to apple cider
2. Cubed, Dried, Spread -- refers to apples that have been preserved
3. Pie -- refers to cherry pie, which can be made from unripe cherries that are otherwise inedible. Neat, huh?

