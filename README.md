# Road-To-Wave-Function-Collapse
#### This is a repo recording my progress in wave function collapse using python!
After watching the video on Wave Function Collapse, on the You-Tube channel 'The Coding Train', I made up my mind to create this program.
So, I am making my way towards it!
<br>
## Part 1 - Random Map Generator
The first part in this algo was a random map generator. A program that takes few roads as inputs and generates a maze like pattern based on simple set of rules!
<br>
<br>
<img src="map gen\up.png">
<img src="map gen\down.png">
<img src="map gen\left.png">
<img src="map gen\right.png">
<img src="map gen\blank.png">
<br>
<br>
Although, my current algo is less spontaneous, it is fine for now. 
I will however work on improving it, and making it to be more spontaneous.
The other limitations to this algo is that, it is designed particularly for a fixed set of grid. That is, if you want output to be of 5x5 grid, you will need to include more grids. By default it works for 3x3.
My next, step is to make it more sponataneous and workble for user speific grids.
<br>
## Part 2 - Random Map Generator for N grid
<br>
In the last version, i.e. random-map-generator.py we could only generate maps for a 4x4 grid. However, in this update, i.e. random-map-generator-2.py we can generate map for any number of N. For this I added iteration in Python Tkinter Module's grid().
I count it as a crucial step as later on when we will actually be working with the actual images and generating patterns based on that image, we will have to be flexible in terms of size.
Here, are some screenshots for the maps that I generated using my algorithm:
<br>
<br>
<img src="map gen\2-1 (5).png">
<img src="map gen\2-1 (1).png">
<img src="map gen\2-1 (2).png">
<img src="map gen\2-1 (3).png">
<img src="map gen\2-1 (4)blank.png">
<br>
For the next part I will working on 3x3 sudoko generator, and later on to an N-size sudoko generator
<br>
## Part 3 - 3x3 Sudoko Generator
