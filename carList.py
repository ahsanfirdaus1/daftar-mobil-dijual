class car:
    
    def __init__(self, namaMobil  , merekMobil , tahunMobil , hargaMobil):
        self.__namaMobil = namaMobil
        self.__merekMobil = merekMobil
        self.__tahunMobil = tahunMobil
        self.__hargaMobil = hargaMobil 
    
    def set_namaMobil (self, namaMobil):
        self.__namaMobil = namaMobil
    
    def set_merekMobil (self, merekMobil):
        self.__merekMobil = merekMobil
    
    def set_tahunMobil (self, tahunMobil):
        self.__tahunMobil = tahunMobil
    
    def set_hargaMobil (self, hargaMobil):
        self.__hargaMobil = hargaMobil
    
    def get_namaMobil (self):
        return self.__namaMobil

    def get_merekMobil (self):
        return self.__merekMobil
    def get_tahunMobil (self):
        return self.__tahunMobil
    def get_hargaMobil (self):
        return self.__hargaMobil
        

    


