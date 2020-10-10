# -*- coding: utf-8 -*-
import os.path
class Person:
    def __init__(self,number):
        self.number=number
        
    def getNumber(self):#returnerar personens nummer
        return self.number
        
    def changeNumber(self,number):#uppdaterar personens nummer
        self.number=number

def options():
    print "OPTIONS:"
    print "add name number"
    print "lookup name"
    print "alias name newname"
    print "change name number"
    print "save filename"
    print "load filename"
    print "options"
    print "quit"      
    print "-"*10 

def add(inp,telebok):
    if telebok.has_key(inp[1]):#kontrollerar att personen inte redan finns i teleboken
        print "Person already exists in phonebook."
        return telebok
    else:
        telebok[inp[1]]=Person(inp[2])#namnet som angavs = en instans av Person med de angivna attributen
        print "You added",inp[1],"with number:",inp[2],"."
        return telebok#returnerar uppdaterad telebok
    
def lookup(inp,telebok):
    if telebok.has_key(inp[1]):#kontrollerar att namnet finns i teleboken
        print inp[1],"'s number is: ",telebok[inp[1]].getNumber()
    else:
        print "That person does not exist in the phonebook."
        return
        
def change(inp,telebok):
    if telebok.has_key(inp[1]):#kontrollerar att namnet finns i teleboken
        telebok[inp[1]].changeNumber(inp[2])
        print inp[1],"'s number has been changed to: ",telebok[inp[1]].getNumber()
    else:
        print "That person does not exist in the phonebook."
        
def save(inp,telebok):
    f=open(inp[1],"w")#skapar en fil som ska skrivas
    values=telebok.values()#skapar en lista bestående av värdena i teleboken
    keys=telebok.keys()#skaper en lista bestående av nycklarna i teleboken
    run=0
    while len(values)>run:
        line=values[run].getNumber()+";"+keys[run]+";"+"\n"#en rad skapas för varje iteration av loopen, med run som index i listorna
        run+=1
        f.write(line)#raden skrivs i filen
    f.close()
    print "File saved as",inp[1],"."

def load(inp,telebok):
    telebok={}#tömmer teleboken
    if os.path.exists(inp[1]):#kontrollerar att filen finns
        f=open(inp[1],"r")#öppnar den angivna filen för läsning
        for line in f:
           nline=line.split(";")#skapar en lista för varje rad med ';' som separerare mellan elementen
           del nline[-1]#tar bort '\n'
           telebok[nline[1]]=Person(nline[0])#skapar nytt objekt enligt filens information. 
        f.close()
        print inp[1],"has been loaded into the phonebook"
        return telebok
    else:
        print "File does not exist."

def main():
    telebok=dict()#skapar tom ordlista
    options()
    while True:
        try: 
            inp=raw_input('telebok> ').split()#skapar en lista av det som skrevs med mellanslag som separerare för element
            if inp[0]=="add" and len(inp)==3:#inp[0] är det det första ordet som skrivs in, om detta är add så körs följande. len(inp) kontrollerar korrekt antal argument.
                telebok=add(inp,telebok)
            elif inp[0]=="lookup" and len(inp)==2: 
                lookup(inp,telebok)
            elif inp[0]=="alias" and len(inp)==3 and telebok.has_key(inp[1]):#.has_key används för att kontrollera att att personen finns
                telebok[inp[2]]=telebok[inp[1]]
                print inp[1],"has been given the alias: ",inp[2]
            elif inp[0]=="change" and len(inp)==3:
                change(inp,telebok)
            elif inp[0]=="save" and len(inp)==2:
                if os.path.exists(inp[1]):
                    ow=raw_input("File already exists, do you want to overwrite? (yes/no):  ")
                    if ow=="yes":
                        save(inp,telebok)
            elif inp[0]=="load" and len(inp)==2:
                telebok=load(inp,telebok)
            elif inp[0]=="options":
                options()
            elif inp[0]=="quit":
                print "Goodbye!"
                return
            else:
                print "INVALID COMMAND, you can at any time 'options' for a list of options!"
        except IndexError: 
            print "INVALID COMMAND, you can at any time 'options' for a list of options!"
            print"-"*10
        except IOError:
            print "INVALID COMMAND, you can at any time 'options' for a list of options!"
            print"-"*10

main()

