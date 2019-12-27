class Hash_Table():
    def __init__(self,size):
        self.size=size
        self.slots= [None]*self.size
        self.data =[None]*self.size

    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))

        #if slot is empty
        if self.slots[hashvalue]==None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
        else:
            if self.slots[hashvalue]==key:          #if slot has the similar key as old update it with new data
                self.data[hashvalue]=data

            else:
                nextslots =self.rehash(hashvalue,len(self.slots))    #if key is different

                while self.slots[nextslots]!=None and self.slots[nextslots]!=key:
                    nextslots=self.rehash(nextslots,len(self.slots))
                    if self.slots[nextslots]==None:
                        self.slots[nextslots]=key
                        self.data[nextslots]=data
                    else:
                        self.data[nextslots]=data  
    def hashfunction(self,key,size):
        return key%size
 
    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
        startslot =self.hashfunction(key,len(self.slots))
        data= None
        stop =False
        found= False
        position =startslot

        while self.slots[position]!=None and not found and not stop:
             if self.slots[position]==key:
                 found=True
                 data= self.data[position]
             else:
                 position=self.rehash(position,len(self.slots))
                 if position==startslot:
                     stop=True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

h = Hash_Table(5)
h[1]='go'
h[2]='python'
print(h[1])
print(h[2])