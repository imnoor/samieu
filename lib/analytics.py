class Analtyics:
    __instance = None
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Analtyics.__instance == None:
            Analtyics()
        return Analtyics.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Analtyics.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.fails= {"Count" : 0}
            self.wins= {"Count" : 0}

            Analtyics.__instance = self

    def log_fail(self, cmd):
        count = self.fails[cmd]
        if not count:
            self.fails[cmd] = 1
        else:
            self.fails[cmd] = self.fails[cmd] +1
        print(cmd + " fails " + self.fails[cmd])
    
    def log_wins(self, cmd):
        count = self.wins[cmd]
        if not count:
            self.wins[cmd] = 1
        else:
            self.wins[cmd] = self.wins[cmd] +1
        print(cmd + " fails " + self.wins[cmd])
    
    def print(self):
        print("Fails")
        self.__print_data(self.fails)
        print("Wins")
        self.__print_data(self.wins)

    def __print_data(self,data):
        data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1],reverse=True)}
        print ("{:<8} {:<15} {:<10}".format('Sl','Label','Count'))
        slno=0
        for k, v in data.items():
            slno = slno + 1
            print ("{:<8} {:<15} {:<10}".format(slno, k, v))

    


