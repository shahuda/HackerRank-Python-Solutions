from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        lines = data.splitlines()
        if len(lines) > 1:
            print(">>> Multi-line Comment")
            for line in lines:
                print(line)
        else:
            print(">>> Single-line Comment")
            print(data)

    def handle_data(self, data):
        if data != '\n':  
            print(">>> Data")
            print(data)


n = int(input())
html = ""
for _ in range(n):
    html += input() + '\n'

parser = MyHTMLParser()
parser.feed(html)

