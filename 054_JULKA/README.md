Problem 54. Julka

Problem code: JULKA<br>
[http://www.spoj.com/problems/JULKA/](http://www.spoj.com/problems/JULKA/)

**Question**:
> Julka surprised her teacher at preschool by solving the following riddle:
> 
> Klaudia and Natalia have 10 apples together, but Klaudia has two apples more than Natalia. How many apples does each of he girls have?
> 
> Julka said without thinking: Klaudia has 6 apples and Natalia 4 apples. The teacher tried to check if Julka's answer wasn't accidental and repeated the riddle every time increasing the numbers. Every time Julka answered correctly. The surprised teacher wanted to continue questioning Julka, but with big numbers she could't solve the riddle fast enough herself. Help the teacher and write a program which will give her the right answers.
> 
> **Task**
> 
> Write a program which
> 
> - reads from standard input the number of apples the girls have together and how many more apples Klaudia has,
> - counts the number of apples belonging to Klaudia and the number of apples belonging to Natalia,
> - writes the outcome to standard output
> 
> **Input**
> 
> Ten test cases (given one under another, you have to process all!). Every test case consists of two lines. The first line says how many apples both girls have together. The second line says how many more apples Klaudia has. Both numbers are positive integers. It is known that both girls have no more than 10100 (1 and 100 zeros) apples together. As you can see apples can be very small.
> 
> **Output**
> 
> For every test case your program should output two lines. The first line should contain the number of apples belonging to Klaudia. The second line should contain the number of apples belonging to Natalia.
> 
> **Example**
> 
> Input:<br>
> 10<br>
> 2<br>
> [and 9 test cases more]<br>
> 
> Output:<br>
> 6<br>
> 4<br>
> [and 9 test cases more]<br>

**Explanation:**<br>
For each test cases, there are two input lines, first line is the number of apples both Klaudia and Natalia has (x). The second line is the number of apples Klaudia has more than Natalia (y).

For each test cases, there should be two output lines, first line is the number of apples Klaudia has (k) and the number of apples Natalia has (n).

to find n:<br>
n = (x - y) / 2

to find k:<br>
k = x - n
