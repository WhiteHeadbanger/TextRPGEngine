import json
import time, os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

class RPGScript:

    def __init__(self, path):
        """
        :param str path: Absolute path to json file 
        """
        self.file = self.load_file(path)

    def load_file(self, path):
        with open(path, 'r') as f:
            data = f.read()
        return data

    def parse_file(self):
        return json.loads(self.file)

class DialogManagement:

    def __init__(self, obj, author, quest):
        """
        Load parsed file for easier management 

        :param obj obj: RPGScript parsed file object
        :param str author: The quest-giver
        :param str quest: The name of the quest
        """
        self.author = author
        self.quest = quest
        self._init = self.initialize(obj)
        self.qtext = self.quest_text(self._init)
        self.rtext = self.response_text(self._init)

        self.quest_length = len(self.qtext)
        self.response_lenght = len(self.rtext)

    def initialize(self, obj):
        return obj[self.author][self.quest]

    def quest_text(self, initobj):
        return initobj["Text"]

    def response_text(self, initobj):
        return initobj["Response"]

    def show_quest(self):
        """
        returns selected quest line

        :param int quest_line: quest line from quest list 
        """
        for quest_line in self.qtext:
            print(quest_line)
            time.sleep(1)

    def user_response(self, dialog_number: int):
        """
        returns selected user response line

        :param int dialog_number: response line from response list 
        """
        return self.rtext[dialog_number][0]

    def npc_response(self, dialog_number: int):
        """
        returns selected npc response line

        :param int dialog_number: response line from response list 
        """
        return self.rtext[dialog_number][1]

def main():
    text = RPGScript(os.path.join(THIS_FOLDER, 'dialog.json'))
    text_parsed = text.parse_file()
    dialog = DialogManagement(text_parsed, "John", "Tutorial")


    running = True
    dialog.show_quest()
    while running:
        print("------ Options ------")
        print("1. {}".format(dialog.user_response(0)))
        print("2. {}".format(dialog.user_response(1)))
        print("3. {}".format(dialog.user_response(2)))
        print("(Q)uit")
        opc = input(">>: ").lower()
        if opc == "1":
            print(dialog.npc_response(0))
        elif opc == "2":
            print(dialog.npc_response(1))
        elif opc == "3":
            print(dialog.npc_response(2))
        elif opc == 'q':
            running = False

if __name__ == "__main__":
    main()


            

