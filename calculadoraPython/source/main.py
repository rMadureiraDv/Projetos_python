import os

#Funcion area -----------------
def calculo():
      mem1=mem2=op=i=0
      for i in range(0,len(calc),1):
            if ((calc[i] == '+')or(calc[i] == '-')or(calc[i] == '*')or(calc[i] == '/')):
                mem1 = calc[:i]
                op = calc[i]
                mem2 = calc[i+1:len(calc)]
                break;
      match (op):
            case '+':
                return float(mem1) + float(mem2)
            case '-':
                return float(mem1) - float(mem2)
            case '/':
                if (float(mem2) == 0):
                     return 0
                
                return float(mem1) / float(mem2) 
            case '*':
                return float(mem1) * float(mem2)
            case _  :
                return 0    
#Function area end----

#main area----
while (True):
    os.system("cls")
    calc = input("CALCULADORA EXTREMAMENTE SIMPLES APERTE [S] PARA SAIR\n>>>")
    if ((calc[0] == 's') or (calc[0]=='S')):
            break;
    elif(not calc[0].isdigit()):
         continue;
    print (f">>>{calculo():.2f}")
    os.system("pause")
    os.system("cls")
#main area end -------