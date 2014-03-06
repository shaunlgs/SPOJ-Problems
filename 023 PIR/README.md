Problem 23. Pyramids

Problem code: PIR<br>
[http://www.spoj.com/problems/PIR/](http://www.spoj.com/problems/PIR/)

> Recently in Farland, a country in Asia, the famous scientist Mr. Log Archeo discovered ancient pyramids. But unlike those in Egypt and Central America, they have a triangular (not rectangular) foundation. That is, they are tetrahedrons in the mathematical sense. In order to find out some important facts about the early society of the country (it is widely believed that the pyramid sizes are closely connected with Farland's ancient calendar), Mr. Archeo needs to know the volume of the pyramids. Unluckily, he has reliable data about their edge lengths only. Please, help him!
> 
> **Input**
> 
> t [number of tests to follow] In each of the next t lines six positive integer numbers not exceeding 1000 separated by spaces (each number is one of the edge lengths of the pyramid ABCD). The order of the edges is the following: AB, AC, AD, BC, BD, CD.
> 
> **Output**
> 
> For each test output a real number - the volume, printed accurate to four digits after decimal point.
> 
> **Example**
> 
> Input:
> 
> 
> 2
> 1 1 1 1 1 1
> 1000 1000 1000 3 4 5
> 
> Output:
> 
> 
> 0.1179
> 1999.9937

Refer [http://www.had2know.com/academics/tetrahedron-volume-6-edges.html](http://www.had2know.com/academics/tetrahedron-volume-6-edges.html) for methods of calculating area of tetrahedron given only edges of 6 sides of tetrahedron.

<center>![](http://www.had2know.com/images/tetrahedron-6-edges.png)</center>

a, b, c, d, e, and f are the edges of the tetrahedron. **First, we have to find the coordinates of vertices of the tetrahedron.** There are four vertices, so we have to find 4 coordinates.

Each coordinate values are as follows:

coordinate 1: (0, 0, 0)<br>
coordinate 2: (0, c, 0)<br>
coordinate 3: (x, y, 0)<br>
coordinate 4: (p, q, r)<br>

where c is the length of edge c,<br>
y = (a<sup>2</sup> + c<sup>2</sup> - b<sup>2</sup>) / (2c), <br>
x = √(a<sup>2</sup> - y<sup>2</sup>), <br>
q = (c<sup>2</sup> + e<sup>2</sup> - d<sup>2</sup>) / (2c), <br>
p = (a<sup>2</sup> + e<sup>2</sup> - f<sup>2</sup> - 2qy) / (2x),<br>
r = √(e<sup>2</sup> - q<sup>2</sup> - p<sup>2</sup>)<br>

After finding 4 coordinates of the vertices, refer [http://www.had2know.com/academics/tetrahedron-volume-4-vertices.html](http://www.had2know.com/academics/tetrahedron-volume-4-vertices.html) to find area of tetrahedron from the vertices.

**Area = (1 / 6) * determinant of simplified 3 x 3 matrix<br>**

The simplified 3 x 3 matrix of tetrahedron with vertices (a, b, c), (d, e, f), (g, h, i), and (p, q, r) is ((a - p, d - p, g - p), (b - q, e - q, h - q), (c - r, f - r, i - r)), to find the determinant, refer diagram below:
![](http://www.allmathwords.org/equations/d/determinant3x3.png)