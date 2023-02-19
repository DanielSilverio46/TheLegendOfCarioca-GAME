from random import randint

class InimigoComum:
    armas = {'soco': 2, 'pistola': 5}
    def __init__(self, vida, amardura, arma):
        self.vida_total = vida
        self.vida_atual = vida

        self.amadura = amardura
        self.arma = arma

    def atacar(self):
        acerto = randint(1, 10)
        
        if acerto == 10:
            dano = self.arma

        elif acerto >= 7:
            dano = randint(1, 5)

        else:
            dano = 0

        return dano

    def se_curar(self):
        acerto = randint(1, 20)

        if acerto == 20:
            cura = 3
        
        elif acerto >= 13:
            cura = randint(1, 3)
        
        else:
            cura = 0
        
        return cura
    
    def receber_dano(self, dano):
        self.dano = dano
        self.dano -= self.amadura

        if self.dano <= 0:
            self.dano = 1
 
    def defender(self):
        acerto = randint(1, 20)
        
        if acerto == 20:
            self.dano = 1

        elif acerto >= 13:
            self.dano -= (self.dano * 50/100) 
            
        return self.dano

    def fugir(self):
        acerto = randint(1, 20)

        if acerto >= 16:
            self.vida -= self.vida
