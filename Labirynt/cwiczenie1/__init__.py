with open('/home/student/Pulpit/labirynt0.txt') as f:
  read_data = f.readlines()
  
print read_data

class Labirynt():
    def __init__(self):
        self.lab = ''
        for i in range(0, len(read_data)):
            j = 0
            while j < len(read_data[i]):
                #print read_data[i][j]
                self.lab += str(read_data[i][j])
                if read_data[i][j] == 'n':
                    self.lab += '\n'
                    j = 100
                j += 1
            
    def printt(self):
        return self.lab
    
    def find(self):
        szukaj = $
        
    
L1 = Labirynt()
print L1.printt()