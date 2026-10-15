letter = '''dear <|name|>
     you are selected
             <|date|>'''

print(letter.replace("<|name|>","Alok").replace("<|date|>","27 oct 2030"))