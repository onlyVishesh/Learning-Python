from turtle import *
ht()
speed(0)
lt(90)
up()
setpos(0,-700)
down()

        
   
        
def tree(size,level,length,angle):
      
      if level==0:
         pensize(2)
         right(30)
         color('green')
         fillcolor('red')
         begin_fill()
         circle(10)
         end_fill()
         left(30)
         
         return
      
      color('black')
      pensize(size)
      fd(length)
      right(angle)
      tree((size*0.8),(level-1),(length*0.75),angle)
      left(angle*2)
      tree((size*0.8),(level-1),(length*0.75),angle)
      right(angle)
      bk(length)
      
      

#for i in range(1,6):
tree(20,6,300,28)
   





mainloop()