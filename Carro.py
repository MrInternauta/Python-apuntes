class CarroF:
    def __init__(self):
        self._CARS = ['''
                       \
          __________ ___/_>________
         /  ____ \ <>     |  ____  \
        =\_/ __ \_\_______|_/ __ \__D
    ________(__)_____________(__)____
    ''',
    '''
           -           __
      --          ~( @\  \
     ---   _________]_[__/_>________
         /  ____ \ <>     |  ____  \
        =\_/ __ \_\_______|_/ __ \__D
    ________(__)_____________(__)____
    ''']

        self._model = ""
        self._color = ""
        self._type = ""
        self._status = False

    def set_information(self,model,color,type,status):
        self._model = model
        self._color = color
        self._type = type
        self._status = status
        self._print()

    def _print(self):
        print('Modelo: {}\nColor: {}\nTipo?: {}\nEstado:'.format(self._model,self._color, self._type ))
        if self._status == True:
            self._status = False
            print(self._CARS[0])
        else:
            self._status = True
            print(self._CARS[1])

    def change_status(self):
        if self._status == True:
            self._status = False
            print(self._CARS[0])
        else:
            self._status = True
            print(self._CARS[1])
