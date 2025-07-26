# University Course Assignment Optimization 

## Introduction
This repository contains the code and resources for the project "An Application of Graph Optimization-Course Project". The project aims to optimize the University Course Assignment System using graph optimization techniques.
This was a graded project in college under the subject of "Discrete Mathematics of Computer Science"

## Research Problem
The main challenge is to develop an assignment scheme that maximizes the number of courses assigned to faculty members while considering their preferences and category-based constraints. The faculty members are categorized into three groups: x1, x2, and x3, each with different course load capacities per semester.

- x1 faculty members handle 0.5 courses per semester.
- x2 faculty members take 1 course per semester.
- x3 faculty members manage 1.5 courses per semester.

Faculty members can take multiple courses, and a single course can be assigned to multiple faculty members. The goal is to ensure that each course assignment aligns with faculty preferences without exceeding their course load limits.

## Features
- Faculty preference list management
- Course assignment optimization
- Constraint satisfaction for faculty categories and course loads
- Flexibility to modify the maximum number of courses for each faculty category
- Ability to extend the number of faculty categories for a generalized solution

## Constraints and Assumptions
Faculty members must provide their preferences for at least:

- 4 FD CDC (Foundation Courses for Department Core Courses)
- 4 FD Ele (Foundation Courses for Electives)
- 2 HD CDC (Higher Department Core Courses)
- 2 HD Ele (Higher Department Electives)

A professor of category x2 (course limit 1) cannot be assigned only 0.5 courses if assigning 1 course isn't possible.
If the assignment is below the course load limit, it should result in a crash test to ensure valid assignment.

## Contributors 
* Ishita Godani [@ishitagod](https://github.com/ishitagod)
* Trisha L Reddy [@trisha2004](http://github.com/trisha2004)
* Bhuvan Satrasala [@Bhuvans00110](https://github.com/Bhuvans00110)
