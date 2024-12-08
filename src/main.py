from textnode import *

def main():
    test1 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    test2 = TextNode("This is a text node", TextType.BOLD)
    print(test1)
    print(test2)


if __name__ == "__main__":
    main()