import turtle
import main

#맵 그리기
map = main.Map(main.Vector2(10, 10), 5)

# 각종 설정
#사용자(player)가 움직이는 거북이
player = turtle.Turtle()       #터틀의 함수를 가지고 옴
screen = player.getscreen()      #화면에 표시
player.shape("turtle")
player.shapesize(map.player_size.x, map.player_size.y)
player.speed(0)
player.up();
player.setpos(map.palyer_init.x, map.palyer_init.y)

def left() :
   player.setheading(180)     
   player.setx(player.xcor() - map.palyer_gap)
def right():
   player.setheading(0)       
   player.setx(player.xcor() + map.palyer_gap)
def up() :
   player.setheading(90)      
   player.sety(player.ycor() + map.palyer_gap)
def down() :
   player.setheading(270)     
   player.sety(player.ycor() - map.palyer_gap)


# onkeypress(함수명, 키보드버튼명) :
# 어떤 버튼을 눌렀을 때, 이 함수가 동작하도록 하겠다
screen.onkeypress(left, "Left")        #왼쪽 방향키눌렀을 때 left 함수 실행
screen.onkeypress(right, "Right")      #오른쪽 방향키눌렀을 때 right 함수 실행
screen.onkeypress(up, "Up")            #위쪽 방향키눌렀을 때 up 함수 실행
screen.onkeypress(down, "Down")        #아래쪽 방향키눌렀을 때 down 함수 실행

screen.listen() # 프로그램 활성화
screen.mainloop() # 프로그램이 계속 동작하는 상태를 유지하겠다!