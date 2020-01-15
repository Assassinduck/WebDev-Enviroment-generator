
#!/usr/bin/env python3


import boilerplates

filename_Html = input("""What do you want to name you HTML file?
if empty - name will be: index.html (reccomended for first file)""")

filename_Css = input("""What do you want to name you Css file?
if empty - name will be: style.css (reccomended for first file)""")

filename_Js = input("""What do you want to name you Js file?
if empty - name will be: index.js (reccomended for first file)""")



def main():
    
    if(filename_Html == ""):
        with open("index.html", "w") as file:
            file.write(boilerplates.html_boilerplate)
    else:
        with open(filename_Html + ".html", "x") as file:
            file.write(boilerplates.html_boilerplate)

    if(filename_Css == ""):
        with open("style.css", "w") as file:
            boilerplates.cssPath = filename_Css
            file.write(boilerplates.css_normalize)
    else:
        with open(filename_Css + "css", "w") as file:
            file.write(boilerplates.css_normalize)

    if(filename_Js == ""):
         with open("index.js", "w") as file:
            boilerplates.jsPath = filename_Js 
            file.write(boilerplates.js_Boilerplate)
    else:
         with open(filename_Js + ".js", "w") as file:
            file.write(boilerplates.js_Boilerplate)


main()
