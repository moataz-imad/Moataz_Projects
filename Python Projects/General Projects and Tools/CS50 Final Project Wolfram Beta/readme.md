# Wolfram Beta (Mathematical Webpage)

## Video Demo: https://youtu.be/x7WdDiAsahc

## Description:

This project is created using Python, Flask, HTML, CSS, and JavaScript.
The project is a mathematical Webpage that find the solution for any given expression\*, and graph it.
The expression can be polynomial, logarithmic, exponential, or any combination of them.
The project will mostly use the Bisection Method to find the root

### Project Features:

-   The algorithm will try up to 3 steps to find the solution (the harder the equation the more steps required).
-   The program can determine automatically a suitable range for the graph, that will show roots with spacing.
-   The program will estimate how complex the graph will be and based on it will determine number of points that make up the graph (50 or 500 points)

## Functions:

### calc function from calc.py:

Expects an equation, range of calculation, and accuracy.

-   processes the equation into an evaluatable format (i.e. instead of x^2 it will be changed into x\*\*2)
    this processing is done using the rules in the file 'mathrules.csv'.
-   will use the Bisection Method to try and find a solution
-   if a solution was found, it will return the solution (x @ y≈0), will return a boolean solved=True
-   otherwise, it will return 0, and boolean solved=False (means that 0 is meaningless)
-   accuracy is used in calculation to detemine how close should y be to 0 be considered as a valid solution. I went for 0.001

### SOLVE function from calc.py:

Expects an equation, accuracy, and optionally a custom range for calculations

-   if the custom range is provided, the range will be devided into two parts, and both will be inserted into the calc funciont to find solutions
-   if no range was provided, calc will run over the two periods [-500,0] and [0,500], which might contain the solutions
-   if there are two solutions, it will check if there are far from each others, if not they will be considered same solution ( for example before adding this step the function x^2 without range gave 2 solution 0.001 and -0.001 instead of 0)
-   if two far away solutions were found, it will determine the ploting range to be [lower - 10%L , Upper + 10%L]; where L is the total distance between solutions.(solution is labeled by this emoji:👌)
-   if one solution was found the plotting range will be from the solution ± 5 to 0 ∓ 5 based on the sign of the solution.
-   if there are no solutions found, it will try to see if there are any point that touches the x-axis and does not cross it: if the closest point to the x axis is close enough it will be considered as a solution step 2 and this solution is labeled by this emoji:🙂
-   if still no solution it will try to find if the curve ever cross the x-axis by multiplying y values with y* values where y* is y but shifted one value upward. based on the fact that the multiplication of the same signed values will return postive values, any negative value mean that there is a difference in sign between y and y\* ; ie. y will cross the x-axis at that point.
    then will use bisection method to find the exact solution between them (solution is labeled by this emoji:😅)
    this method has a large potential find many solutions, not just two. but that was out of the scope of this project
-   if there are no solutions still, it will return no solution was found and will plot the graph (response is labeled by this emoji:🙁)
-   if there are any prohibeted values like sqrt(-1) and 1/x, it will return an error (response is labeled by this emoji:❌)
-   SOLVE will return a series of x,y along side the graphing range and the solutions

## WorkFlow:

The work flow for the website is as follow:

-   user will enter equation alongside the optional calculation range
-   when the user click = or press enter, this will send a check request to the server (using javascript) with the equation and the range
-   Equation will be inserted into python, using flask, along side with the calculation range
-   the equation will be inserted into SOLVE
-   SOLVE will return x,y and solution(s).
-   x,y will be aranged into a specificly shaped series that will be inserted into javascript
-   series will have a header and will be returned into javascript.
-   in javascript, the data will be stored in a variable and used to populate google chart which was obtained from google
