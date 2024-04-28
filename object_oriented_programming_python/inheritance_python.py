import colorsys as cl
class Maruthi:
    def turbo_engine(self):
        return 'Turbo pertol +Dsg'
    def car_color(self):
        color= (250,0,0)
        return color

class Toyota(Maruthi):
    def spoiler(self):
        return 'No spolier'

class Lexes:
    def typre_size(self):
        return '13 inch'
    def ai_system(self):
        activated =True
        return activated
class BmwModels(Lexes,Toyota):
      def panoromic_sunroof(self):
          roof=True and False
          return roof
toyota =Toyota()
# print(toyota.car_color)
obj1=toyota.turbo_engine()
print(obj1)
bmwModels= BmwModels()
c=bmwModels.panoromic_sunroof()
print(c)
print(bmwModels.car_color(),'\n',bmwModels.turbo_engine())