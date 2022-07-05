from tkinter import *
import speedtest
import matplotlib.pyplot as plt
root=Tk()
root.title("Internet speed test")
root.geometry("800x800")
root.configure(bg="green")
label_internet=Label(root,text="Internet Speed Test",font=("Arial Greek",50,"italic"),fg="white",bg="green")
label_internet.place(relx=0.5,rely=0.2,anchor=CENTER)
label_download_speed=Label(root,text="Download Speed",font=("Cambria Math",20,"bold"),fg="white",bg="green")
label_download_speed.place(relx=0.25,rely=0.5,anchor=CENTER)
label_upload_speed=Label(root,text="Upload Speed",font=("Cambria Math",20,"bold"),fg="white",bg="green")
label_upload_speed.place(relx=0.75,rely=0.5,anchor=CENTER)

label_up=Label(root)
label_up.place(relx=0.75,rely=0.7,anchor=CENTER)
label_down=Label(root)
label_down.place(relx=0.25,rely=0.7,anchor=CENTER)


def speedcheck():
    st=speedtest.Speedtest()
    download_speed=round(st.download()/1000000,2)
    upload_speed=round(st.upload()/1000000,2)
    label_up['text']=str(upload_speed)+"mbps"
    label_down['text']=str(download_speed)+"mbps"
    






btn1=Button(root,text="Start Test",relief=FLAT,bg="white",fg="black",command=speedcheck)
btn1.place(relx=0.5,rely=0.3,anchor=CENTER)
root.mainloop()

