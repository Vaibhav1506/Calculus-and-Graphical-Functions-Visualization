# Calculus & Graphical Visualization of Function in Python MySql Connectivity
A project where we used Python and MySql to showcase a tiny yet significant part of the beautiful yet mysterious field of Mathematics - Calculus.

## Coming Soon
- Documentation
- Output (Screenshots)
- Output Documentation

## Hardware Requirements
- x86 64-bit CPU ([Intel](https://www.intel.com/content/www/us/en/homepage.html) / [AMD](https://www.amd.com/en.html) architecture).
- a minimum of 2 GB RAM (4GB recommended).

## Software Requirements
- [Windows](https://en.wikipedia.org/wiki/Microsoft_Windows) 7 or higher.
- [Mac OS X](https://en.wikipedia.org/wiki/MacOS) 10.11 or higher, 64-bit.
- [Linux](https://en.wikipedia.org/wiki/Linux): RHEL 6/7, 64-bit.
- Almost all python libraries also work in [Ubuntu](https://en.wikipedia.org/wiki/Ubuntu).

## Code Information
- Line Count: 1216.
- Code Language : [Python 3.12](https://www.python.org/) (100%).
- Date Created : 12th September 2023.
- Publish Date (on [Github](https://github.com/)) : 14th November 2023.
- Authors : [Rajveer Vora](https://github.com/RajveerVora) and [Vaibhav Bakshi](https://github.com/Vaibhav1506).
- License Used: [GNU Public License](https://www.gnu.org/licenses/gpl-3.0.en.html) (Open Source).

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

