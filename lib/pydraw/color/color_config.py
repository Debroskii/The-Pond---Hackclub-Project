class ColorConfig:
    primary_color: tuple
    secondary_color: tuple
    tertiary_color: tuple
    
    def __init__(self, primary_color: tuple, secondary_color: tuple, tertiary_color: tuple):
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.tertiary_color = tertiary_color