# ExcelScript

Suppose you copied multiple lines of text in a single cell inside excel or google spreadsheet and now you want each line in the cell in a new row cell, then this script is for you.

Steps:
1) Run this command in a terminal pip3 install xlsxwriter
2) Copy all the lines that you have in one cell to a file called 'testfile'.txt in the directory and navigate to that directory.
3) Clone this repo in the directory where you copied 'testfile.txt'. Run the script 'python3 excelwrite.py'. You will find a new spreadsheet called demo.xlsx created in this directory.
4) Open 'demo.xlsx'. You will see that each newline is now in a new row. You can now copy this and paste it into the spreadsheet that you were working on.
