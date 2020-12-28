# Will we get a White Christmas in Transylvania in 2020?

What makes a perfect Christmas? Maybe one that reminds you of the perfect Christmases you had in your childhood. One of the things that made it perfect back then was having a White Christmas. How we can define a White Chritmas? Being snow on the ground or snowing on the day of Christmas, the 25th of December.

In past years, here in the heart of Transylvania, in the city of Alba Iulia, we didn't have any White Christmases. So after I watched <b>[Simon Clarck's](https://www.youtube.com/channel/UCRRr_xrOm66qaigIbwFLvbQ)</b> video of <b>[Will you get a White Christmas in 2020?](https://www.youtube.com/watch?v=sh-zWu6dXxo&t=525s)</b> I thought why not try to do the same analysis in the case of my city but because I didn't find the weather data of the weather station of my city and only the ones of the bigger cities from my region, I thought it will be better for me to do an analysis for the region of Transylvania, having the weather data from the weather stations of the three main cities: Cluj Napoca, Deva and Sibiu. 

The weather data from the weather stations (which consisted in precipitations, average temperatures, maximum and minimum temperatures registered from 1950 until 2019) were ordered from the [National Centers for Environmental Information (NCEI - offers access to the most significant archives of oceanic, atmospheric, geophysical and coastal data](https://gis.ncdc.noaa.gov/maps/ncei/). I used the data from 1950 until 2019 because the data for the <b>[AO Index (Arctic Oscillation Index)](https://www.cpc.ncep.noaa.gov/products/precip/CWlink/daily_ao_index/monthly.ao.index.b50.current.ascii.table)</b> and the <b>[NINO3.4 Index (El NINO Index)](https://climexp.knmi.nl/data/iersst_nino3.4a_rel.dat)</b> were available only during this period.

## Cluj Napoca:
[[12  3]
 [ 3  3]]
0.7142857142857143
              precision    recall  f1-score   support

         0.0       0.80      0.80      0.80        15
         1.0       0.50      0.50      0.50         6

    accuracy                           0.71        21
   macro avg       0.65      0.65      0.65        21
weighted avg       0.71      0.71      0.71        21

## Sibiu:

[[8 3]
 [4 3]]
0.6111111111111112
              precision    recall  f1-score   support

         0.0       0.67      0.73      0.70        11
         1.0       0.50      0.43      0.46         7

    accuracy                           0.61        18
   macro avg       0.58      0.58      0.58        18
weighted avg       0.60      0.61      0.60        18

## Deva:
[[14  0]
 [ 4  0]]
0.7777777777777778
              precision    recall  f1-score   support

         0.0       0.78      1.00      0.88        14
         1.0       0.00      0.00      0.00         4

    accuracy                           0.78        18
   macro avg       0.39      0.50      0.44        18
weighted avg       0.60      0.78      0.68        18