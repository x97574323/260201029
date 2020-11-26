while(True):
    arry1=[1,2,3]
    arry2=[4,5,6]
    arry3=[7,8,9]
    new_arr=[arry1,arry2,arry3]
    print("*****************************************")
    print("            X-O-X'e HOŞGELDİNİZ          ")
    print("*****************************************")
    choice=input("               EXIT:1 ,PLAY:2             ")
    if choice=="1":
        break
    elif choice=="2":
        counter=0
        while(counter<10):
            print("X-O-X oynamak icin numaralndırılmıs karelerden birisini giriniz:")
            print("{} | {} | {}".format(new_arr[0][0],new_arr[0][1],new_arr[0][2]))
            print("---------")
            print("{} | {} | {}".format(new_arr[1][0],new_arr[1][1],new_arr[1][2]))
            print("---------")        
            print("{} | {} | {}".format(new_arr[2][0],new_arr[2][1],new_arr[2][2]))
            number=input("Pls input your number:")
            if(number=="1"):
                if(new_arr[0][0]==1):
                  if(counter%2==1):
                    new_arr[0][0]="x"
                  else:
                    new_arr[0][0]="o"
                counter=counter+1
            elif(number=="2"):
                if(new_arr[0][1]==2):
                  if(counter%2==1):
                    new_arr[0][1]="x"
                  else:
                    new_arr[0][1]="o"
                counter=counter+1
            elif(number=="3"):
                if(new_arr[0][2]==3):
                  if(counter%2==1):
                    new_arr[0][2]="x"
                  else:
                    new_arr[0][2]="o"
                counter=counter+1
            elif(number=="4"):
                if(new_arr[1][0]==4):
                  if(counter%2==1):
                    new_arr[1][0]="x"
                  else:
                    new_arr[1][0]="o"
                counter=counter+1
            elif(number=="5"):
                if(new_arr[1][1]==5):
                  if(counter%2==1):
                    new_arr[1][1]="x"
                  else:
                    new_arr[1][1]="o"
                counter=counter+1
            elif(number=="6"):
                if(new_arr[1][2]==6):
                  if(counter%2==1):
                    new_arr[1][2]="x"
                  else:
                    new_arr[1][2]="o"
                counter=counter+1
            elif(number=="7"):
                if(new_arr[2][0]==7):
                  if(counter%2==1):
                    new_arr[2][0]="x"
                  else:
                    new_arr[2][0]="o"
                counter=counter+1
            elif(number=="8"):
                if(new_arr[2][1]==8):
                  if(counter%2==1):
                    new_arr[2][1]="x"
                  else:
                    new_arr[2][1]="o"
                counter=counter+1
            elif(number=="9"):
                if(new_arr[2][2]==9):
                  if(counter%2==1):
                    new_arr[2][2]="x"
                  else:
                    new_arr[2][2]="o"
                counter=counter+1
            else:
                print("Wrong input!!!")
                
            if(new_arr[0][0]=="x" and new_arr[0][1]=="x" and new_arr[0][2]=="x"):
                print("X wins")
                break
            if(new_arr[0][0]=="o" and new_arr[0][1]=="o" and new_arr[0][2]=="o"):
                print("o wins")
                break
            if(new_arr[1][0]=="x" and new_arr[1][1]=="x" and new_arr[1][2]=="x"):
                print("X wins")
                break
            if(new_arr[1][0]=="o" and new_arr[1][1]=="o" and new_arr[1][2]=="o"):
                print("o wins")
                break
            if(new_arr[2][0]=="x" and new_arr[2][1]=="x" and new_arr[2][2]=="x"):
                print("x wins")
                break
            if(new_arr[2][0]=="o" and new_arr[2][1]=="o" and new_arr[2][2]=="o"):
                print("o wins")
                break
            if(new_arr[0][0]=="x" and new_arr[1][0]=="x" and new_arr[2][0]=="x"):
                print("x wins")
                break
            if(new_arr[0][0]=="o" and new_arr[1][0]=="o" and new_arr[2][0]=="o"):
                print("o wins")
                break
            if(new_arr[0][1]=="x" and new_arr[1][1]=="x" and new_arr[2][1]=="x"):
                print("x wins")
                break
            if(new_arr[0][1]=="o" and new_arr[1][1]=="o" and new_arr[2][1]=="o"):
                print("o wins")
                break
            if(new_arr[0][2]=="x" and new_arr[1][2]=="x" and new_arr[2][2]=="x"):
                print("x wins")
                break
            if(new_arr[0][2]=="o" and new_arr[1][2]=="o" and new_arr[2][2]=="o"):
                print("o wins")
                break
            if(new_arr[0][0]=="x" and new_arr[1][1]=="x" and new_arr[2][2]=="x"):
                print("x wins")
                break
            if(new_arr[0][0]=="o" and new_arr[1][1]=="o" and new_arr[2][2]=="o"):
                print("o wins")
                break
            if(new_arr[0][2]=="x" and new_arr[1][1]=="x" and new_arr[2][0]=="x"):
                print("x wins")
                break
            if(new_arr[0][2]=="o" and new_arr[1][1]=="o" and new_arr[2][0]=="o"):
                print("o wins")
                break
            if(counter==9):
              print("Berabere")
              break 
            
