from visual.graph import * #graphics and math classes
scene=display(x=0,y=0,width=700,height=200,range=700,
           title='Linear Accelerator. E: electric field white arrows')
ball=sphere(pos=(-600,0,0),radius=10,color=color.green)  #the electron
ball.trail=curve(color=color.red,radius=3)
arrow1=arrow(color=color.white)                                       #arrows for electric field
arrow2=arrow()                   #In this way, arrows will be erased
arrow3=arrow()
arrow4=arrow()
arrow5=arrow()  
def tube(xpos,length):   
     pipe=helix(pos=(xpos,0,0),radius=30,axis=(length,0,0),coils=length*0.15,
                thickness=5,color=color.orange)     
def linac():                     #plots the tubes
    xpos=-600
    for i in range(1,7):
        length=80*math.sqrt(i)
        gap=70   
        tube(xpos,length)
        xpos=xpos+gap+length
        
def oscillator():                 #a sine wave represents the potential
    incr=math.pi/8.0              #between the gaps
    initime=10*incr               #begins with a phase difference
    xx=-600                       
    for j in range(1,7):
        xxincr=80*math.sqrt(j)/14.0  #each tube is divided in 14 parts
        for i in range(1,17):        #and the electron jumps in them
            rate(15)                 #smaller rates for slower motion
            ar=math.sin(initime+i*incr) #a sine potential
            if ar>=0 :
                apos=0
            else:
                apos=70
            posx1=80-600+apos +xxincr        #initial position of electron
            arrow1.pos=vector(posx1,0,0)      
            arrow1.axis=(70*ar,0,0)
            posx2=posx1+80*math.sqrt(2)+70      #shows the oscillating
            arrow2.pos=vector(posx2,0,0)        #electric fields
            arrow2.axis=(70*ar,0,0)
            posx3=posx2+80*math.sqrt(3)+70
            arrow3.pos=vector(posx3,0,0)
            arrow3.axis=(70*ar,0,0)
            posx4=posx3+80*math.sqrt(4)+70
            arrow4.pos=vector(posx4,0,0)
            arrow4.axis=(70*ar,0,0)
            posx5=posx4+80*math.sqrt(5)+70
            arrow5.pos=vector(posx5,0,0)
            arrow5.axis=(70*ar,0,0)
            if i<15:    xx +=xxincr    #inside the gap the velocity increases
            if i==15:
                xx +=35
            if  i==16:                 
                xx +=35
           
            ball.pos=vector(xx,0,0)   #plots the electron position
            ball.trail.append(pos=(xx,0,0))    #trail left by the electron 
linac()
oscillator()
