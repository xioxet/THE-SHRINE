r'''
Task Description:
In this task, you are going to design one program to check the popular characters
in a given string. You need to write one program to calculate the top 5 most 
frequent characters. The following are some hints that may help you design this program. 
	. String has a cool function that you can use to return a copy of the string 
     in which all case-based characters have been lowercased. 
	. To get the top 5 most frequent characters after sorting them, you need to 
     extract all the characters first and figure out one way to calculate the frequency 
     of each character. Then select the top 5 characters. 
	. The output must in the descending order of character frequency. If there are 
     characters with the same frequency, they must be printed in ascending ASCII order.
	. Print out the top 5 characters and their counts in the screen. (Your output should be in one line)

Running Examples:
C:\INF1002\Lab2\CountPopularChars>python CountPopularChars.py sdsERwweYxcxeewHJesddsdskjjkjrFGe21DS2145o9003gDDS
d:7,s:7,e:6,j:4,w:3
'''
import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def CountPopularChars():
     string = sys.argv[1].lower()
     counter = {}

     for character in string:
          if character in list(counter.keys()):
               counter[character] += 1
          else:
               counter[character] = 1
          
     counter = sorted(counter.items(), key=lambda item: (-item[1],item[0]))
     final_string = ""

     for i in range(0,5):
          current_char = counter[i]
          final_string += f"{current_char[0]}:{current_char[1]}"

          if i != 4:
               final_string += ","


     print(final_string)
          


if __name__=='__main__':
      CountPopularChars()
      
