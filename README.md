# Sea level Prediction

## Project Definition:
Sea level prediction is essential for the design of coastal structures and harbor operations. In this project we will predict sea level.

## Requirements : 
We use pandas , numpy , datetime , matlplotlib  libraries and scipy to import linregress .

## Explaining implementation of task :
In this task we :
-	 import libraries .
-	read excel data using pandas read_excel(path).
-	 preprocessing for data set that convert year column to numerical data by     independent on fixed days and all months exist along all years from 1880 to 1962 we do that by using numpy arrange start by year 1880 and end by 1963+(1/12)*4 and go through 1/12 step  and put the result into variable X, then we get second column and put into variable y .
-	Make scatter to visualize sea level in years put X in x_axis and y in y_axis 
-	Using scipy library we use linregress to predict model and get Slope ,Intercept, Standard deviation, rvalue , pvalue  and Intercept standard deviation .
-	Make the line go through the year 2000 to predict the sea level rise in 2000 by using numpy arrange .
-	Multiply slope by each xi and sum to each xi in features to get the result for each xi
-	Finally we make scatter plot to get the final result and x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.
