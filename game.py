import turtle
import drawmap

#맵 그리기
drawmap.draw();

# 각종 설정
#사용자(player)가 움직이는 거북이
player = turtle.Turtle()       #터틀의 함수를 가지고 옴
screen = player.getscreen()      #화면에 표시
player.shape("turtle")
player.shapesize(1.35, 1.35)
player.speed(100)
player.up();



#turtle 의 상하이동
movegap = 72;
def left() :
   player.setheading(180)     
   player.setx(player.xcor() - movegap)
def right():
   player.setheading(0)       
   player.setx(player.xcor() + movegap)
def up() :
   player.setheading(90)      
   player.sety(player.ycor() + movegap)
def down() :
   player.setheading(270)     
   player.sety(player.ycor() - movegap)


# onkeypress(함수명, 키보드버튼명) :
# 어떤 버튼을 눌렀을 때, 이 함수가 동작하도록 하겠다
screen.onkeypress(left, "Left")        #왼쪽 방향키눌렀을 때 left 함수 실행
screen.onkeypress(right, "Right")      #오른쪽 방향키눌렀을 때 right 함수 실행
screen.onkeypress(up, "Up")            #위쪽 방향키눌렀을 때 up 함수 실행
screen.onkeypress(down, "Down")        #아래쪽 방향키눌렀을 때 down 함수 실행

screen.listen() # 프로그램 활성화
screen.mainloop() # 프로그램이 계속 동작하는 상태를 유지하겠다!