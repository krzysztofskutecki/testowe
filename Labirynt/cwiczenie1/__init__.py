with open('/home/student/Pulpit/labirynt0.txt') as f:
  read_data = f.readlines()
  
print read_data

class Labirynt():
    def __init__(self):
        self.lab_str = ''
        self.lab_tab = []
        self.wyjscie = [0,0]
        self.pozycja = [0,0]
        for i in range(0, len(read_data)):
            j = 0
            a = []
            while j < len(read_data[i]):
                #print read_data[i][j]
                self.lab_str += str(read_data[i][j])
                a.append(read_data[i][j])
                if read_data[i][j] == '$':
                    self.wyjscie = read_data[i][j]
                if read_data[i][j] == '@': 
                    self.pozycja = read_data[i][j]
                if read_data[i][j] == 'n':
                    self.lab_str += '\n'
                    j = 100
                j += 1
                self.lab_tab.append(a)
        self.wysokosc = len(self.lab_tab)-1
        self.szerokosc = len(self.lab_tab[1])-1
            
    def printt(self):
        return self.lab, self.szerokosc, self.wysokosc
        
    def lewo(self):
        self.pozycja[0] - 1 = self.pozycja[0]
        self.lab_tab[self.pozycja] = '*'
    def prawo(self):
        self.pozycja[0] + 1 = self.pozycja[0]
        self.lab_tab[self.pozycja] = '*'
    def gora(self):
        self.pozycja[1] + 1 = self.pozycja[0]
        self.lab_tab[self.pozycja] = '*'
    def dol(self):
        self.pozycja[1] - 1 = self.pozycja[0]
        self.lab_tab[self.pozycja] = '*'
        
    def find(self):
        while self.wyjscie != self.pozycja:
            if self.pozycja[0] + 1 != '#' or self.pozycja[0] + 1 != '*' or self.pozycja[0] + 1 != '@':
                self.prawo()
            if self.pozycja[1] - 1 != '#' or self.pozycja[1] - 1 != '*' or self.pozycja[1] - 1 != '@':
                self.dol()
            if self.pozycja[0] - 1 != '#' or self.pozycja[0] - 1 != '*' or self.pozycja[0] - 1 != '@':
                self.lewo()
            if self.pozycja[1] + 1 != '#' or self.pozycja[1] + 1 != '*' or self.pozycja[1] + 1 != '@':
                self.gora()
            if self.pozycja[0] + 1 != '#':
                self.prawo()
            if self.pozycja[1] - 1 != '#':
                self.dol()
            if self.pozycja[0] - 1 != '#':
                self.lewo()
            if self.pozycja[1] + 1 != '#':
                self.gora()
        return self.lab_tab
        
        
        
    
L1 = Labirynt()
print L1.printt()
