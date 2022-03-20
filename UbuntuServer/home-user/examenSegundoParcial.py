from Tkinter import *
import ttk
import tkFont
import tkMessageBox
import os
import time
import subprocess
import ScrolledText



v0 = Tk()
v0.title("EXAMEN SEGUNDO PARCIAL")
v0.geometry("600x600+0+0")

cmdOn21 = 'sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/on21.sh"'
cmdOff21 = 'sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/off21.sh"'
cmdOn22 = 'sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/on22.sh"'
cmdOff22 = 'sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/off22.sh"'
cmdOn23 = 'sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/on23.sh"'
cmdOff23 = 'sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/off23.sh"'

formato = tkFont.Font(family="Helvetica", size=12)
label = Label(v0, text="Desarrollado en Equipo",font=formato).place(x=165, y=10)


img_on = PhotoImage(file="on.gif")
img_off = PhotoImage(file="off.gif")

def limpiar():
              horaInicial.set("")
              minInicial.set("")
              horaFinal.set("")
              minFinal.set("")

def salida():
             v0.destroy()

def registrar21():
                print "REGISTRADO"
                hi=horaInicial.get()
                mi=minInicial.get()
                hf=horaFinal.get()
                mf=minFinal.get()
                tab=" "
                dia="*"
                mes="*"
                ano="*"
                usuario="root"
                path1='sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/on21.sh"'
                path2='sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/off21.sh"'

                #Asignar permisos de escritura y ejecucion

                os.system("sudo chmod -R 777 /etc/cron.d/tarea1")
                os.system("sudo chmod -R 777 /etc/cron.d/tarea2")

                #cadena
                cadena=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
                cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))

                # aperturar archivo

                pf=open("/etc/cron.d/tarea1","w")
                pf.write(cadena)
                pf.write("\n")
                pf.close()
                
                pf=open("/etc/cron.d/tarea2","w")
                pf.write(cadena2)
                pf.write("\n")
                pf.close()
                time.sleep(0.1)


                #Revertir permiso
                os.system("sudo chmod -R 755 /etc/cron.d/tarea1")
                os.system("sudo chmod -R 755 /etc/cron.d/tarea2")

                #Reiniciar servicios
                os.system("sudo /etc/init.d/cron restart")
                limpiar()
                tkMessageBox.showinfo("save",message="Tiempos registrado")

          
                
def registrar22():
                print "REGISTRADO"
                hi=horaInicial.get()
                mi=minInicial.get()
                hf=horaFinal.get()
                mf=minFinal.get()
                tab=" "
                dia="*"
                mes="*"
                ano="*"
                usuario="root"
                path1='sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/on22.sh"'
                path2='sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/off22.sh"'

                #Asignar permisos de escritura y ejecucion

                os.system("sudo chmod -R 777 /etc/cron.d/tarea3")
                os.system("sudo chmod -R 777 /etc/cron.d/tarea4")

                #cadena
                cadena=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
                cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))

                # aperturar archivo

                pf=open("/etc/cron.d/tarea3","w")
                pf.write(cadena)
                pf.write("\n")
                pf.close()
                
                pf=open("/etc/cron.d/tarea4","w")
                pf.write(cadena2)
                pf.write("\n")
                pf.close()
                time.sleep(0.1)


                #Revertir permiso
                os.system("sudo chmod -R 755 /etc/cron.d/tarea3")
                os.system("sudo chmod -R 755 /etc/cron.d/tarea4")

                #Reiniciar servicios
                os.system("sudo /etc/init.d/cron restart")
                limpiar()
                tkMessageBox.showinfo("save",message="Tiempos registrado")

                     

def registrar23():
                print "REGISTRADO"
                hi=horaInicial.get()
                mi=minInicial.get()
                hf=horaFinal.get()
                mf=minFinal.get()
                tab=" "
                dia="*"
                mes="*"
                ano="*"
                usuario="root"
                path1='sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/on23.sh"'
                path2='sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/off23.sh"'

                #Asignar permisos de escritura y ejecucion

                os.system("sudo chmod -R 777 /etc/cron.d/tarea5")
                os.system("sudo chmod -R 777 /etc/cron.d/tarea6")

                #cadena
                cadena=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
                cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))

                # aperturar archivo

                pf=open("/etc/cron.d/tarea5","w")
                pf.write(cadena)
                pf.write("\n")
                pf.close()
                
                pf=open("/etc/cron.d/tarea6","w")
                pf.write(cadena2)
                pf.write("\n")
                pf.close()
                time.sleep(0.1)


                #Revertir permiso
                os.system("sudo chmod -R 755 /etc/cron.d/tarea5")
                os.system("sudo chmod -R 755 /etc/cron.d/tarea6")

                #Reiniciar servicios
                os.system("sudo /etc/init.d/cron restart")
                limpiar()
                tkMessageBox.showinfo("save",message="Tiempos registrado")
                
              

def abrirVentana21():
                     ventana21 = Toplevel(v0)
                     ventana21.geometry("600x600+0+0")
                     titulo21 = Label(ventana21, text="OPCION GPIO-21")
                     label = Label(ventana21, text="SE ENCUENTRA EN GPIO-21",font=formato).place(x=165, y=10)
                     
                     global horaInicial
                     global minInicial
                     global horaFinal
                     global minFinal
                     
                     def lecturaOn ():
                                      os.system('sudo /./home/fcarmona/lectura21on.sh > /home/fcarmona/gpio21.txt')
                                      pf=open("/home/fcarmona/gpio21.txt","r")
                                      for linea in pf:
                                                      campo=linea.split("\n")
                                                      campof=campo[0]
                                                      if (campof=="1"):
                                                                       
                                                                       imagenOn=Button(ventana21,image=img_on).place(x=320, y=102)
                                                                       text1= tkFont.Font(family="Arial",size ="20")
                                                                       label1 = Label(ventana21,text="1",font=text1).place(x=300,y=50)
                                                                       ventana21.after(1000,lecturaOn)
                                                      if (campof=="0"):
                                                                       text1= tkFont.Font(family="Arial",size ="20")
                                                                       imagenOn=Button(ventana21,image=img_off).place(x=320, y=102)
                                                                       label1 = Label(ventana21,text="0",font=text1).place(x=300,y=50)
                                                                       ventana21.after(1000,lecturaOn)
                     lecturaOn()

                     def on():
                              os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/on21.sh"')

                     def off():
                               os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/off21.sh"')

                     def salida():
                                  ventana21.destroy()
                                  ventana21.update()
                     
                                
                     btn_on21 = Button(ventana21,text="ENCENDER                         ", command=on).place(x=50, y=50)
                     btn_off21 = Button(ventana21,text="APAGAR                             ", command=off).place(x=50, y=110)
                     btn_retorno = Button(ventana21, text="RETORNO MENU PRINCIPAL", command=salida).place(x=50, y=180)
                     
                     minInicial=StringVar()
                     horaInicial=StringVar()
                     minFinal=StringVar()
                     horaFinal=StringVar()

                     label_horaInicial =Label(ventana21, text="Hora Inicial").place(x=10,y=250)
                     txt_horaInicial = Entry(ventana21, textvariable=horaInicial, width=20).place(x=130, y=250)

                     label_minInicial =Label(ventana21, text="Minuto Inicial").place(x=10,y=280)
                     txt_minInicial = Entry(ventana21, textvariable=minInicial, width=20).place(x=130, y=280)

                     label_horaFinal =Label(ventana21, text="Hora Final").place(x=10,y=310)
                     txt_horaFinal = Entry(ventana21, textvariable=horaFinal, width=20).place(x=130, y=310)

                     label_minFinal =Label(ventana21, text="Minuto Final").place(x=10,y=340)
                     txt_minFinal = Entry(ventana21, textvariable=minFinal, width=20).place(x=130, y=340)
                     
                     btn_guardar=Button(ventana21,text="GUARDAR", command=registrar21).place(x=150,y=385)

def abrirVentana22():
                     ventana22 = Toplevel(v0)
                     ventana22.geometry("600x600+0+0")
                     titulo22 = Label(ventana22, text="OPCION GPIO22")
                     label = Label(ventana22, text="SE ENCUENTRA EN GPIO-22",font=formato).place(x=165, y=10)
                     global horaInicial
                     global minInicial
                     global horaFinal
                     global minFinal   
                     
                     def lecturaOn ():
                                      os.system('sudo /./home/fcarmona/lectura22on.sh > /home/fcarmona/gpio22.txt')
                                      pf=open("/home/fcarmona/gpio22.txt","r")
                                      for linea in pf:
                                                      campo=linea.split("\n")
                                                      campof=campo[0]
                                                      if (campof=="1"):
                                                                       
                                                                       imagenOn=Button(ventana22,image=img_on).place(x=320, y=102)
                                                                       text1= tkFont.Font(family="Arial",size ="20")
                                                                       label1 = Label(ventana22,text="1",font=text1).place(x=300,y=50)
                                                                       ventana22.after(1000,lecturaOn)
                                                      if (campof=="0"):
                                                                       text1= tkFont.Font(family="Arial",size ="20")
                                                                       imagenOn=Button(ventana22,image=img_off).place(x=320, y=102)
                                                                       label1 = Label(ventana22,text="0",font=text1).place(x=300,y=50)
                                                                       ventana22.after(1000,lecturaOn)
                     lecturaOn()

                     def on():
                              os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/on22.sh"')

                     def off():
                               os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/off22.sh"')

                     def salida():
                                  ventana22.destroy()
                                  ventana22.update()
                     
                                
                     btn_on22 = Button(ventana22,text="ENCENDER                         ", command=on).place(x=50, y=50)
                     btn_off22 = Button(ventana22,text="APAGAR                             ", command=off).place(x=50, y=110)
                     btn_retorno = Button(ventana22, text="RETORNO MENU PRINCIPAL", command=salida).place(x=50, y=180)

                     minInicial=StringVar()
                     horaInicial=StringVar()
                     minFinal=StringVar()
                     horaFinal=StringVar()

                     label_horaInicial =Label(ventana22, text="Hora Inicial").place(x=10,y=250)
                     txt_horaInicial = Entry(ventana22, textvariable=horaInicial, width=20).place(x=130, y=250)

                     label_minInicial =Label(ventana22, text="Minuto Inicial").place(x=10,y=280)
                     txt_minInicial = Entry(ventana22, textvariable=minInicial, width=20).place(x=130, y=280)

                     label_horaFinal =Label(ventana22, text="Hora Final").place(x=10,y=310)
                     txt_horaFinal = Entry(ventana22, textvariable=horaFinal, width=20).place(x=130, y=310)

                     label_minFinal =Label(ventana22, text="Minuto Final").place(x=10,y=340)
                     txt_minFinal = Entry(ventana22, textvariable=minFinal, width=20).place(x=130, y=340)
                     
                     btn_guardar=Button(ventana22,text="GUARDAR", command=registrar22).place(x=150,y=385)


def abrirVentana23():
                     ventana23 = Toplevel(v0)
                     ventana23.geometry("600x600+0+0")
                     titulo23 = Label(ventana23, text="OPCION GPIO23")
                     label = Label(ventana23, text="SE ENCUENTRA EN GPIO-23",font=formato).place(x=165, y=10)
                     global horaInicial
                     global minInicial
                     global horaFinal
                     global minFinal  
                     
                     def lecturaOn ():
                                      os.system('sudo /./home/fcarmona/lectura23on.sh > /home/fcarmona/gpio23.txt')
                                      pf=open("/home/fcarmona/gpio23.txt","r")
                                      for linea in pf:
                                                      campo=linea.split("\n")
                                                      campof=campo[0]
                                                      if (campof=="1"):
                                                                       
                                                                       imagenOn=Button(ventana23,image=img_on).place(x=320, y=102)
                                                                       text1= tkFont.Font(family="Arial",size ="20")
                                                                       label1 = Label(ventana23,text="1",font=text1).place(x=300,y=50)
                                                                       ventana23.after(1000,lecturaOn)
                                                      if (campof=="0"):
                                                                       text1= tkFont.Font(family="Arial",size ="20")
                                                                       imagenOn=Button(ventana23,image=img_off).place(x=320, y=102)
                                                                       label1 = Label(ventana23,text="0",font=text1).place(x=300,y=50)
                                                                       ventana23.after(1000,lecturaOn)
                     lecturaOn()

                     def on():
                              os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/on23.sh"')

                     def off():
                               os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/off23.sh"')

                     def salida():
                                  ventana23.destroy()
                                  ventana23.update()
                     
                                
                     btn_on23 = Button(ventana23,text="ENCENDER                         ", command=on).place(x=50, y=50)
                     btn_off23 = Button(ventana23,text="APAGAR                             ", command=off).place(x=50, y=110)
                     btn_retorno = Button(ventana23, text="RETORNO MENU PRINCIPAL", command=salida).place(x=50, y=180)

                     minInicial=StringVar()
                     horaInicial=StringVar()
                     minFinal=StringVar()
                     horaFinal=StringVar()

                     label_horaInicial =Label(ventana23, text="Hora Inicial").place(x=10,y=250)
                     txt_horaInicial = Entry(ventana23, textvariable=horaInicial, width=20).place(x=130, y=250)

                     label_minInicial =Label(ventana23, text="Minuto Inicial").place(x=10,y=280)
                     txt_minInicial = Entry(ventana23, textvariable=minInicial, width=20).place(x=130, y=280)

                     label_horaFinal =Label(ventana23, text="Hora Final").place(x=10,y=310)
                     txt_horaFinal = Entry(ventana23, textvariable=horaFinal, width=20).place(x=130, y=310)

                     label_minFinal =Label(ventana23, text="Minuto Final").place(x=10,y=340)
                     txt_minFinal = Entry(ventana23, textvariable=minFinal, width=20).place(x=130, y=340)
                     
                     btn_guardar=Button(ventana23,text="GUARDAR", command=registrar23).place(x=150,y=385)

                     

             

#Botones

btn_gpio17 = Button(v0,text="OPCION GPIO-21      ", command=abrirVentana21).place(x=50, y=50)

btn_gpio27 = Button(v0,text="OPCION GPIO-22      ", command=abrirVentana22).place(x=50, y=120)

btn_gpio21 = Button(v0,text="OPCION GPIO-23      ", command=abrirVentana23).place(x=50, y=190)

btn_salida = Button(v0,text="SALIDA                    ", command=salida).place(x=50, y=260)




v0.mainloop()
