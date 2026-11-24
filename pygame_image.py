import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    tmr = 0
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr  # 時間の経過とともに増加する変数
        screen.blit(bg_img, [-x, 0])  # 背景の横座標を -x にして左へ移動させる
        screen.blit(bg_img, [-x + 1600, 0])  # 練習7：2枚目の背景を右隣にblit
        screen.blit(bg_img2, [-x + 1600, 0])  #練習8
        screen.blit(kk_img, [300, 200])  # 練習４こうかとんを描画

        pg.display.update()
        tmr += 1        
        clock.tick(200)# 練習6：FPSを200に変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()