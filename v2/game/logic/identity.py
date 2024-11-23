import random
from logic.trait import Trait

class Identity:
    def __init__(self):
        self.movement = []
        self.food = []
        self.fear = []
        
        self.traits = []
        
    def generate(self):
        self.movement = [random.randint(25, 75) / 100, random.randint(25, 75) / 100, random.randint(25, 75) / 100] # Natural Speed, Acceleration Frequency, Path Variance
        self.food = [random.randint(25, 75) / 100, random.randint(25, 75) / 100, random.randint(15, 55) / 100] # Attentiveness, Pursuit Speed, Gluttony
        self.fear = [random.randint(25, 75) / 100] # Avoidance
        
        for i in range(3):
            self.traits.append(random.choice(list(Trait)))
            
        for trait in len(self.traits):
            match trait:
                case Trait.Trait.SHY: 
                    self.movement[1] * (random.randint(40, 60) / 100)
                    self.movement[2] * (random.randint(95, 115) / 100)
                    self.food[1] * (random.randint(60, 75) / 100)
                    self.food[2] * (random.randint(30, 50) / 100)
                    self.fear[0] * (random.randint(100, 135))
                case Trait.Trait.BRUTISH:
                    pass