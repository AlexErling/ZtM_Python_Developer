from translate import Translator

try:
    with open("sample.txt", mode="r") as my_file:
        sentence = my_file.read()
        translator = Translator(to_lang="ja")
        translation = translator.translate(sentence)
        print(translation)

except FileNotFoundError as e:
    print('Check your file path!')

