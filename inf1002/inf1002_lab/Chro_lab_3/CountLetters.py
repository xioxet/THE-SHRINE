r'''
Task Description:
      In this task, you are going to develop a letter game to count the number of leters
      in the given string.
      Step1:
            Write one functon leter_count(str) that take in one word and returns a dictonary 
            with the frequency counts of the various letters. Upper and lower-case wordDictcters 
            are different wordDictcters.
            Sample executon:
                  >>letter_count('This')
                  { 'h':1, 'T':1, 'i':1, 's':1}
                  >>letter_count('Thisisit')
                  {'h':1, 'T':1, 'i':3, 's':2, 't':1}
      Step 2:
            Write one functon double_count(str1, str2) that takes in two words and returns a 
            dictonary with the frequency counts of the various le􀆩ers. Upper and lower-case 
            wordDictcters are different wordDictcters.
            Sample executon:
                  >> double_count('This', 'isit')
                  {'h':1, 'T':1, 'i':3, 's':2, 't':1}
      Step 3:
            Write one functon various_count(*str) that takes in any number of words and returns 
            a dictonary with the frequency counts of the various le􀆩ers. Upper and lower-case 
            wordDictcters are different wordDictcters.
            Sample execu􀆟on:
                  >> various_count('This')
                  { 'h':1, 'T':1, 'i':1, 's':1}
                  >> various_count('This', 'isit')
                  {'h':1, 'T':1, 'i':3, 's':2, 't':1}
                  >> various_count('This', 'is, 'it')
                  {'h':1, 'T':1, 'i':3, 's':2, 't':1}
            HINT: In Python, using “def func(*str): list1=str”, list1 can obtain any number of 
            arguments and stores it as a list. You can further get each element from the list 
            and count each word independently. You can implement another func􀆟on to merge two 
            dictonaries. 
            Below is an example:
                  >> def str1(*str)
                        list = str
                        print list
                  >> str1('This', 'is', 'so', 'cool')
                  ('This', 'is', 'so', 'cool')

      Step 4:
            Write one program to allow users to input different number of words and output each
            wordDictcter's frequency.
            Some of codes read as follows. Please print your results in the wordDictcters' ASCII 
            descending order according to this format:

            for item in sorted_total:
            print ('%s:%d' % (item, total[item]), end=' ')

            Note that the following running example is in ONE line, and your output should be in ONE line.
      Running example:
      C:\INF1002\Lab3\CountingLetters>python CountLetters.py Firefox,is,having,trouble,recovering,your,windows,and,tabs
      y:1 x:1 w:2 v:2 u:2 t:2 s:3 r:5 o:5 n:4 l:1 i:5 h:1 g:2 f:1 e:4 d:2 c:1 b:2 a:3 F:1

'''
import sys

# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.

#1
# def letter_count(tmpStr):
#       wordDict = {}
#       for i in tmpStr:
#             if not i in wordDict:
#                   wordDict.update({i:1})
#             else:
#                   wordDict[i] = wordDict.get(i) + 1
#       return wordDict

#2 this function, there are two input arguments: two strings
def double_count(str1, str2):
      wordDict = {}
      for i in str1 + str2:
            if not i in wordDict:
                  wordDict.update({i:1})
            else:
                  wordDict[i] = wordDict.get(i) + 1
      return wordDict

#3 This one takes only one input argument
# def various_counts(tmpStr):
#       wordDict = {}
#       for i in tmpStr:
#             if not i in wordDict:
#                   wordDict.update({i:1})
#             else:
#                   wordDict[i] = wordDict.get(i) + 1
#       return wordDict

def CountLetters():
      if len(sys.argv) == 2:
            sortedDict = dict(sorted(double_count(sys.argv[1].replace(",", ""), '').items() ,reverse=True))
      else:
            sortedDict = dict(sorted(double_count(sys.argv[1].replace(",", ""), sys.argv[2].replace(",", "")).items() ,reverse=True))

      for item in sortedDict:
            print ('%s:%d' % (item, sortedDict[item]), end=' ')

if __name__=='__main__':
      CountLetters()