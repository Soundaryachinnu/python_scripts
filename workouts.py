import json
import urllib2
import arithmetic
import os
import datetime
import MySQLdb

class ValueTooSmallError():
	"""Raised when the file size is too large"""
	pass

print "\n List of Tasks \n 1. Second Greatest No \n 2. File operations \n 3. Reading JSON file \n 4. Arithmetic Operations \n 5. DB Actions\n";
task  = raw_input("Enter the task to be executed : ");

#To find the second greatest number from the given string
if task == '1':
	def secondgreatest():
		lst 	= 	raw_input('Enter your list: ')
		lst 	= 	eval(lst)
		firstMaxStr 	= 	max(lst);
		lst.remove(firstMaxStr);
		secondMaxStr 	=	max(lst);
		print "\n Second Greatest Number from the given List : ", secondMaxStr, "\n";

	secondgreatest(); #function call to find the 2nd greatest no.

#To read the input file and do the file operations
elif task == '2':	
	filename		=	'toberead.txt';
	outfile			=	'output.txt';
	filesize 		= 	os.path.getsize(filename);
	inputfileSize 	= 	float(filesize) / (1024*1024);	

	try:
		if inputfileSize > 1:		
			raise ValueTooSmallError;
		else:
			writefile			=	open(outfile, "w");
			inputFileCont		= 	"Size of the Input File : %.2f" % inputfileSize + ' MB \n';		
			appendfileContent 	= 	open(outfile,'a');
			writefile.write(inputFileCont);		
	 		writefile.close();

	 		appendfile 			= 	open(outfile,'a');
			currenttime 		= 	datetime.datetime.now();	
			appendfile.write(str(currenttime))
			appendfile.close();
			print inputFileCont , currenttime;

	#Handling the exception
	except ValueTooSmallError: 
	 	print "oops!!..File size is greater than 1MB";

#To parse the json file and filter the nodes
elif task == '3':
	print "Reading the file. Please wait....................";

	jout 		= 	urllib2.urlopen('https://api.github.com/users/mralexgray/repos');
	json_input 	= 	json.load(jout);
	print " List of Names : ";
	for jlst in json_input:		
		if jlst['fork']==False:
			print ' '+jlst['name']

#To perform the basic arithmetic operations
elif task == '4':
	arg1 	= 	raw_input('Enter the First number  : ');
	arg2 	= 	raw_input('Enter the Second number : ');
	obj 	= 	arithmetic.mathfunc(arg1,arg2);	
	obj.funcadd();  
	obj.funcsub();
	obj.funcmultiply();
	obj.funcdivide();

#To manipulate the DB operations
elif task == '5':
	db 		= 	MySQLdb.connect("localhost","root","password","pythondb");
	cursor 	= 	db.cursor()

	print " Please select the action to be performed : \n 1. List \n 2. Insert \n 3. Update \n 4. Delete \n";
	getActionType = raw_input("Select the Option :");

	if getActionType == '1':
		cursor.execute("SELECT Id,title,author,published_date FROM books");
		results = cursor.fetchall();
		cnt 	= cursor.rowcount;
		print "*******************************************************************";
		if cnt > 0 :
			for row in results:
				id 		= 	row[0];
				title 	= 	row[1];
				author 	= 	row[2];
				pdate 	= 	row[3];

				print "Id : %s,Title : %s, Autor : %s, Published Date : %s " % \
						(id, title,author,pdate)						
		else:
			print 'No Data Found';
		print "*******************************************************************";
	elif getActionType == '2':	

		argtitle		=	raw_input("Enter the Book Title : ");
		argauthor		=	raw_input("Enter the Author Name : ");
		insqry 			= 	"INSERT INTO books(title,author) VALUES ('%s','%s')" % (argtitle,argauthor);

		try : 
			cursor.execute(insqry);	
			db.commit();
			print "Inserted Successfully";
		except :
			print "Something went Wrong. Try Again !!!";
		
	elif getActionType == '3':

		argid		=	raw_input("Enter the Id to be updated : ");
		argtitle	=	raw_input("Enter the Book Title : ");
		argauthor 	=  	raw_input("Enter the Author Name : ");	
		updqry		=	"UPDATE books SET title = '%s',author = '%s' WHERE Id = %s" % (argtitle,argauthor,argid);		
		
		try : 
			cursor.execute(updqry);	
			db.commit();
			print "Updated Successfully";
		except :
			print "Something went Wrong. Try Again !!!";

	elif getActionType == '4':
		argid		=	raw_input("Enter the Id to be deleted : ");
		delqry		=	"DELETE FROM books WHERE Id = %s" % (argid);

		try : 
			cursor.execute(delqry);	
			db.commit();
			print "Deleted Successfully";
		except :
			print "Something went Wrong. Try Again !!!";

	else:
		print "Invalid option chosen";

	db.close();

else :
	print "Oops!!! Please select the correct option...";
