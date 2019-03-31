"# GraphTheoryProject_2019" 
The Shunting python file uses the shunting algorithm to change an infix to postfix.
The Thompson python file uses Thompson's construction to create states for the postfix and combine each character
together to make one series of states with an initial state and an accept state with specified routes through each 
states. 
The Match python file is the file i use to call the other files and read in a set of strings and infixes. It also
will go through all the specified states when comparing the string to the postfix. There is a method that passes 
through any empty arrows(labels).