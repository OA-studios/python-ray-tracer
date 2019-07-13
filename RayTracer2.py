import pygame , sys, math
from random import randint
 
background_colour = (0,0,0)
(width, height) = 601, 601

 

 
def circle (screen):
    a = 0
    b = 0


    for a in range(0,width):
        for b in range(0,height):
            i,j = normal(a,b)
            if (i)**2 + (j)**2 <= 1:
                k = getz(i,j)
                n=(i,j,k)

                
                l=norm((-10,1,10))

                R = 244 * getL(0.15,n,(l),0.4,0.5,10)
                G = 64  * getL(0.15,n,(l),0.4,0.5,10)
                B = 217 * getL(0.15,n,(l),0.4,0.5,10)
                screen.set_at((a,b), (int(R),int(G),int(B)))
 
def getz(x,y):
    k = math.sqrt(1-(y**2)-(x**2))
    return(k)
 
 
def normal(x,y):#only for use in 2d space with magnitude of the screen's width / height
    i = x/(width) * 2 -1
    j = y/(height) * 2 -1
    return(i,j)

def norm(m):#m=xyz to be normalized
    c=1/math.sqrt(m[0]**2+m[1]**2+m[2]**2)
    return (c*m[0],c*m[1],c*m[2])



def dot(a,b):#does the dot product of 2 3d coordinates and does max too
    n=(a[0]*b[0]+a[1]*b[1]+a[2]*b[2])
    if n<0:
        return 0
    return n

def getL(a,n,l,kd=1,ks=1,q=5):#a=ambient,n=point,return of getl(), kd= constant of diffuse, ks is the constant of specular and q is the brightness of the specular
    L=a + kd*dot(n,l) +getS(ks,n,l,q)
    if L>1:
        L=1
        #print("more")
    if L<a:
        L=a
        #print("less")
    return L

def getr(n,l):#gets reflection (n and l are tupels)
    R=2*dot(n,l)
    r=(R*n[0]-l[0]),(R*n[1]-l[1]),(R*n[2]-l[2])
    return r

def getS(k,n,l,q):#gets specular - k is brightness, n is pos, l is light pos, q is shinnieness
    S=k*dot((getr(n,l)),(0,0,1))**q
    return S




def triangle(screen,a,b,c,col=(255,255,255)):
#draws a triangle between the three points (a,b,c)



    x=1
    y=1

    #gradients
    l1m=(a[1]-b[1])/(a[0]-b[0])
    l2m=(a[1]-c[1])/(a[0]-c[0])
    l3m=(c[1]-b[1])/(c[0]-b[0])

    #intercepts
    l1C=(a[1]-l1m*(a[0]))
    l2C=(a[1]-l2m*(a[0]))
    l3C=(c[1]-l3m*(c[0]))

    #opposite
    l1opposite=(l1m*c[0]+l1C)
    l2opposite=(l2m*b[0]+l2C)
    l3opposite=(l3m*a[0]+l3C)

    for y in range(1,height):
        for x in range(1,width):
            l1y=(l1m*x)+ l1C

            l2y=(l2m*x)+ l2C

            l3y=(l3m*x)+ l3C


            if (y<=l1y)==(c[1]<=l1opposite)  and (y>=l2y)==(b[1]>=l2opposite) and (y>=l3y)==(a[1]>=l3opposite):
                screen.set_at((x,y),(col))

        






def main():
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Ray Tracer')
    screen.fill(background_colour)
    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit(0)
        circle(screen)
        triangle(screen,(400,500),(300,300),(100,100))
        pygame.display.flip()
        
if __name__ == "__main__":
    main()