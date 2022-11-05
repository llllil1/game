import turtle

# 스크린 크기
size = 800;
# 맵 바깥여백
margin = 38;
# 최초 위치 X값
initX = ((size/2) - (margin*2)) * -1;
# 최초 위치 Y값
initY = ((size/2) - (margin*2));
# 간격
space = (size - (margin*2))/10;
# 줄 길이
drawSize = size - (margin*2) - space;

# 스크린 설정 및 맵 그리는 속도 설정
screen=turtle.Screen()
screen.setup(size, size)
turtle.speed(100)

# 왼쪽 상단 초기 위치로 이동
turtle.up()
turtle.setpos(initX, initY)
turtle.down()

def draw():
	for i in range(20):
		# 줄 긎기
		turtle.forward(drawSize)
		
		# 가로 10줄 다그었으면 방향 전환
		if(i + 1 == 10):
			turtle.right(90)

		# 10줄은 가로로 나머지 줄은 세로로
		turtle.up()
		if(i + 1 < 10):
			turtle.setpos(initX, initY - (i+1) * space)
		else:
			turtle.setpos(initX + (i+1-10) * space, initY)
		turtle.down()
