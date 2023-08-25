import core.consts as consts
import os
import json

class Messenger:
    def __init__(self, title: str, args) -> None:
        self.title = title
        self.args = args
        self.version = consts.VERSION

        self.config = self.parse_config()
        self.__run__()

    def parse_config(self):
        self.args.config = os.path.abspath(self.args.config)

        if os.path.exists(self.args.config):
            conf = json.load(open(self.args.config))
            if conf.get("app") == self.title:
                return conf
            else:
                print("Wrong config file")
        else:
            answr = input(f"Config file does not exist. Are you want to create it [{self.args.config}] (Y/n): ")
            if answr in ("Y","y","YES","yes","Yes",""):

                if os.access(self.args.config, os.W_OK):
                    json.dump(consts.DEFAULT_CONFIG, self.args.config, indent=4)
                    conf = json.load(self.args.config)
                    if conf.get("app") == self.title:
                        return conf
                    else:
                        print("Wrong config file")
                else:
                    print(f"no access to file {self.args.config}")
                    

            else:
                answr = input(f"Are you want to use default config (Y/n): ")
                if answr in ("Y","y","YES","yes","Yes",""):
                    return consts.DEFAULT_CONFIG
                else:
                    print("You need config file to run this program")
                    exit(1)


    def __run__(self):
        if self.args.mode == "t":
            self.server(True)
            self.tui()
        elif self.args.mode == "g":
            self.server(True)
            self.gui()
        elif self.args.mode == "s":
            self.server()
    
    def tui(self): ...
    def gui(self): ...
    def server(self, sp: bool=False): ...