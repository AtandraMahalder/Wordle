# Wordle
This accompanying strategy and given program can be used to get fast and near accurate solutions to Wordle. 

First try out the following guesses: brick, glent, jumpy, vozhd, waqfs

From these guesses we can determine the letters in our desired words and if possible their positions.

Next run the accompanying script. 

The script will ask for the number of lines of information about letters and then information about the letters.

For information about letters, in each line write the letter deduced to be occuring in the final word and if applicable its position in the desired word. For example, let's say we know our desired word has t in the 5th position and the letters s, n, o, u occur in it. Then our input should be,

5

t 5

s

n

o

u

You will get a few guesses as to what's the best word that could be the desired final guess from which you must choose the best guess (which is likely to be the most commonly occuring word out of all the guesses)
