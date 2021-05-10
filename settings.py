class Settings:


    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1100
        self.bg_color = (18, 5, 255)
        self.bg_image = "images/meme.bmp"
        self.troll_limit = 3
        self.bullet_height = 50
        self.bullet_color = 255, 255, 0
        self.fleet_drop_speed = 30
        self.fleet_direction = 1
        self.speedup_scale= 2
        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        self.troll_speed_factor = 1.5
        self.bullet_speed_factor = 1.5
        self.megusta_speed_factor = 2
        self.bullet_width = 5
        self.bullets_allowed = 10

    def increase_speed(self):
        self.troll_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.megusta_speed_factor *= self.speedup_scale
        self.bullet_width *= self.speedup_scale
        self.bullets_allowed *= self.speedup_scale
