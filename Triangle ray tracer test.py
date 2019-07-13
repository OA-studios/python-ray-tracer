import pygame , sys, math
from random import randint
 
class Triangle(object):
    def __init__(self,p1,p2,p3):
        self.p1=p1
        self.p2=p2
        self.p3=p3

    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return str((self.p1,self.p2,self.p3))
    def draw(self,screen):
 
    
        def getgradient(p,q):

            try:
                m=(p[1]-q[1])/(p[0]-q[0])
            except ZeroDivisionError:
                if (p[1]-q[1])>0:
                    m=100000
                elif (p[1]-q[1])<0:
                    m=-100000
                else:
                    m=None
            return m
        x=1
        y=1

        #gradients
        l1m=getgradient(self.p1,self.p2)
        l2m=getgradient(self.p1,self.p3)
        l3m=getgradient(self.p2,self.p3)


        if l1m is None or l2m is None or l3m is None:
            return


        #intercepts
        l1C=(self.p1[1]-l1m*(self.p1[0]))
        l2C=(self.p1[1]-l2m*(self.p1[0]))
        l3C=(self.p3[1]-l3m*(self.p3[0]))

        #opposite
        l1opposite=(l1m*self.p3[0]+l1C)
        l2opposite=(l2m*self.p2[0]+l2C)
        l3opposite=(l3m*self.p1[0]+l3C)

        for y in range(1,height):
            for x in range(1,width):
                l1y=(l1m*x)+ l1C

                l2y=(l2m*x)+ l2C

                l3y=(l3m*x)+ l3C


                if (y<=l1y)==(self.p3[1]<=l1opposite)  and (y>=l2y)==(self.p2[1]>=l2opposite) and (y>=l3y)==(self.p1[1]>=l3opposite):
                    screen.set_at((x,y),(255,255,255))

    def rotate(self,a):
        self.p1=rotatex(self.p1,a)
        self.p2=rotatex(self.p2,a)
        self.p3=rotatex(self.p3,a)
        return self

    def multiply(self):
        for i in range(0,2):
            self.p1[i]=self.p1[i]*100+width/2
            self.p2[i]=self.p2[i]*100+width/2
            self.p3[i]=self.p3[i]*100
            return self

background_colour = (0,0,0)
(width, height) = 601, 601

run=width/2


cube=   [Triangle((-1.0,-1.0,-1.0), 
    (-1.0,-1.0, 1.0),
    (-1.0, 1.0, 1.0)),Triangle( 
    (1.0, 1.0,-1.0), 
    (-1.0,-1.0,-1.0),
    (-1.0, 1.0,-1.0)),Triangle( 
    (1.0,-1.0, 1.0),
    (-1.0,-1.0,-1.0),
    (1.0,-1.0,-1.0)),Triangle(
    (1.0, 1.0,-1.0),
    (1.0,-1.0,-1.0),
    (-1.0,-1.0,-1.0)),Triangle(
    (-1.0,-1.0,-1.0),
    (-1.0, 1.0, 1.0),
    (-1.0, 1.0,-1.0)),Triangle(
    (1.0,-1.0, 1.0),
    (-1.0,-1.0, 1.0),
    (-1.0,-1.0,-1.0)),Triangle(
    (-1.0, 1.0, 1.0),
    (-1.0,-1.0, 1.0),
    (1.0,-1.0, 1.0)),Triangle(
    (1.0, 1.0, 1.0),
    (1.0,-1.0,-1.0),
    (1.0, 1.0,-1.0)),Triangle(
    (1.0,-1.0,-1.0),
    (1.0, 1.0, 1.0),
    (1.0,-1.0, 1.0)),Triangle(
    (1.0, 1.0, 1.0),
    (1.0, 1.0,-1.0),
    (-1.0, 1.0,-1.0)),Triangle(
    (1.0, 1.0, 1.0),
    (-1.0, 1.0,-1.0),
    (-1.0, 1.0, 1.0)),Triangle(
    (1.0, 1.0, 1.0),
    (-1.0, 1.0, 1.0),
    (1.0,-1.0, 1.0))]


def order(data):
   return sorted(data,key=(lambda a:a.p1[2]+a.p2[2]+a.p3[2]))


def matrixmultiply(a,matrix):#a is a tuple, matrix is the matrix
    b=list(range(0,3))
    b[0]=matrix[0][0]*a[0]+matrix[0][1]*a[1]+matrix[0][2]*a[2]
    b[1]=matrix[1][0]*a[0]+matrix[1][1]*a[1]+matrix[1][2]*a[2]
    b[2]=matrix[2][0]+a[0]+matrix[2][1]*a[1]+matrix[2][2]+a[2]
    return b


def rotatex(a,angle):#a is coordinates
    return matrixmultiply(a,((1,0,0),(0,math.cos(angle),-math.sin(angle)),(0,math.sin(angle),math.cos(angle))))


def main():
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Triangle Ray Tracer')
    screen.fill(background_colour)
    running = True

    multiply = lambda  a:a*100+width/2
    multiply2 = lambda  a:a*100

    cuber=list(map(lambda a:a.rotate(0.5),cube))
    cuber=order(cuber)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit(0)



        for i in range(1,35):
            if i%3==0:
               #print(cuber[i])
                cuber=list(map(lambda a:a.multiply(),cuber))
                print(cuber)
                list(map(lambda a:a.draw(screen),cuber))

            i+=1




       # triangle(screen,(width/2,height/2),(0,height/2),(0,0))



        pygame.display.flip()
        
if __name__ == "__main__":
    main()