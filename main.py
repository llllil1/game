import turtle


class Vector2:
    def __init__(self, x, y):
        self.x=x
        self.y=y


    def multiply(vector1, vector2):
        return Vector2(vector1.x * vector2.x, vector1.y * vector2.y)
    
    def multiplySelf(self, vector1):
        self.x *= vector1.x
        self.y *= vector1.y

    def add(vector1, vector2):
        return Vector2(vector1.x + vector2.x, vector1.y + vector2.y)

    def addSelf(self, vector1):
        self.x += vector1.x
        self.y += vector1.y

class Map:
    def __init__(self, mapSize, margin): 
        # 스크린 draw turtle 생성 및 설정
        tu = turtle.Turtle()
        tu.speed(0)

        # 스크린 표시
        screen = tu.getscreen()

        # 스크린 사이즈 설정
        size = 800

        # 베이스 라인 위치 설정
        drawInit = Vector2((size/2) * -1, (size/2));
        drawLength = Vector2.multiply(drawInit, Vector2(-1, -1))

        # 바깥여백 설정
        drawInit.add(Vector2(margin * -1, margin))
        drawLength.add(Vector2(margin*-1, margin))


        screen.setup(size+(margin * size/100), size+(margin * size/100))
        
        # 간격
        gap = Vector2(size/mapSize.x, size/mapSize.y)

        # 가로 라인
        for y in range(mapSize.y+1):
            tu.up()
            tu.setpos(drawInit.x,  drawInit.y + ((y * gap.y) * -1))
            tu.down()
            tu.setpos(drawLength.x, drawInit.y + ((y * gap.y) * -1))

        # 세로 라인
        for x in range(mapSize.x+1):
            tu.up()
            tu.setpos(drawInit.x + ((x * gap.x) * 1), drawInit.y)
            tu.down()
            tu.setpos(drawInit.x + ((x * gap.x) * 1), drawLength.y)

        
        self.gap = gap
        self.drawInit = drawInit


        self.player_size = Vector2(self.gap.x/32, self.gap.y/32);

        initX = self.player_size.x * 16
        initY = self.player_size.y * 16        

        self.palyer_init = Vector2(self.drawInit.x + initX, self.drawInit.y - initY)
        self.palyer_gap = ((gap.x/32) * 16) + (initX)

        
