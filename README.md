## Task description
Use English SpaCy lib, find all tokens with only digits and all proper nouns (PROPN, aka, personal nouns ) in the text, count it and output it right-aligned in the HTML.
For example, for the text "we need 2 tickets to Dublin, and 1/2 a spoon of milk" read from the stdin (use python myprogram.py < input.txt >output.html ) the program should output that "2" was found twice (output "2"), "1" was found once (output "1"), "Dublin" was found once (output "1").
Display it as an HTML table with 2 columns: the first column for the entry, and the second column for the number of times it was found.
Remember that it will be much easier to set up SpaCy on Colab rather than on a Windows machine.
