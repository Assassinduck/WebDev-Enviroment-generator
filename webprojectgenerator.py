
#!/usr/bin/env python3

import wget
import os
import time


def main():

    extention_Condition = input(
        "Will you be using an framwork in this project? [Y]es or [N]o ?")
    extention_Condition = extention_Condition.lower()

    if(extention_Condition == "y"):
        framework_q = input("""Which framework do you want to use?
         [V]ue - [R]eact - [C]at """)
        framework_q = framework_q.lower()

        if(framework_q == "v"):
            print("Vue n shit")
            time.sleep(1)
            return
        elif(framework_q == "r"):
            print("Rect and shit")
            time.sleep(3)
            return
        elif(framework_q == "c"):
            print("UwU twank ywu fowr cwhoosing catto ")
            time.sleep(2.5)
            url = "https://d17fnq9dkz9hgj.cloudfront.net/uploads/2018/03/Scottish-Fold_01.jpg"
            path = os.getcwd() + "\cat\\"
            os.mkdir(path)
            print(path)
            wget.download(url, path + "cat.jpg")

    if(extention_Condition == "n"):

        print("Initiating vanilla Js project creation...")

        time.sleep(1.5)

        filename_Html = input("""What do you want to name you HTML file?
        if empty - name will be: index.html (reccomended for first file)""")

        filename_Css = input("""What do you want to name you Css file?
        if empty - name will be: style.css (reccomended for first file)""")

        filename_Js = input("""What do you want to name you Js file?
        if empty - name will be: index.js (reccomended for first file)""")

        css_path = filename_Css
        jsPath = filename_Js 
        title = "Title"
        
        html_boilerplate = ("""<!DOCTYPE html >
        <html lang = "en">
        <head>
        <meta charset = "UTF-8 ">
        <meta name = "viewport" content = "width = device-width, initial-scale = 1.0">
        <meta http-equiv = "X-UA-Compatible" content = "ie = edge">
        <link rel="stylesheet" href= "normalize.css">
        <link rel="stylesheet" href=\"""" + css_path + """.css">
        <title> """ + title + """ </title>
        </head>
        <body>
 


        <script src=\"""" + jsPath + """.js"></script>
        </body>
        </html>
        """)
        
        import boilerplates
        if(filename_Html == ""):
            
            with open("index.html", "w") as file:
                file.write(html_boilerplate)
        else:
            
            print("i got here")
            with open(filename_Html + ".html", "w") as file:
                file.write(html_boilerplate)

        if(css_path == ""):
            with open("style.css", "w") as file:
                file.write(boilerplates.css_normalize)

            with open("normalize.css", "w") as file2:
                file2.write(boilerplates.css_normalize)
        else:
            print("i got here")
            with open(filename_Css + ".css", "w") as css:
                css.write("css goes here")

            with open("normalize.css", "w") as normalize:
                normalize.write(boilerplates.css_normalize)

        if(jsPath == ""):
            with open("index.js", "w") as js:
                js.write(boilerplates.js_Boilerplate)
                
            os.system('start /wait cmd /c "code ."')
        else:
            print("i got here")
            with open(filename_Js + ".js", "w") as js:
                js.write(boilerplates.js_Boilerplate)

            os.system('start /wait cmd /c "code ."')


main() 