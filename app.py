from Tkinter import *
import requests
from BeautifulSoup import BeautifulSoup
# create the root window
data = {};
def getdata(event):
	#print(event['handle'].get())
	#data['rank']=event['field'].get()
	data['solved']=scrapping(event)
	print(data['solved'])
	makeEntry(data,text)	
	#url = "https://www.codechef.com/users/"+str(user['Handle'].get())
def scrapping(user):
	url="https://www.codechef.com/users/"+str(user['handle'].get())
	print(url)
	try:
		response = requests.get(url)
	except:
		print("connectivity error")
		exit(0)
	html = response.content
	soup=BeautifulSoup(html)
	table = soup.find('section',attrs={'class':'rating-data-section problems-solved'}).find('div',attrs={'class':'content'}).find('h5')
	s="";
	s=s+table.text[14]
	i=15
	while(table.text[i]!=')'):
	    s=s+table.text[i]
	    i=i+1
	            
	print(s)
	return s
	
    


def makeform(root):
   entries = {}
   ent = Entry(root)
   ent.insert(0,"0")
   ent.pack(side=RIGHT, expand=YES, fill=X)
   entries['handle'] = ent
   ent.place(x=10,y=30)
   return entries
def makeEntry(data,text):
	text.delete(1.0,END)
	text.insert(INSERT,"Questions solved:-"+data['solved'])


root = Tk()

# modify the window
root.title("Create a window")
root.geometry("500x500")

frame = Frame(root,bg="black",height="100",width="500")
frame.pack(side=TOP)
frame.place(x=0,y=0)
#handle = Entry(frame,bg="green",width="40")
#handle.pack(expand=YES, fill=X)
#handle.place(x=10,y=30)
#handles['abc']=handle
#print(str(handles['abc'].get()));
ents=makeform(root)
button = Button(frame,text="Explore",command=(lambda e=ents:getdata(e)))
#print(data)
button.pack();
button.place(x=10,y=60)

text = Text(root,width="60")
text.insert(INSERT, "Welcome to codehcef tool.Just enter the codechef handle\nand we are providing you all the data related to that\nhandle:-\n\n")

text.pack()
text.place(x=10,y=110)


# Start the window's event-loop
root.mainloop()


