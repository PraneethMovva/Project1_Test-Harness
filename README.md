# Project1_Test_Harness

## Praneeth Movva             (pmovva1@stevens.edu)

## URL:  https://github.com/PraneethMovva/project1

## Hours Worked
Worked for around 22-30 hours

## A Description on How I tested my code
 I have used git bash in the folder where I have done my project and using the help of python documentation, git documentation and other sources I was able to get some help when in doubt and I have used git bash commands to first check how a particular command actually work and try to implement the same thing in my code and later used the commands using the python and was able to get the similar kind of output. like the "wc foo" gave me the same output when I gave "python wc.py foo" and I have used several test cases to test all the programs and used a lot of trail and error and was finally able to get it .

## Bugs or Issues I couldn't resolve
No

## Difficult Issue and How I solved it 
I couldn't find what is wrong with the test case for wc as my expected output and actual output are similar but still the test.py file keep showing it as output mismatch then later I have figured that it is taking some extra space and then used the split command and then the problem was resolved

While trying to write an extension for the wordcount program I had used an extension called -occurrences where I find if a particular word is there in the given file and gives me how many times the same word is repeated in the file. I had to figure out a way on how to use other extensions together with occurrences like using wc with 2 files and it gives the total of the both files but I had encountered lot of errors/problems when I tried to implement both of them together I usually got wrong output or either one of it couldn't work then I had gone through web and searched a little. Then I have implemented a new function for occurrences and also slightly changed the wc function in such a way that I can't get confused and in the main function I had to make sure all the types were correct. There are few more things like I had to make sure that occurrences work when two files were given and also prints out a total of the occurrences from both the files. This I could do it but it kept on giving total for even one file as well and had to go through all the code to see what went wrong and tested it using trail and error then finally able to rectify it

## Extensions
I have implemented a total of 4 extensions. Out of which 3 extensions are for WC and 1 extension is for gron. To use the extension first you need to have the total python file(codes) and then you can type the following commands in the bash terminal 
### 1. python wc.py foo yo    (To get word count of both the files and their total you can also use more files if you want)
### 2. python wc.py -lw foo   (It just shows the line and words there in a file)
### 3. python wc.py -occurrences bye yo (It shows how many occurrences of bye are there in 'yo' file)
### 4. python gron.py --obj o order.json     (this helps to use o as the base rather than using json as default)
### Those are the commands to test them out and also try to experiment to use others as well like python wc.py -l foo etc but remember to have an appropriate file for each of the command to work like you need to have some content on each file for wc to work but for gron you need to have a json file where the file should contain a content in the form of dictionary because only then the gron function is actually going to be useful or you would just get json = {}; two curly braces and also the same thing with ungron aswell.
