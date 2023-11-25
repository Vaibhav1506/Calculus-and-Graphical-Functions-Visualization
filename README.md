# Calculus & Graphical Visualization of Function in Python MySql Connectivity
A project where we used Python and MySql to showcase a tiny yet significant part of the beautiful yet mysterious field of Mathematics - Calculus.

## Coming Soon
- Code Documentation

## Hardware Requirements
- x86 64-bit CPU ([Intel](https://www.intel.com/content/www/us/en/homepage.html) / [AMD](https://www.amd.com/en.html) architecture).
- A minimum of 2 GB RAM (4GB recommended).

## Software Requirements
- [Windows](https://en.wikipedia.org/wiki/Microsoft_Windows) 7 or higher.
- [Mac OS X](https://en.wikipedia.org/wiki/MacOS) 10.11 or higher, 64-bit.
- [Linux](https://en.wikipedia.org/wiki/Linux): RHEL 6/7, 64-bit.
- Almost all python libraries also work in [Ubuntu](https://en.wikipedia.org/wiki/Ubuntu).
- [Python](https://www.python.org/) Latest Version (3.12 as of November 2023).
- [MySql](https://www.mysql.com/) (preferably both Command Line Client and Workbench both of version 8.0)
- [Numpy](https://numpy.org/) Python Library.
- [Matplotlib](https://matplotlib.org/) Python Library.
- [Mysql-Connector](https://pypi.org/project/mysql-connector-python/) Library.

## How to Execute the Code
- Make sure the above Software Requirements are satisfied including libraries.
- For installing libraries, first open Command Prompt(CMD) in Windows or Terminal in Mac OS or other operating systems.
  - For installing numpy, run: **pip3 install numpy**
  - For installing matplotlib, run: **pip3 install matplotlib**
  - For installing mysql-connector-python, run: **pip3 install mysql-connector-python** 
- Download the zip file and unzip it.
- Open the Folder in any code editor.
- Navigate to the file: **Final_CS_Project_Without_Documentation (Version 3.6).py**
- Press F5 or run the code manually.

## Project Information
- Line Count: 1214.
- Code Language : Python (Version 3.12) **(100%)**.
- Code Editor Used : Microsoft [Visual Studio Code](https://code.visualstudio.com/) Editor
- Date Created : 12th September 2023.
- Publish Date (on [Github](https://github.com/)) : 14th November 2023.
- Authors : [Rajveer Vora](https://github.com/RajveerVora) and [Vaibhav Bakshi](https://github.com/Vaibhav1506).
- Number of Contributors : 2
- License Used: [GNU Public License](https://www.gnu.org/licenses/gpl-3.0.en.html) (Open Source Project).

## Output
The general first thing which you will notice after running the code is this :-

![Screenshot 2023-11-21 233145](https://github.com/Vaibhav1506/Calculus-Functions-Visualization-Python-MySql-Connectivity-Project/assets/74455023/6e336bc2-52b0-43a3-bd84-161dc3008d49)

Here you have to enter the given 3 parameters - hostname, username and password of ur MySql database after accepting to run the code by entering "Y" or "y". Clearly there are 5 basic operations - Differentiation, Indefinite Integrals, Definite Integrals, Graphs and Exit. The user can enter the choice number and it further divides into operation type which consists of 5 basic mathematical expressions - Trigonometric, Inverse Trigonometric, Polynomial, Logarithmic and Exponential functions. This is only for the first 3 operations while for the 4th one there are 2 choices - One specifically for polynomials and other for universal (implicit / explicit functions).

1) For example here is the Differentiation part:

![Screenshot 2023-11-21 213003](https://github.com/Vaibhav1506/Calculus-Functions-Visualization-Python-MySql-Connectivity-Project/assets/74455023/f924d848-b262-458a-8bc7-eb1b7d6063d8)

2) Now here is an Indefinite Integral part:

![Screenshot 2023-11-21 213248](https://github.com/Vaibhav1506/Calculus-Functions-Visualization-Python-MySql-Connectivity-Project/assets/74455023/f2661d4d-6cee-41e0-9050-20a6471f07e3)

3) Here is a Definit Integral part:

![Screenshot 2023-11-21 213205](https://github.com/Vaibhav1506/Calculus-Functions-Visualization-Python-MySql-Connectivity-Project/assets/74455023/72b0c3e8-ea05-44a7-83ed-0002e64f1bb4)

4) And here is the Graphing part (both choices):

![Screenshot 2023-11-21 232238](https://github.com/Vaibhav1506/Calculus-Functions-Visualization-Python-MySql-Connectivity-Project/assets/74455023/23b6191f-49a0-4323-b6e9-6ed7bfcbfb29)

![Screenshot 2023-11-21 213833](https://github.com/Vaibhav1506/Calculus-Functions-Visualization-Python-MySql-Connectivity-Project/assets/74455023/ae6e8dcd-af4e-4c3e-a968-d13af8fcd7c5)

Exiting the code will simply display:

![Screenshot 2023-11-21 232328](https://github.com/Vaibhav1506/Calculus-Functions-Visualization-Python-MySql-Connectivity-Project/assets/74455023/c7a33fae-8c7e-4ba0-9756-1dfbc12a112c)

Now for viewing the User History you can simply go to MySQL Command Line Client or Workbench (Latest Version 8.0).

![Screenshot 2023-11-23 201830](https://github.com/Vaibhav1506/Calculus-Functions-Visualization-Python-MySql-Connectivity-Project/assets/74455023/ee8f04e5-b12d-4e17-9f64-33c9c710231e)

![Screenshot 2023-11-24 201035](https://github.com/Vaibhav1506/Calculus-Functions-Visualization-Python-MySql-Connectivity-Project/assets/74455023/ef337702-1cfa-461b-a32f-247fee7de763)

Therefore, you can see the results which the user has entered clearly in an organised and tabular format.

## Changelogs and Version History
Contains various versions of the file from starting alongwith some details and descriptions about the code.The previous version files are availaible in the **Previous Versions** folder.

### Version 3.6 (24th November 2023) [Latest Version]
1. Removed unnecessary comment lines "#type:ignore" (used previously for ignoring warnings).
2. Removed redundant guidelines and made it user - friendly.

### Version 3.5 (21st November 2023) 
1. Fixed an issue in Matplotlib display of any function entered by the user.
2. Fixed an error in displaying part of polynomial function as label and along y - axis in normal form in graphing part of the program.
3. Added Name Error Handling.
4. Added a Rule regarding entering of expressions in the Graphing part of program.
5. Added the expression entered in graphing part as answer to be inserted in database since using hyphens will result in duplication errors. This is due to the fact that the Answer column in the MySql database has UNIQUE constraint applied on it and since every graph will have hyphens has answer therefore we decided to change to the expresison entered by the user itself.

### Version 3.4 (18th November 2023)
1. Improved Error Handling of mysql connection.
2. Added better exit option.

### Version 3.3 (13th November 2023)
1. Added two messages displaying whether the result has been fetched from database or added to database.

### Version 3.2 (4th November 2023)
1. Documentation removed as we plan it to write it in a seperate code so as to make the code look clean.
2. Reduced the number of lines by adding list comprehension.
3. Removed Searching and Full viewing of user history function for MySql to make the code simple.

### Version 3.1 (2nd November 2023)
1. Connectivity Search is now integrated in main code.

### Version 3.0 (2nd November 2023)
1. Updated connectivity search for working.

### Version 2.9 (28th October 2023)
1. Fixed some indentation errors.
2. Removed some unneccessary lines from rules.  

### Version 2.8 (24th October 2023)
1. Added answer history storing system where is stores the type of functions being chosen and evaluated along with the answer.
2. Fixed an issue in LaTeX display of differentiation.

### Version 2.7 (20th October 2023)
1. Fixed an issue in display of log(x) or ln(x) graph by adjusting its arange() and linespace().

### Version 2.6 (18th October 2023)
1. New graph function is now integrated in the code.
2. Complex and Special functions like Alpha function, Lambert W , Riemann Zeta and Factorial Functions, etc. are not supported.
3. Fixed an issue in the polynomial integration.

### Version 2.5 (15th October 2023)
1. Supports Modulus Function
2. Better visualization of Polynomial functions (of n - degree where n can be input by the user) showing the roots. 

### Version 2.4 (12th October 2023)
1. New graph function is added allowing more sophisticated and customizable functions to be displayed.
2. It involves implicit functions over a wide range along a fixed domain.
3. Modulus function is not yet supported.

### Version 2.3 (8th October 2023)
1. Code Documentation along with rules added.
2. A welcome message is also added.

### Version 2.2 (1st October 2023)
1. LaTeX display is now supported for Differentiation part.
2. Fixed a minor issue in LaTeX displaying of Inverse Trigonometric Function's parentheses and formulae.

### Version 2.1 (29th September 2023)
1. SQL connectivity's basic structure is implemented for storing the user's history in a database.

### Version 2.0 (29th September 2023)
1. Fixed a minor issue in exponential function display in LaTeX.

### Version 1.9 (28th September 2023)
1. LaTeX display is now supported for Definite Integrals' part.

### Version 1.8 (21st September 2023)
1. The evaluated expressions were difficult to understandable since its written in a machine linear form where one can have a difficulty in understanding.
2. Hence we implemented LaTeX display using matplotlib especially for the functions in Indefinite Integral Calculus in the main code for better view.

### Version 1.7 (21st September 2023)
1. Definite Integration part is now supported.
2. It is evaluated on the basis of fundamental theorem of Calculus.

### Version 1.6 (17th September 2023)
1. Graphical Function now supports Trigonometric Functions(alongwith Inverse functions also).
2. Graphical Functions Visualization is now integrated in the main code.
3. Random selection of similar results is removed to make the code less complicated.
### Version 1.5 (16th September 2023)
Initially we had no plans to add graphical visualization of functions. But we thought to implement it at a standard level. Hence the basic structure was created for Tangent Function.

### Version 1.4 (14th September 2023)
1. Random selecting result is now supported for Differentiation.

### Version 1.3 (14th September 2023)
1. Indefinite Integration evaluation part was written.
2. Indefinite Integration part is supported for all the 5 basic types of function (in linear form) as written for Differentiation earlier.
3. Random choice is added to display random results from a set of results which are equivalent to one another (only for Indefinite Integration).

### Version 1.2 (13th September 2023)
1. Function to convert to superscript format (for powers and exponentials) was defined. 
2. Differentiation evaluating part was written.
3. Differentiation is now supported for 5 basic types of functions - Inverse Trigonometric, Logarithmic, Basic Algebraic, Trigonometric and Exponentials.
4. All the expressions are of linear form in order to keep the code structure simple.

### Version 1.1 (13th September 2023)
1. Menus and other conditional blocks were implemented.
2. 3 Basic types of Operations are defined - Differentiation, Integration (Both Indefinite and Definite)

### Version 1.0 (12th September 2023) [First Version]
1. A basic and rough structure of the code was defined.

