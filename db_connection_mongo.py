#-------------------------------------------------------------------------
# AUTHOR: Carlos Castrillo
# FILENAME: db_connection_mongo.py
# SPECIFICATION: Definitions of the functions for MongoDB
# FOR: CS 4250- Assignment #2
# TIME SPENT: 1 hour
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with
# standard arrays

#importing some Python libraries
# --> add your Python code here
import pymongo as pm

def connectDataBase():

    # Create a database connection object using pymongo
    # --> add your Python code here
	return pm.MongoClient()

def createDocument(col, docId, docText, docTitle, docDate, docCat):

    # create a dictionary (document) to count how many times each term appears in the document.
    # Use space " " as the delimiter character for terms and remember to lowercase them.
    # --> add your Python code here
	terms = docText.split(" ")
	document = {}
	for i in terms:
		count = terms.count(i)
		document.update({i: count})

    # create a list of dictionaries (documents) with each entry including a term, its occurrences, and its num_chars. Ex: [{term, count, num_char}]
    # --> add your Python code here
	collection = []
	for i in document:
		collection.append({i, document[i], len(i)})

    #Producing a final document as a dictionary including all the required fields
    # --> add your Python code here
	docFinal = {"_id:" : docId, "text" : docText, "title" : docTitle, "date" : docDate, "category" : docCat, "terms" : collection}

    # Insert the document
    # --> add your Python code here
	col.insertOne(docFinal)

def deleteDocument(col, docId):

    # Delete the document from the database
    # --> add your Python code here
	col.deleteOne(docId)
	
def updateDocument(col, docId, docText, docTitle, docDate, docCat):

    # Delete the document
    # --> add your Python code here
    deleteDocument(col, docId)
    # Create the document with the same id
    # --> add your Python code here
    createDocument(col, docId, docText, docTitle, docDate, docCat)

def getIndex(col):

    # Query the database to return the documents where each term occurs with their corresponding count. Output example:
    # {'baseball':'Exercise:1','summer':'Exercise:1,California:1,Arizona:1','months':'Exercise:1,Discovery:3', ...}
    # We are simulating an inverted index here in memory.
    # --> add your Python code here
	return -1