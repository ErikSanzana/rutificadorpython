from tkinter import Entry,Button,Label,Tk,Text,StringVar
import requests
import webbrowser
import json
ventana=Tk()
ventana.title("RUTIFICADOR")
def borrar ():
    mensajeTxt.delete(1.0 ,"end-1c")
def enviarDatos():
    mensaje=mensajeTxt.get(1.0 ,"end-1c")

    re_rut=eval(mensaje)
    resultado="?rut="+str(re_rut)
    print(resultado)
    base ="https://api.libreapi.cl/rut/activities"
    url=base+resultado
    response=requests.get(url)
    data=response.json()
    pretty=json.dumps(data, indent=4)
    mensajeTxt.delete(1.0 ,"end-1c")
    mensajeTxt.insert(1.0,pretty)

Label(text="ingrese el rut sin guion ni punto",fg="gray",font=("Verdana",12)).grid(row=0,column=0,sticky="e",padx=20,pady=5)


mensajeTxt=Text(ventana,width=80,height=15,background="black",foreground="green")
mensajeTxt.grid(row=1,column=0)

botonEnviar=Button(ventana,text="BUSCAR RUT",fg="black",font=("Verdana",14),command=enviarDatos)
botonEnviar.grid(row=7,column=0,padx=20,pady=20)

botonBorrar=Button(ventana,text="BORRAR",fg="black",font=("Verdana",14),command=borrar)
botonBorrar.grid(row=8,column=0,padx=20,pady=20)

ventana.mainloop()