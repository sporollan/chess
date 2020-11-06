import game


if __name__ =='__main__':
    g = game.Game()
    while 1:
        coords = input('move')
        for line in g.play((int(coords[0]), int(coords[1]))):
            print(line)
        print(g.check)