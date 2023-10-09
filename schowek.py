 # # pygame.draw.rect(background, score, Rect(1420, 80, 400, 800))
    # pygame.draw.rect(background, score, Rect(100, 80, 400, 800))
    # # pygame.draw.rect(background, black, Rect(1420, 80, 400, 800), 3)
    # pygame.draw.rect(background, black, Rect(100, 80, 400, 800), 3)
    # # pygame.draw.rect(background, black, Rect(1420, 80, 400, 100), 3)
    # pygame.draw.rect(background, black, Rect(100, 80, 400, 100), 3)

        # pygame.draw.rect(background, black, Rect(560, 80, 800, 800), 4)
    # pygame.draw.rect(background, prop_color, Rect(562, 82, 796, 796))
    # pygame.draw.rect(background, deck_cen, Rect(662, 182, 596, 596))

    # pygame.draw.rect(background, black, Rect(560, 776, 104, 104), 2)

     # font = pygame.font.Font(None, 90)
    # text = font.render("Monopoly", 1, monopoly_txt)
    # textpos = text.get_rect()
    # textpos.centerx = background.get_rect().centerx
    # textpos = textpos.move(0, 430)
    # background.blit(text, textpos)


        # """Players title"""
    # font = pygame.font.Font(None, 50)
    # text = font.render("Players", 1, black)
    # textpos = text.get_rect()
    # textpos.centerx = background.get_rect().centerx
    # textpos = textpos.move(650, 110)
    # background.blit(text, textpos)

    # """Action title"""
    # font = pygame.font.Font(None, 50)
    # text = font.render("Action", 1, black)
    # textpos = text.get_rect()
    # textpos.centerx = background.get_rect().centerx
    # textpos = textpos.move(-660, 110)
    # background.blit(text, textpos)


# pygame.draw.rect(background, special, Rect(560 + 2, 776 + 2, 100, 100))
    
    # pygame.draw.rect(background, black, Rect(move, 776, 104, 104), 2)
    # pygame.draw.rect(background, special, Rect(move + 2, 776 + 2, 100, 100))
    
    # pygame.draw.rect(background, black, Rect(560, move_up, 104, 104), 2)
    # pygame.draw.rect(background, special, Rect(560 + 2, move_up + 2, 100, 100))
    # pygame.draw.rect(background, black, Rect(move, move_up, 100, 104), 2)
    # pygame.draw.rect(background, special, Rect(move + 2, move_up + 2, 100, 100))





surf = self.background
        corn = self.corner_size + 6
        x_start = self.xcord + self.corner_size
        y_start = self.ycord + self.corner_size - 2
        x_right = self.xcord + self.size - self.corner_size
        y_down = y_start + self.center_size - 3
        for i in range(39):
            size = self.center_size // 9
            move = (i % 10) * size
            side = i // 10
            if side == 2:
                pygame.draw.rect(surf, black, Rect(x_start + move, self.ycord, size, corn), 2)
            if side == 0:
                pygame.draw.rect(surf, black, Rect(x_start + move, y_down, size, corn), 2)
            if side == 1:
                pygame.draw.rect(surf, black, Rect(self.xcord, y_start + move, corn, size + 2), 2)
            if side == 3:
                pygame.draw.rect(surf, black, Rect(x_right, y_start + move, corn, size + 2), 2)





            game = True
    while game:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        for player in players:
            # Player_name(player, background)
            # Player_info(players, background)
            screen.blit(background, (0, 0))
            pygame.display.flip()
            while player.throws() != 0 and player.pause() == 0:
                try:
                    player.throw_dices()
                    pos = player.position()
                    active_sqr = database[pos]
                    if active_sqr.type() == "special":
                        active_sqr.do_action(player)
                    elif active_sqr.type() == "property":
                        if active_sqr.owner() is not None and active_sqr.owner() != player:
                            print(active_sqr.owner().name())
                            active_sqr.pay_rent(player)
                            if player.bankrut():
                                players.remove(player)
                        elif active_sqr.owner() != player:
                            text = input("Co chcesz zrobić")
                            if text == "Kup":
                                try:
                                    active_sqr.buy(player)
                                    pygame.display.flip()
                                except NotEnoughtMoneyError():
                                    print("Nie posiadasz wystarczających funduszy")
                        elif active_sqr.area().check_if_fully_occupied(player):
                            action = input("Możesz kupić domek, chcesz?: ")
                            if action == "Tak":
                                try:
                                    active_sqr.buy_house()
                                except NotEnoughtMoneyError():
                                    print("Nie posiadasz wystarczających funduszy")
                except:
                    break
            player.subtract_pause()
            if player.pause() == 0:
                player.add_throws()




# font = pygame.font.Font(None, 20)

    # for i in range(4):
    #     sqr = database[10 * i]
    #     text = font.render(sqr.name(), 1, black)
    #     textpos = text.get_rect()
    #     textpos.centerx = background.get_rect().centerx
    #     text = pygame.transform.rotate(text, 45)
    #     text = pygame.transform.rotate(text, -90 * i)
    #     textpos = textpos.move(360, 825)
    #     if i == 1 or i == 2:
    #         textpos = textpos.move(-728, 0)
    #     if i == 2 or i == 3:
    #         textpos = textpos.move(0, -742)
    #     background.blit(text, textpos)

    # """0 - 10"""
    # font = pygame.font.Font(None, 15)
    # for i in range(1, 10):
    #     move_txt = i * 66
    #     line = database[i].name()
    #     if database[i].type() == "property":
    #         pygame.draw.rect(background, black, Rect(1256 - move_txt, 776,  68, 25,), 2)
    #         pygame.draw.rect(background, database[i].area().colour(), Rect(1258 - move_txt, 778, 64, 21))
    #     text = font.render(line, 1, black)
    #     textpos = text.get_rect()
    #     textpos.centerx = background.get_rect().centerx
    #     textpos = textpos.move(332 - move_txt, 805)
    #     background.blit(text, textpos)

    # """10 - 20"""
    # for i in range(1, 10):
    #     move_txt = i * 66
    #     line = database[i + 10].name()
    #     if database[i + 10].type() == "property":
    #         pygame.draw.rect(background, black, Rect(639, 776 - move_txt, 25, 68), 2)
    #         pygame.draw.rect(background, database[i + 10].area().colour(), Rect(641, 778 - move_txt, 21, 64))
    #     text = font.render(line, 1, black)
    #     text = pygame.transform.rotate(text, 270)
    #     textpos = text.get_rect()
    #     textpos.centerx = background.get_rect().centerx
    #     textpos = textpos.move(-332, 790 - move_txt)
    #     background.blit(text, textpos)

    # """20 - 30"""
    # for i in range(1, 10):
    #     move_txt = i * 66
    #     line = database[i + 20].name()
    #     if database[i + 20].type() == "property":
    #         pygame.draw.rect(background, black, Rect(596 + move_txt, 159,  68, 25,), 2)
    #         pygame.draw.rect(background, database[i + 20].area().colour(), Rect(598 + move_txt, 161, 64, 21))
    #     text = font.render(line, 1, black)
    #     text = pygame.transform.rotate(text, 180)
    #     textpos = text.get_rect()
    #     textpos.centerx = background.get_rect().centerx
    #     textpos = textpos.move(-328 + move_txt, 145)
    #     background.blit(text, textpos)

    # """30 - 40"""
    # for i in range(1, 10):
    #     move_txt = i * 66
    #     line = database[i + 30].name()
    #     if database[i + 30].type() == "property":
    #         pygame.draw.rect(background, black, Rect(1256, 116 + move_txt, 25, 68), 2)
    #         pygame.draw.rect(background, database[i + 30].area().colour(), Rect(1258, 118 + move_txt, 21, 64))
    #     text = font.render(line, 1, black)
    #     text = pygame.transform.rotate(text, 90)
    #     textpos = text.get_rect()
    #     textpos.centerx = background.get_rect().centerx
    #     textpos = textpos.move(332, 125 + move_txt)
    #     background.blit(text, textpos)


    blue = (66, 135, 245)
red = (153, 28, 28)
yellow = (184, 150, 48)
green = (88, 184, 48)
black = (0, 0, 0)
white = (255, 255, 255)
monopoly_txt = (235, 74, 0)
special = (0, 128, 128)
lighted_spec = (0, 195, 222)
score = (145, 165, 199)
color = (227, 250, 247) # background
corner = (255, 94, 0)
prop_color = (165, 245, 240)
lighted_prop = (220, 174, 222)
deck_cen = (145, 165, 199)
button_color = (123, 129, 31)
pons_color = (216, 29, 29)
title_color = (0, 128, 128)
to_fly_color = (180, 174, 122)
title_center_board = white