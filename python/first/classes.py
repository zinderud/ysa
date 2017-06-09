
class pazaryeri:  

    def __init__(self, pazaryeri_adi, pazaryeri_tipi):  # creating a constructor function
        self.pazaryeri_adi = pazaryeri_adi
        self.pazaryeri_tipi = pazaryeri_tipi

    def pazaryeri_open(self):  # methods declaration
        print(self.pazaryeri_adi.title()+' bugun acik ')

    def pazaryeri_close(self):
        print(self.pazaryeri_adi.title() + ' kapali')


my_1 = pazaryeri('ciflik', 'balik')
my_1 = pazaryeri('meydan', 'fast food')

print('instance 1')
print(my_1.pazaryeri_open())  # use dot attrib to access properties or methods

print('instance 2')
print(my_1.pazaryeri_close())
