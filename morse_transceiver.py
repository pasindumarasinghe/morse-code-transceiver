print("-------------------------")
print("tranciever  of morse code")
print("-------------------------")

print("Transmitter=T,Reciever=R")
mode=input("Enter Transmitter or Reciever? ")

if mode=="T":
    from pyfirmata import Arduino,OUTPUT
    #import inbuilt time module
    import time

    # creat an Arduino board instanse
    board=Arduino("COM11")
    # digital pin number
    led_pin=6
    buzzer = board.get_pin('d:9:p')
    # set it as an output pin
    board.digital[led_pin].mode=OUTPUT
    print("---------------------")
    print('MORSE CODE TRANSMITTER')
    print("----------------------")
    transmit_dict = {
        "a" : "iol",
        "b" : "loioioi",
        "c" : "loioloi",
        "d" : "loioi",
        "e" : "i",
        "f" : "ioioloi",
        "g" : "loloi",
        "h" : "ioioioi",
        "i" : "ioi",
        "j" : "iololol",
        "k" : "loiol",
        "l" : "ioloioi",
        "m" : "lol",
        "n" : "loi",
        "o" : "lolol",
        "p" : "iololoi",
        "q" : "loloiol",
        "r" : "ioloi",
        "s" : "ioioi",
        "t" : "l",
        "u" : "ioiol",
        "w" : "iolol",
        "x" :"loioiolo",
        "y" : "loiolol",
        "z" : "loloioi",
        "1" : "iolololol",
        "2" : "ioiololol",
        "3" : "ioioiolol",
        "4" : "ioioioiol",
        "5" : "ioioioioio",
        "6" : "loioioioi",
        "7" : "loloioioi",
        "8" : "lololoioi",
        "9" : "lolololoi",
        "0" : "lolololol",
        " " : "ooooooo",
}
    while True:
        message=input("Enter message :")
        List=list(message)
        print('Sending:',end='')
        for i in range(0,len(List)):
            character=List[i]
            s1=transmit_dict.get(character)
            s1=str(s1)
            n=len(s1)
            for j in range(0,n):
                morse=s1[j]
                if morse=="i":
                    print(".",end ='')
                    board.digital[led_pin].write(1)
                    buzzer.write(1)
                    time.sleep(0.2)
                    board.digital[led_pin].write(0)
                    buzzer.write(0)
                    
                
                elif morse=="o":
                    print(" ",end ='')
                    board.digital[led_pin].write(0)
                    time.sleep(0.2)
                
             
                elif morse=="l":
                    print("-",end ='')
                    board.digital[led_pin].write(1)
                    buzzer.write(0.9)
                    time.sleep(0.6)
                    board.digital[led_pin].write(0)
                    buzzer.write(0)
                    
                    
            board.digital[led_pin].write(0)
            time.sleep(0.4)
        board.digital[led_pin].write(1)
        time.sleep(1.2)
        board.digital[led_pin].write(0)
        print('\n')

        
        
elif mode=="R":
    from pyfirmata import Arduino,util,OUTPUT,INPUT
    import time
    board=Arduino("COM11")
    ldr_pin=0
    #set it as an input pin
board.analog[ldr_pin].mode=INPUT
board.analog[ldr_pin].enable_reporting()
it=util.Iterator(board)
it.start()
print('-------------------')
print('MORSE CODE RECEIVER')
print('-------------------')
print('Reciving:',end='')
 
receive_dict = {
    '.-':'a',
    '-...':'b',
    '-.-.':'c',
    '-..':'d',
    '.':'e',
    '..-.':'f',
    '--.':'g',
    '....':'h',
    '..':'i',
    '.---':'j',
    '-.-':'k',
    '.-..':'l',
    '--':'m',
    '-.':'n',
    '---':'o',
    '.--.':'p',
    '--.-':'q',
    '.-.':'r',
    '...':'s',
    '-':'t',
    '..-':'u',
    '...-':'v',
    '.--':'w',
    '-..-':'x',
    '-.--':'y',
    '--..':'z',
    '.----':'1',
    '..---':'2',
    '...--':'3',
    '....-':'4',
    '.....':'5',
    '-....':'6',
    '--...':'7',
    '---..':'8',
    '----.':'9',
    '-----':'0',
    '       ':' '
}

ldr_v=0.4 #if l>ldr_v:on  if l<ldr_v:off
#create a morse code list
m_c=[]
#string
st=[]
while True:
    l=board.analog[ldr_pin].read()
    #ON
    t_b=time.time()#time before
    while l>ldr_v:
        l=board.analog[ldr_pin].read()
        time.sleep(0.05)
    t_a=time.time()#time after
    #OFF
    T_B=time.time()#time before
    while l<ldr_v:
        l=board.analog[ldr_pin].read()
        time.sleep(0.05)
    T_A=time.time()#time before
    dt=t_a-t_b #on time
    DT=T_A-T_B #off time
    #print(dt)
    if (0.1<dt<0.3):
        m_c.append('.')
        #print('.',end='')
    if (0.5<dt<0.7):
        m_c.append('-')
        #print('-',end='')
    if (0.3<DT<0.5):
        m=''
        for x in m_c:
            m=m+x #m:morse code string
        ch=receive_dict[m]
        print(ch,end=' ')
        st.append(ch)
        m_c=[]
    if (1.1<dt<1.3):
        print('\n')
        print('Message:',end='')
        for x in st:
            print(x,end='')
        st=[]
        print('\n')
            
            
        
        
            
            
         
        
     
     
