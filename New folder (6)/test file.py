import json5
def checking(file):
    def json_or_text():
        try:
            json_data = json5.load(file("note .json"))
        except:
            try:
                text_data = file().read()
            except:
                print("Such a file is not supported")
            else:
                print(text_data)
        else:
            return json_data
    return json_or_text
@checking
def open_fileing():
    open_file = open("notebook.json")
    return open_file
open_fileing()