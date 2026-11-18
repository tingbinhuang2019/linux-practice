import subprocess

phone = "0123-546-346"
email = "Office@email.com"
path  = ""

def create_folder_file(path, title):
	path = "./" + path
	print(path)
	mkdir_com = "mkdir " + path
	subprocess.run(mkdir_com, shell=True)

	title_com = "touch " + path + "/" + title
	subprocess.run(title_com, shell=True)

	phone_command = "echo " + phone + " > " + path + "/Cell"
	subprocess.run(phone_command,shell=True)

	email_command = "echo " + email + " > " + path + "/Email"
	subprocess.run(email_command,shell=True)	
	
employees = {
	"THOMAS_EDISON": ["CEO", path, "Chief_Executive_Officer", phone, email],
	"MARIE_CURIE"  : ["THOMAS_EDISON", path, "Chief_Operating_Office", phone, email],
	"ISAAC_NEWTON" : ["MARIE_CURIE", path, "Manager", phone, email],
	"LOUIS_PASTEUR": ["ISAAC_NEWTON",path, "Employee",phone, email],
	
	"NIKOLA_TESLA" : ["THOMAS_EDISON", path, "Manager", phone, email],
	"ADA_LOVELACE" : ["NIKOLA_TESLA",  path, "Employee", phone, email],
	
	"BLAISE_PASCAL": ["THOMAS_EDISON", path, "Chief_Financial_Officer",phone, email],
	"ALEXANDER_BELL":["BLAISE_PASCAL", path, "Manager", phone, email],
	"CARL_GAUSS"   : ["ALEXANDER_BELL",path, "Employees",phone,email]
	} 

for k, v in employees.items():
	new_path = ""
	if v[0] == "CEO":
		v[1] += k + "/"
	else: 
		v[1] += employees[v[0]][1] + k + "/"
	new_path += v[1]
	create_folder_file(new_path, employees[k][2])

		
