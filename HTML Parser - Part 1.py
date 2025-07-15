from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            name = attr[0]
            value = attr[1] if attr[1] is not None else "None"
            print(f"-> {name} > {value}")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            name = attr[0]
            value = attr[1] if attr[1] is not None else "None"
            print(f"-> {name} > {value}")


n = int(input())

html_code = ""
for _ in range(n):
    html_code += input()

parser = MyHTMLParser()
parser.feed(html_code)
