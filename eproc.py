import pickle
import os.path


continue_running = True


account = dict()
current_loggedin_account = ""
list_of_job = []


class persistanceDB:
	def __init__(self):
		self.account = dict()
		self.job = []

	def setup(self,acc,job):
		self.account = acc
		self.job = job


class JobOffering :
	def __init__(self,creator,title):
		self.creator = creator
		self.title = title
		self.participants = []
		self.winner = ""
	def printDetail(self):
		print self.title
		print "Instantion : " + self.creator
	def join(self,person):
		self.participants.append(person)
	def printParticipants(self):
		print "yeah"
		i = 0
		for x in self.participants:
			print str(i) + " - "+ x
			i += 1
	def setWinner(self,idwinner):
		self.winner = self.participants[idwinner]
	def isOpen(self):
		return (self.winner == "")




pdb = persistanceDB()


def autosave():
	f= open("db","w+")
	pdb.setup(account,list_of_job)
	pickle.dump(pdb,f)
	print "Autosave success"

## Autoload DB from File
if os.path.isfile("db"):
	f = open("db","rb")
	pdb = pickle.load(f)
	account = pdb.account
	list_of_job = pdb.job


print account
#print list_of_job
while continue_running:
	terminal_string = current_loggedin_account +"@eprocd >"
	query = raw_input(terminal_string)
	splitted_query = query.split()
	query_command = splitted_query[0]
	if query_command == "version":
		print "Eproc Daemon v1.4.1"
		print "Copyright (c) 2018 - reitnorF Technologies"
	elif query_command == "q":
		print "Exiting eprocd..."
		continue_running = False
	elif query_command == "reg":
		if (len(splitted_query) != 3):
			print "Invalid query"
			print "Usage : reg <<username>> <<password>>"
		else:
			account[splitted_query[1]] = splitted_query[2]
			autosave()
			print "Account " + splitted_query[1] + " successfully created!"
	
	elif query_command == "login":
		if (len(splitted_query) != 3):
			print "Invalid query"
			print "Usage : reg <<username>> <<password>>"
		else:
			if (account[splitted_query[1]] == splitted_query[2]):
				current_loggedin_account = splitted_query[1]
				print "Account " + splitted_query[1] + " successfully logged in!"
			else:
				print "Incorrect username/password"
	
	elif query_command == "logout":
		current_loggedin_account = ""
		print "Logged Out successfully.. "

	elif query_command ==  "create":
		if (len(splitted_query) != 2):
			print "Invalid query"
			print "Usage : create <<title>> "
		else:
			joboffering = JobOffering(current_loggedin_account,splitted_query[1])
			list_of_job.append(joboffering)	
			autosave()		
			print "Job " + splitted_query[1] + " is successfully posted"
	
	elif query_command == "list":
		i = 0
		for x in list_of_job:
			if x.isOpen():
				print str(i) +" - "+ x.title
			i += 1

	elif query_command == "closedlist":
		i = 0
		for x in list_of_job:
			if not x.isOpen():
				print str(i) +" - "+ x.title
			i += 1



	elif query_command == "mylist":
		i = 0
		for x in list_of_job:
			if x.creator == current_loggedin_account:
				print str(i) +" - "+ x.title
			i += 1



	elif query_command == "getdetail":
		if (len(splitted_query) != 2):
			print "Invalid query"
			print "Usage : getdetail <<id_job_offering>> "
		else:
			id_job = int(splitted_query[1])
			list_of_job[id_job].printDetail()
			if list_of_job[id_job].creator == current_loggedin_account:
				list_of_job[id_job].printParticipants()
			if not list_of_job[id_job].isOpen():
				print "Won by " + list_of_job[id_job].winner

	elif query_command == "win":
		if (len(splitted_query) != 3):
			print "Invalid query"
			print "Usage : win <<id_job_offering>> <<id_participant>> "
		else:
			id_job = int(splitted_query[1])
			id_winner = int(splitted_query[2])
			list_of_job[id_job].setWinner(id_winner)
			autosave()
			print "User " + list_of_job[id_job].winner + " win this tender!"

	elif query_command == "join":
		if (len(splitted_query) != 2):
			print "Invalid query"
			print "Usage : getdetail <<id_job_offering>> "
		else:
			id_job = int(splitted_query[1])
			list_of_job[id_job].join(current_loggedin_account)
			autosave()
			print current_loggedin_account + "successfully placed bid on " + list_of_job[id_job].title

	else:
		print "Incorrect query"