import os
import sys
import markdown


class AetherRequest:
    def __init__(self, text: str):
        self.__text: str = text

    def as_markdown(self):
        # does basically nothing
        return self.__text

    def as_html(self):
        print("coming soon!")

        return markdown.markdown(self.__text, extensions=['tables'])

    def as_json(self):
        print("Not ready yet")


def aether_fetch(query: str) -> AetherRequest:
    with open(query) as resp:
        # TODO: Implement search feature
        text = resp.read()

        return AetherRequest(text)


if __name__ == '__main__':
    req: AetherRequest = aether_fetch(f"{sys.argv[1]}")
    text = req.as_html()
    f = open("dump.html", 'w')
    f.write(text)
    f.close()
