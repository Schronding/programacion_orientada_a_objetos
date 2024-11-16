from bs4 import BeautifulSoup

with open("home.html", 'r') as html_file: 
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find('h5')
    print(tags)
    
# What I don't understand here is that if I am already telling my 'open()' function that I want to read the local file, why on 'content' I need to use the method 'read()' ...
# ... again?

# As we need to make use of that content, we need to pass the content to the constructor 'BeautifulSoup' so we can use it freely as a variable, the thing is that I don't ...
# ... understand why we couldn't use 'content' directly. 

# According to the rubber duck, content requires the '.read()' method on the 'html_file' in order to have the contents stored in a variable, however, these information is ...
# ... in a plain string, when we use the 'BeautifulSoup' constructor it seems that we have a better navigation through the 'html_file', as it analizes the string, ...
# ... transforms it into a parse tree and then allows you to have access to methods such as 'find' or 'find_all' that are not directly available in a plain string. 