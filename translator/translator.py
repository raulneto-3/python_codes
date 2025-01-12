from googletrans import Translator

def translate(text, dest='en'):
    translator = Translator()
    return translator.translate(text, dest=dest).text

if __name__ == '__main__':
    text = input("Enter the text to translate: ")
    dest = input("Enter the language code of the destination language: ")
    print(translate(text, dest))