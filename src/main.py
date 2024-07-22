'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-20 14:30:27
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-23 00:42:53
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# main.py

import pygame
import sys

from utils.graphic import Graphic
from entity.player import Player
from utils.settings import Settings

# ! 重置游戏状态 TODO: 开发结束后请删掉!!!
def reset_game(screen, graphic, message, use_popup=True, font=None, duration=2000):
    Settings.state = Settings.MENU
    if use_popup:
        graphic.draw_popup(screen, message, font=font, duration=duration)

# 退出游戏
def quit_game():
    print('Bye Bye~')
    pygame.quit()
    sys.exit()

# pygame 事件处理
def pygame_event_handler(screen, graphic, player=None):
    game_state = Settings.state
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        elif event.type == pygame.KEYDOWN:

            # ! TODO: 开发结束后请删掉!!!
            if Settings.debug_mode and event.key == pygame.K_F2:
                reset_game(screen, graphic, '游戏已重置', font=Settings.FONT_CN)
            # ! -----------------------

            if game_state == Settings.MENU:
                if event.key == pygame.K_RETURN:
                    Settings.state = Settings.PLAYING
                elif event.key == pygame.K_s:
                    Settings.state = Settings.SETTINGS
                elif event.key == pygame.K_q:
                    quit_game()
            elif game_state == Settings.SETTINGS:
                if event.key == pygame.K_ESCAPE:
                    Settings.state = Settings.MENU
            elif game_state == Settings.PLAYING:
                if event.key == pygame.K_ESCAPE:
                    Settings.state = Settings.PAUSED
                elif event.key == pygame.K_F5:
                    Settings.debug_mode = not Settings.debug_mode
            elif game_state == Settings.PAUSED:
                if event.key in [pygame.K_p, pygame.K_ESCAPE]:
                    Settings.state = Settings.PLAYING
                elif event.key == pygame.K_s:
                    graphic.save_game(screen, player)
                elif event.key == pygame.K_l:
                    player = graphic.load_game(screen, player)
                elif event.key == pygame.K_q:
                    quit_game()

# 返回是否游戏中判断
def is_playing(screen, graphic):
    game_state = Settings.state
    if game_state == Settings.MENU:
        graphic.draw_menu(screen)
    elif game_state == Settings.SETTINGS:
        graphic.draw_settings(screen)
    elif game_state == Settings.PAUSED:
        graphic.draw_pause(screen)
    elif game_state == Settings.PLAYING:
        return True
    return False

# 主函数
def main():
    # 初始化 pygame
    graphic = Graphic()
    screen, background_image = graphic.initialize_game()

    # 初始化玩家
    player = Player(name='HanskiJay')
    # player.set_x(Settings.SCREEN_WIDTH // 2).set_y(Settings.SCREEN_HEIGHT // 2)

    # 主循环
    clock = pygame.time.Clock()
    running = True

    while running:
        # 监听事件处理
        pygame_event_handler(screen, graphic)

        # 游戏中逻辑执行
        if is_playing(screen, graphic):
            # 判断玩家是否存活
            if not player.is_alive():
                # ! TODO: 保存游戏数据 & 重置游戏状态
                reset_game(screen, graphic, 'Game Over!')
                continue

            # 清屏
            screen.blit(background_image, (0, 0))
            # 游戏内逻辑
            keys = pygame.key.get_pressed()
            # player.move(keys)

            # 绘制调试窗口
            if Settings.debug_mode:
                graphic.draw_debug_window(screen, [
                    'Version=0.0.1 (Build 202407220001) | DEBUG_MODE=ON',
                    f'FPS: {clock.get_fps()}'
                ], color=[
                    (0, 255, 255),
                    (250, 250, 51)
                ])
                # player.set_health(100)

            # 更新显示
            pygame.display.flip()

        # 控制帧率
        clock.tick(Settings.FPS)

if __name__ == '__main__':
    main()