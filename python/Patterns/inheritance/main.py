class Yaratik(object):

    def move_left(self):
        print('Moving left...')

    def move_right(self):
        print('Moving left...')


class Ejderha(Yaratik):

    def Ates_puskurtme(self):
        print('ates puskurtum!')


class Zombie(Yaratik):

    def Isirmak(self):
        print('Isirdim simdi!')


enemy = Yaratik()
enemy.move_left()

# ejderha also includes all functions from parent class (yaratik)
ejderha = Ejderha()
ejderha.move_left()
ejderha.Ates_puskurtme()

# Zombie is called the (child class), inherits from Yaratik (parent class)
zombie = Zombie()
zombie.move_right()
zombie.Isirmak()
