# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to
#page = '<div id="top_bin"><a href="http://udacity.com">Hello world</a>'
'<div class="udacity float-left"'
# that your code still assigns the same value to the variable 'url', 
# and therefore still prints the same thing.
# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=') #finding the position of '<a href' 
#print start_link
index=page[start_link:].find("http://")
#finding the position of 'http' using '<a href' index 
#print index
index2=page[start_link+index:].find('"')
#finding position of ""(quotes) using both  index positions
#print index2
url=page[start_link+index:start_link+index+index2]
#assigning the value to url variable
print (url);
#print page[start_link+index+url:]

