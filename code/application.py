#-------------Heres some ideas for queries-------------------#



# - At least two queries that select at least some data from both of your datasets

#*****Toxins*****
# Select the toxins levels per country
# Select the amount of a specific toxin in all counties

#*****Cancers*****
# Select the data from each type of cancer


# - At least two queries that showcase syntax beyond the basic `SELECT-FROM-WHERE` clauses (e.g., Grouping, Subqueries, etc.)

#*****Toxins*****
# Join Cancer on county

#*****Cancers*****
# Select the data with cases over a certain threshold


# - At least two queries that accept input entered by the user (as opposed to just allowing selection from a list of options)

#*****Toxins*****
# Select the amount of toxins for a specific county

#*****Cancers*****
# Select the data for a specific county
# select data for a specific type

import os
from texttable import Texttable
from database import DatabaseController

def ttDemo(tt):
	tt.set_cols_align(["l", "c", "r"])
	# First array column is a header
	tt.add_rows([["Left", "Number", "Right"], ["Value", "10", "More Value"]])
	print(tt.draw())


def find_specific_cancer():
	type = input("Type which cancer you want to get data for [Leukemias, Lung and Bronchus, Melanomas of the Skin]: ")
	db.find_specific_cancer(type)

def main():
	# Initialize Imports
	db = DatabaseController()
	tt = Texttable()
	tt.set_deco(Texttable.HEADER)

	ttDemo(tt)

	print("Welcome to our application")
	print("Contributors: Christopher Pence, Howard Zhao, Aidan Duane, Caitlin Crowley")
	print("Please pick from one of these options to query our database:")


	#array of options for queries
	arr = ["1: find specific cancer"]


	for item in arr:
		print(item)


	query = input("Enter the number of the query you would like to run: ")
	query_ = int(query)


	print("You selected",arr[query_-1])

	#run function per user input
	if query_ == 1:
		find_specific_cancer()


if __name__ == "__main__":
	main()