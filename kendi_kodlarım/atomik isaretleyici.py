#!/usr/bin/env python
# coding: utf-8

# In[2]:


from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from os import path
import math

konum="C:\\Users\\conro\\OneDrive\\Masaüstü\\MetalDatabase.txt"
bcc=list()
fcc=list()
hcp=list()
pointers=list()
allof=list()
if(path.exists(konum)):
    file=open(konum,"r")
    for i in file:
        a=i.rstrip()
        text=a.split("\t")
        allof.append(text)
    bcc_p=allof.index(["BCC"])
    fcc_p=allof.index(["FCC"])
    hcp_p=allof.index(["HCP"])
    
    uzunluk=len(allof)
    for ankara in allof[bcc_p+1:fcc_p]:
        if(ankara[2]==""):
            ankara.remove("")
        bcc.append(ankara)
        
    for istanbul in allof[fcc_p+1:hcp_p]:
        if(istanbul[2]==""):
            istanbul.remove("")
        fcc.append(istanbul)
        
    for izmir in allof[hcp_p+1:uzunluk-1]:
        if(izmir[2]==""):
            izmir.remove("")
        hcp.append(izmir)
      
    while(True):
        print("*********************************************")
        print("İSTEDİĞİNİZ İŞLEMİ SECİNİZ:")
        print("ELLE VERİ GİR:1")
        print("PROGRAMI KAPAT:2")
        print("*********************************************")
        girdi=input("SECİMİNİZ:")
        if(girdi=="1"):
            print("-----------------------------------------------")
            print("Lütfen elementin sembolünü giriniz :")
            print("-----------------------------------------------")
            sembol=input("SEMBOL:")
            for metal in bcc:
                coordinates=list()
                symbol=(metal[0]).lower()
                aranan=sembol.lower()
                if(aranan==symbol):
                    a=input("A degerini giriniz(x ekseni):")
                    b=input("B degerini giriniz(y ekseni):")
                    c=input("C degerini giriniz(z ekseni):")
                    
                    
                    olcut=float(metal[2])
                    x_atom_sayısı=float(a)//olcut
                    y_atom_sayısı=float(b)//olcut
                    z_atom_sayısı=float(c)//olcut
                    
                    lattice=2*(2**(1/2))*olcut
                    if((x_atom_sayısı)>0 and (y_atom_sayısı)>0 and (z_atom_sayısı)>0):
                        tüm=list()
                        atom_1=[0,0,0]#merkez atom
                        tüm.append(atom_1)
                        x=list()
                        y=list()
                        z=list()
                        xy=list()
                        yz=list()
                        xz=list()
                        xyz=list()
                        counter=1
                        while(counter<x_atom_sayısı+1):
                            arr=[counter*lattice,0,0]
                            tüm.append(arr)
                            x.append(arr)
                            counter=counter+1
                       
                        counter=1
                        while(counter<y_atom_sayısı+1):
                            arr=[0,counter*lattice,0]
                            tüm.append(arr)
                            y.append(arr)
                            counter=counter+1
                        counter=1
                        
                        while(counter<z_atom_sayısı+1):
                            arr=[0,0,counter*lattice]
                            tüm.append(arr)
                            z.append(arr)
                            counter=counter+1
                        counter=1
                        
                        while(counter<=y_atom_sayısı):
                            for i in x:
                                arr=[i[0],counter*lattice,0]
                                xy.append(arr)
                                tüm.append(arr)
                            counter=counter+1
                        counter=1
                        while(counter<=z_atom_sayısı):
                            for i in y:
                                arr=[0,i[1],counter*lattice]
                                yz.append(arr)
                                tüm.append(arr)
                            counter=counter+1
                        counter=1
                        while(counter<=x_atom_sayısı):
                            for i in z:
                                arr=[counter*lattice,0,i[2]]
                                xz.append(arr)
                                tüm.append(arr)
                            counter=counter+1
                        counter=1
                        while(counter<=x_atom_sayısı):
                            for i in yz:
                                arr=[counter*lattice,i[1],i[2]]
                                if not(arr in xyz and arr in tüm):
                                    xyz.append(arr)
                                    tüm.append(arr)
                            counter=counter+1
                        counter=1
                        while(counter<=y_atom_sayısı):
                            for i in xz:
                                arr=[i[0],counter*lattice,i[2]]
                                if not(arr in xyz and arr in tüm):
                                    xyz.append(arr)
                                    tüm.append(arr)
                            counter=counter+1
                        counter=1
                        while(counter<=z_atom_sayısı):
                            for i in xy:
                                arr=[i[0],i[1],counter*lattice]
                                if not(arr in xyz and arr in tüm):
                                    xyz.append(arr)
                                    tüm.append(arr)
                            counter=counter+1
                        
                        tüm.append([lattice/2,lattice/2,lattice/2])
                        counter=1
                        for i in yz:
                            k=[counter*lattice/2,i[1]-lattice/2,i[2]-lattice/2]
                            if((i[1]-lattice/2)>0 and (i[2]-lattice/2)>0 and not(k in tüm)):
                                
                                xyz.append(k)
                                tüm.append(k)
                                counter=counter+1
                        counter=1
                        for i in xy:
                            k=[i[0]-lattice/2,i[1]-lattice/2,counter*lattice/2]
                            if((i[0]-lattice/2)>0 and (i[1]-lattice/2)>0 and not(k in tüm)):
                                
                                xyz.append(k)
                                tüm.append(k)
                                counter=counter+1
                        counter=1
                        for i in xz:
                            k=[i[0]-lattice/2,counter*lattice/2,i[2]-lattice/2]
                            if((i[0]-lattice/2)>0 and (i[2]-lattice/2)>0 and not(k in tüm)):
                                
                                xyz.append(k)
                                tüm.append(k)
                                counter=counter+1
                        x_value=list()
                        y_value=list()
                        z_value=list()
                        
                        for i in tüm:
                            x_value.append(i[0])
                            y_value.append(i[1])
                            z_value.append(i[2])
                        fig = pyplot.figure()
                        ax = Axes3D(fig)
                        
                        # Generate the values
                        x_vals = x_value
                        y_vals = y_value
                        z_vals = z_value
                        # Plot the values
                        ax.scatter(x_vals, y_vals, z_vals)
                        ax.set_xlabel('X-axis')
                        ax.set_ylabel('Y-axis')
                        ax.set_zlabel('Z-axis')

                        pyplot.show()
                        file1=open("C:\\Users\\conro\\OneDrive\\Masaüstü\\{}.txt".format(metal[1]),"w")
                        file1.write("Name:{}".format(metal[0]))
                        file1.write("\nAtomic Radius:{}".format(metal[2]))
                        file1.write("\nStructure:BCC")
                        file1.write("\nDimensions:x0,y:0,z:0")
                        file1.write("\nTotal number of atoms:9")
                        file1.write("\n\t \t \t X \t \t Y \t \t Z")
                        counter=1
                        for i in tüm:
                            file1.write("\nAtom{}--{}-----------------{}-----------------{}".format(counter,i[0],i[1],i[2]))
                            counter=counter+1
                        file1.close()
                        
                    else:
                        print("HATALI DEGER GİRİSİ YAPTINIZ LÜTFEN MESAFELERİN LATTİCE DEGERİNDEN BÜYÜK EŞİT OLDUGUNU KONTROL EDİNİZ")
                    
            for metal in fcc:
                symbol=(metal[0]).lower()
                aranan=sembol.lower()
                if(aranan==symbol):
                    olcut=metal[2]
                    print("FCC")
                    a=input("A degerini giriniz(x ekseni):")
                    b=input("B degerini giriniz(y ekseni):")
                    c=input("C degerini giriniz(z ekseni):")
                    
                    
                    olcut=float(metal[2])
                    x_atom_sayısı=float(a)//olcut
                    y_atom_sayısı=float(b)//olcut
                    z_atom_sayısı=float(c)//olcut
                 
                   
                    lattice=2*(2**(1/2))*olcut
                    if((x_atom_sayısı)>0 and (y_atom_sayısı)>0 and (z_atom_sayısı)>0):
                        tüm=list()
                        atom_1=[0,0,0]#merkez atom
                        tüm.append(atom_1)
                        x=list()
                        y=list()
                        z=list()
                        xy=list()
                        yz=list()
                        xz=list()
                        xyz=list()
                        counter=1
                        while(counter<x_atom_sayısı+1):
                            arr=[counter*lattice,0,0]
                            if(not (arr in xy)):
                                tüm.append(arr)
                                x.append(arr)
                            counter=counter+1
                       
                        counter=1
                        while(counter<y_atom_sayısı+1):
                            arr=[0,counter*lattice,0]
                            if(not (arr in xy)):
                                tüm.append(arr)
                                y.append(arr)
                            counter=counter+1
                        counter=1
                        
                        while(counter<z_atom_sayısı+1):
                            arr=[0,0,counter*lattice]
                            if(not (arr in xy)):
                                tüm.append(arr)
                                z.append(arr)
                            counter=counter+1
                        counter=1
                        
                        while(counter<=y_atom_sayısı):
                            for i in x:
                                arr=[i[0],counter*lattice,0]
                                arr1=[i[0],counter*lattice/2,0]
                                if(not((arr in xy) and arr1 in xy)):
                                    xy.append(arr)
                                    xy.append(arr1)
                                    tüm.append(arr)
                                    tüm.append(arr1)
                            counter=counter+1
                        counter=1
                        while(counter<=z_atom_sayısı):
                            for i in y:
                                arr=[0,i[1],counter*lattice]
                                arr1=[0,i[1],counter*lattice/2]
                                if(not((arr in yz) and arr1 in yz)):
                                    yz.append(arr)
                                    yz.append(arr1)
                                    tüm.append(arr)
                                    tüm.append(arr1)
                            counter=counter+1
                        counter=1
                        while(counter<=x_atom_sayısı):
                            for i in z:
                                arr=[counter*lattice,0,i[2]]
                                arr1=[counter*lattice/2,0,i[2]]
                                if(not((arr in xz) and arr1 in xz)):
                                    xz.append(arr)
                                    xz.append(arr1)
                                    tüm.append(arr)
                                    tüm.append(arr1)
                            counter=counter+1
                        counter=1
                        while(counter<=x_atom_sayısı):
                            for i in yz:
                                arr=[counter*lattice,i[1],i[2]]
                                if not(arr in xyz and arr in tüm):
                                    xyz.append(arr)
                                    tüm.append(arr)
                            counter=counter+1
                        counter=1
                        while(counter<=y_atom_sayısı):
                            for i in xz:
                                arr=[i[0],counter*lattice,i[2]]
                                if not(arr in xyz and arr in tüm):
                                    xyz.append(arr)
                                    tüm.append(arr)
                            counter=counter+1
                        counter=1
                        while(counter<=z_atom_sayısı):
                            for i in xy:
                                arr=[i[0],i[1],counter*lattice]
                                if not(arr in xyz and arr in tüm):
                                    xyz.append(arr)
                                    tüm.append(arr)
                            counter=counter+1
                        
                        tüm.append([lattice/2,lattice/2,lattice/2])
                        counter=1
                        for i in yz:
                            k=[counter*lattice/2,i[1],i[2]-lattice/2]
                            m=[counter*lattice/2,i[1]-lattice/2,i[2]]
                            l=[counter*lattice/2,i[1]-lattice/2,i[2]-lattice/2]
                            if((i[1]-lattice/2)>0 and (i[2]-lattice/2)>0 and not(k in tüm)):
                                if((i[1]-lattice/2)>0 and (i[2]-lattice/2)>0 and not(m in tüm)):
                                    if((i[1]-lattice/2)>0 and (i[2]-lattice/2)>0 and not(l in tüm)):
                                        xyz.append(l)
                                        tüm.append(l)
                                        xyz.append(m)
                                        tüm.append(m)
                                        xyz.append(k)
                                        tüm.append(k)
                                        counter=counter+1
                        x_value=list()
                        y_value=list()
                        z_value=list()
                        tüm1=list()
                        for k in tüm:
                            if not(k in tüm1):
                                tüm1.append(k)
                        tüm=tüm1
                        for i in tüm:
                            x_value.append(i[0])
                            y_value.append(i[1])
                            z_value.append(i[2])
                        fig = pyplot.figure()
                        ax = Axes3D(fig)
                        
                        # Generate the values
                        x_vals = x_value
                        y_vals = y_value
                        z_vals = z_value
                        # Plot the values
                        ax.scatter(x_vals, y_vals, z_vals)
                        ax.set_xlabel('X-axis')
                        ax.set_ylabel('Y-axis')
                        ax.set_zlabel('Z-axis')

                        pyplot.show()
                        file1=open("C:\\Users\\conro\\OneDrive\\Masaüstü\\{}.txt".format(metal[1]),"w")
                        file1.write("Name:{}".format(metal[0]))
                        file1.write("\nAtomic Radius:{}".format(metal[2]))
                        file1.write("\nStructure:BCC")
                        file1.write("\nDimensions:x0,y:0,z:0")
                        file1.write("\nTotal number of atoms:9")
                        file1.write("\n\t \t \t X \t \t Y \t \t Z")
                        counter=1
                        for i in tüm:
                            file1.write("\nAtom{}--{}-----------------{}-----------------{}".format(counter,i[0],i[1],i[2]))
                            counter=counter+1
                        file1.close()
                        
                    else:
                        print("HATALI DEGER GİRİSİ YAPTINIZ LÜTFEN MESAFELERİN LATTİCE DEGERİNDEN BÜYÜK EŞİT OLDUGUNU KONTROL EDİNİZ")
                    
                    
            for metal2 in hcp:
                symbol2=(metal2[0]).lower()
                aranan2=sembol.lower()
                if(aranan2==symbol2):
                    olcut=metal2[3]
                    
                    
                    
        elif(girdi=="2"):
            break
        else:
            print("HATALI GİRİS YAPTINIZ!")


# 

# In[ ]:





# In[ ]:




