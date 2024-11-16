# Ejercicio 1: Extraer todos los enlaces de una pagina web
## Utilize la biblioteca BeautifulSoup junto con requests para extraer todos los enlaces (etiquetas <a>) de una pagina web y almacenarlos en una lista. 
## Buscar la totalidad de enlaces rotos vs enlaces correctos

import threading
import queue
import requests
from bs4 import BeautifulSoup

# Tecnologia; Neurociencias; Ortesis y Protesis
urls = [#'https://sejuve.queretaro.gob.mx/out/home/sejuve', 
        'https://oferta.unam.mx/',
        #'https://www.posgrado.unam.mx/'
        ]

working_links = []
broken_links = []

for url in urls:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href and href.startswith('http'):
                try:
                    link_response = requests.get(href)
                    if link_response.status_code == 200:
                        working_links.append(href)
                    else:
                        broken_links.append(href)
                except Exception as e:
                    broken_links.append(href)
                    print(f"Fallo al obtener {href}, Error: {e}")
    except Exception as e:
        broken_links.append(href)
        print(f"Fallo al obtener {url}, Error: {e}")

print(f"Links que funcionan: {working_links}\n")
print(f"Links que no funcionan: {broken_links}\n")
print(f"Todos los enlaces (etiquetas <a>) en el sitio web: {links}\n")


# I am getting an exception, which tells me that I might not even get the links. It seems like the object 'Response' wasn't designed to have a length, the problem ...
# ... is that I am not even using length anywhere in my code. Maybe could it be an inner working of the 'in' statement? As I am working with an actual loop it would make ...
# ... sense that internally 'python' is trying to know how many elements I have to begin with. 

# It wasn't that. For what the rubber duck tells me the 'in' statement goes for each element without relying on the size of the iterable in any case. 

# The rubber duck tells me that any response in 'BeautifulSoup' contains several attributes, in which some are 'content', 'status_code' or 'headers'. It makes sense that ...
# ... when I don't specify the actual content I want in the 'soup' variable, python gets confused about what to do. I know that 'status_code' can help me to take on the ...
# ... other part of the problem, which is knowing which links are still functioning and which of those is broken. Maybe I could work on the same loop separating them on ...
# ... two lists. 

# It seems that the line of 'soup = BeautifulSoup(respuesta.content, 'html.parser')' doesn't work very well with broken html, which is a problem. There seems to be ...
# ... multiple ways to parse a page, but what is parse to begin with? According to the rubber duck, "parsing is the act of analyzing syntax". If we recall that an html ...
# ... file has its unique tags that describe how a page is constructed, making a "parsing tree" is therefore putting that representation of the page into the html ...
# ... source code that we already know and need. The thing that I don't understand here is if Google already gives us that information with the "web dev tools" ...
# ... 'BeautifulSoup' does the work twice? or does it copy it from Google? or does it transform it into a "visually friendly" way for the programmer to work with? ...
# ... a combination of all of them? 

# As an alternative for 'html.parser' we have xml, that is why I installed the 'lxml' library, yet what is xml to begin with? It sounds like an alternative for html ...
# ... but that seems unlikely, as for what I recall javascript, html and css is literally all over the internet, so why build something that won't work in most of the ...
# ... cases? According to the rubber duck XML stands for (eXtenible Markup Language), which comes really close to the Hyper-Text Markup Language (html), in which the ...
# ... main difference is that HTML is concerned with how the data looks while XML is a flexible way to store and transport that data more efficiently.  