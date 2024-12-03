import random


class FishColorConfig:
    possible_configs = [
        [(252, 186, 3), (0, 0, 0)],
        [(255, 255, 255), (232, 46, 21)],
        [(232, 46, 21), (71, 26, 20)],
        [(126, 166, 222), (255, 214, 212)],
        [(237, 192, 57), (255, 226, 138)],
        [(255, 252, 232), (54, 30, 18)],
        [(255, 255, 255), (242, 100, 29)],
        [(18, 18, 18), (222, 55, 55)],
        [(0, 0, 0), (18, 18, 18)],
        [(209, 89, 25), (255, 152, 97)],
        [(227, 82, 82), (255, 245, 245)],
        [(247, 122, 84), (255, 243, 184)],
        [(255, 252, 237), (255, 102, 31)],
        [(24, 26, 59), (234, 236, 255)],
        [(128, 171, 191), (54, 86, 112)]
    ]
    
    def __init__(self, base_color: tuple, accent_color: tuple):
        self.base_color = base_color
        self.accent_color = accent_color
        
    def random():
        colors = random.choice(list(FishColorConfig.possible_configs))
        return FishColorConfig(colors[0], colors[1])