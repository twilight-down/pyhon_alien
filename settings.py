class Settings():
    """用于存储外星人的设置"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (240,240,255)
        # 设置子弹
        self.bullet_speed_factor =1
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (0,0,0)
        self.bullets_allowed = 15
        # 依次为速度 宽度 高度 颜色 允许出现最大子弹数量

        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction 为 1 表示向右移，为 -1 表示向左移
        self.fleet_direction = 1

        #飞船设置
        self.ship_speed_factor = 4
        self.ship_limit = 3
