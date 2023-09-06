
import json5
class Note:
    def __init__(self):
        self.id = None
        self.title = None
        self.context = None
        self.demo = {"Users":[]}
        
class Repository:
    def __init__(self):
        self.Note = Note()
        self.Json_file = "note .json"
        self.Json_data = None
        self.Json_dict = None
    
    def create(self):
        with open(self.Json_File, mode = "w") as DATA:
            json5.dump(self.Note.demo, DATA)
            
    def get_id(self):
        with open(self.Json_File, mode = "r") as DATA:
            LEN_DICT = json5.load(DATA)
            self.Note.id = len(LEN_DICT["Users"])
        
    def get_all(self):
        self.get_id()
        self.Note.title = input("TITLE : ")
        self.Note.context = input("COMMENT: ")
        self.Json_Dict = {
            "id" : self.Note.id,
            "title" : self.Note.title,
            "context" : self.Note.context
        }

        def save():
            with open(self.Json_File, mode = "r") as DATA:
                self.Json_Data = json5.load(DATA)
            self.Json_Data["Users"].append(self.Json_Dict)
            with open(self.Json_File, mode = "w") as DATA:
                json5.dump(self.Json_Data, DATA, indent = 4)
        return save()

class view:
    def __init__(self):
        self.Method = Repository()
        self.input_id = None 
        
    def show_all(self):
        with open(self.Method.Json_File, mode = "r") as DATA:
            show = json5.load(data)
        return show
    
    def show_whit_id(self, ID):
        with open(self.Method.Json_File,  mode = "r") as DATA:
            show = json5.load(DATA)
        try:
            Result_Input = show["Users"][int(ID)]
        except:
            print("Your entry is either incorrect or there is no such ID!")
        else:
            return Result_Input
        
class NoteBook:
    def __init__(self):
        self.Repo = Repository()
        self.view = view()
        self.Repo.create()
        
    def ENTER_TITLE_AND_COMMENT(self):
        self.Repo.GET_TITLE_AND_COMMENT()
    
    def GIVE_ALL_ITEM(self):
        return self.view.show_all()
    
    def GIVE_ITEM_WITH_ID(self, ID):
        return self.view.show_whit_id(ID)

if __name__ == '__main__':
    final = Repository()

