# Will we get a White Christmas in Transylvania in 2020?

What makes a perfect Christmas? Maybe one that reminds you of the perfect Christmases you had in your childhood. One of the things that made it perfect back then was having a White Christmas. How we can define a White Chritmas? Being snow on the ground or snowing on the day of Christmas, the 25th of December.

In past years, here in the heart of Transylvania, in the city of Alba Iulia, we didn't have any White Christmases. So after I watched <b>[Simon Clarck's](https://www.youtube.com/channel/UCRRr_xrOm66qaigIbwFLvbQ)</b> video: <b>[Will you get a White Christmas in 2020?](https://www.youtube.com/watch?v=sh-zWu6dXxo&t=525s)</b> I thought why not try to do the same analysis in the case of my city but because I didn't find the weather data of the weather station from my city and only the ones of the bigger cities from my region, I thought it will be better for me to do an analysis for the region of Transylvania having the weather data from the weather stations of the three main cities: Cluj Napoca, Deva and Sibiu.

But first, how can you predict the weather in a large time span, like a month? As Simon explained, the atmosphere is a horrific and complicated set of interacting fields like wind and temperature, humidity and pressure and it’s all too much to keep in mind when trying to create systems to predict the weather. Scientist invented statistical tricks like Principal Component Analysis to draw out the basic things the atmosphere is doing at any given time. For example in the northern hemisphere, the air pressure is best described using something like the Arctic Oscillation Index (AO Index – is a measure of how the wiggly the jet stream is and how likely it is to see extremely cold air spill out from the arctic to the middle latitudes). The Arctic Oscillation has a pattern associated with it which tells us about the strength of the jet stream and a number associated with it, it’s index, and the index basically says if the jet is stream anonymously strong and stable or anonymously weak and wobblily. So if you want to describe what the atmosphere in the northern hemisphere is doing at any one time, at least at the surface, then your best bet is the Arctic Oscillation Index. The one number that sums up the most possible variability in the northern hemisphere.

If you are more interested in oceans rather then atmospheres then the principal component of sea surface temperatures is the EL NINO SOUTHERN OSCILLATION (ENSO). You can represent the strength of ENSO with the help of the index NINO 3.4.

These indices vary on much longer time scales. For example the temperature in a location the temperature may vary day to day or even within a day while the AO Index varies smoothly over weeks and months and that means that with enough data you can predict what it will be quite a few weeks into the feature further than you can predict the weather. So, we can predict what the AO Index and Nino3.4 will be in December (~ 0 : ~ -1.5).

As a result, you can look through past years at the relationships between these indexes and the possibility of a place receiving a White Christmas or not both within the month of December so you can get a much stronger statistically relationship.

The weather data from the weather stations (which consisted in precipitations, average temperatures, maximum and minimum temperatures registered from 1950 until 2019) were ordered from the [National Centers for Environmental Information (NCEI - offers access to the most significant archives of oceanic, atmospheric, geophysical and coastal data](https://gis.ncdc.noaa.gov/maps/ncei/). I used the data from 1950 until 2019 because the data for the <b>[AO Index (Arctic Oscillation Index)](https://www.cpc.ncep.noaa.gov/products/precip/CWlink/daily_ao_index/monthly.ao.index.b50.current.ascii.table)</b> and the <b>[NINO3.4 Index (El NINO Index)](https://climexp.knmi.nl/data/iersst_nino3.4a_rel.dat)</b> were available only during this period.

With the help of the data collected above, I built three data sets, one for each city, and I tested the performance of different models on these data sets, such as Logistic Regression, Support Vector Classifier, Random Forest Classifier, and XGBoost Classifier, with the help of StratifiedKFold cross validator, and after that, I choose the best performing model to try to predict the estimated probability regarding the binary outcome: if these cities will have a White Christmas (1) or not (0) in 2020.

The scores obtained for the models were overall good. Probably if I could have a larger number of values, the scores would be better. We also have to take into account the fact that overall the time span for which the weather data was registered is small. For temperatures and precipitation in some weather stations like the ones from Great Britain we can find the a larger span of data like from the beginning of the 18th century but for indexes like in our case, the AO Index and NINO3.4 Index, I could only find data from 1950 until the present day and if you are interested in only one day of the year, automatically the range of the data will be smaller.

#### For predicting the probability of having a White Christmas in Cluj Napoca, the result obtained was:
* ```array([[0.88, 0.12]])``` : We can state that there is a probability of 88% that Cluj Napoca will not have a White Christmas in 2020.

#### For predicting the probability of having a White Christmas in Sibiu, the result obtained was:
* ```array([[0.8497904 , 0.15020959]], dtype=float32)``` : We can state that there is a probability of 85% that Sibiu will not have a White Christmas in 2020.

#### For predicting the probability of having a White Christmas in Deva, the result obtained was:
* ```array([[0.69624656, 0.30375344]])``` : We can state that there is a probability of approximately 70% that Deva will not have a White Christmas in 2020.

Overall, based on our findings, we can conclude that this year there will not be a White Christmas in Transylvania.

Now, after Christmas, I can state that the predictions were accurate because during Christmas time we had slightly warm weather for this time of the year, and it also rained.
