#!/usr/bin/env python
# coding: utf-8

# In[38]:


from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user = 'aacuser', passwrd = 'infiniteMemory1!'):
        # Initializing the MongoClient.  This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        # 
        USER = user
        PASS = passwrd
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32659
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
            
    def create(self, data) ->bool:
        """ push a dictionary-type object to the AAC.animals database """
        if data is not None:
            self.database.animals.insert_one(data) # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False
                    
    def read(self, data_filter) ->list:
        """ return all documents that match a given filter """
        result = list()
        result = list(self.database.animals.find(data_filter)) # convert the search result into a list
        return result # return either the search results or an empty list otherwise
            
    def update(self, data_filter, new_data) ->int:
        """ modify the value of any documents matching the data_filter with the new data and return the number of documents modified"""
        num_updates = 0
        if (data_filter is None) or (new_data is None): #escape the function if nothing is specified
            return num_updates
        else:
            results = self.database.animals.update_many(data_filter, new_data) #update the results
            num_updates = results.modified_count #get the number of documents modified
                
        return num_updates
        
    def delete(self, data_filter) ->int:
        """ deletes any object matching the input key/value pair and return the number of objects deleted"""
        num_deletions = 0
        if data_filter is None:
            return num_deletions
        else:
            results = self.database.animals.delete_many(data_filter)
            num_deletions = results.deleted_count
        return num_deletions
        

