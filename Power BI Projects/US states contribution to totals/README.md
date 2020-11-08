# The US states contribution to total sales

I tried solving the challenge from [2020 Week 20: How much do these states contribute to the total?](http://www.workout-wednesday.com/2020w20/) that also had a [dataset](https://data.world/annjackson/20194-tableau-superstore) needed for it to be solved.

The challenge was to create a dashboard that allows the user to select any state(s). Clicking a state in the map will add them to the proportional set. Then on the right sidebar, allow users to select from the list of selected states which will remove them from the proportional set. 

I couldn’t figure out yet in Power BI how to add a state to a proportional set and then create a sidebar to allow users to choose the states which could then be removed from the proportional set. Instead, I created a shape map with the states of the US taking into account the amount of sales, orders, and customers made by each one compared their total amounts. I also made two gauges for each type of information to present the amount, respectively the percentage of the selected state in their total amounts made in the US.

The end result was:

<img src='US states contribution to total sales.png'>

