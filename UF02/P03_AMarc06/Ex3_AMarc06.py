def crear_HTML(**kwargs) -> str:
    result = ""
    for i in kwargs:
        result += '<'+i+'>'+kwargs[i]+'</'+i+'>\n'
    return result


print(crear_HTML(p="paràgraf", h1="Títol 1", h2="Títol 2"))
