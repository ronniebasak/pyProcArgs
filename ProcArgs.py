#! /usr/bin/env python

#This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License.
#To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/.

import string, types

class ProcArgs():
	def __init__(self):
		"""  This is the argument processing class"""
		import sys
		self._args=sys.argv
		self.count=len(self._args)

		self.args={}
		self.long_args={}
		self.lone_args=None
		self.lone_long_args=None
		self.unproc_args=None
		
		self.tot_args=0
		self.n_args=0
		self.n_long_args=0
		self.n_lone_args=0
		self.n_lone_long_args=0
		self.n_unproc_args=0
		
		
	def has_args(self):
		""" It checks whether any arguments are available for processing """
		
		if self.count == 1:
			return False
		elif self.count > 1:
			return self.count-1
			
	def process_args(self):
		""" This processes the arguments and returns the dictionary
		If a argument starts with -, it is labeled as a key value pair
		and if it has --, it can be a unique descriptor and can have multiple values """

		
		if self.has_args():
			keys=[]	#control to hold the keys
			ikeys=[] #control to hold iKeys
		
			vals=[] #control to hold values to keys
			ivals=[] #control to hold values to iKeys
		
			ukeys=[] #control to add alone keys, like -h
			iukeys=[] #control to add alone iKeys, like --help
		
			uargs=[] #control to add unhandled keys

			i=1
			while i<self.count:
				# At first checking if the argument starts with --
				if self._args[i][:2]=="--":
					ikeys.append(self._args[i][2:])  					#Appending it to ikeys, assumed
					
					if self.count>i+1 and self._args[i+1][0] != "-":    # checking if there exists a next argument (the count var has one more argument) and if next arg is not parsable through parser, then its assumed to be a value
						ivals.append(self._args[i+1])  					#appending to values, and incrementing pointer to avoid coflict
						i+=1
					
					else:												#Otherwise, it is a lone argument and appending to iukeys, and removing from ikeys
						ikeys.pop()
						iukeys.append(self._args[i][2:])
					
				#Then checking if the argument starts with -
				elif self._args[i][0]=="-":
					keys.append(self._args[i][1:])
				
					if self.count>i+1 and self._args[i+1][0] != "-":
						vals.append(self._args[i+1])
						i+=1
					
					else:
						keys.pop()		#remove the item appended to keys list and add to lone args list
						ukeys.append(self._args[i][1:])
					
				
					
				else:													#If the argument is not parsable at all, it is returned as-is to be handled by the author of the program
					uargs.append(self._args[i])
				
				i+=1
			
			self.__makeDict(keys, vals, self.args)
			self.__makeDict(ikeys, ivals, self.long_args)
			self.lone_args=ukeys
			self.lone_long_args=iukeys
			self.unproc_args=uargs
			
			self.n_args=len(self.args)
			self.n_long_args=len(self.long_args)
			self.n_lone_args=len(self.lone_args)
			self.n_lone_long_args=len(self.lone_long_args)
			self.n_unproc_args=len(self.unproc_args)
			return True
			
		else:
			return False
			
			
	def __makeDict(self, keys, vals, target):
		"""It is a function for making a dictionary with 2 arrays of same length"""
		if len(keys)==len(vals) and (type(target) is types.DictType):
			
			for i in range(len(keys)):
				target[keys[i]]=vals[i]
				
	
			
			
if __name__=="__main__":
	a=ProcArgs()
	if a.has_args():
		print "It has "+str(a.has_args())+" args"
		a.process_args()
		
		if a.args:
			print "\nArgument Value Pairs:"
			for i in a.args.keys():
				print "  ",i," : ", a.args[i]
		
		if a.long_args:	
			print "\nLong Argument Value pairs:"
			for i in a.long_args.keys():
				print "  ",i, " : ", a.long_args[i]
	
		if a.unproc_args:
			print "\nUnparsed/Unprocessed Args:"
			for i in a.unproc_args:
				print "  ",i
			
		if a.lone_args:
			print "\nLone/Isolated/Flag Args:"
			for i in a.lone_args:
				print "  ",i
		
		if a.lone_long_args:	
			print "\nLong Lone/Isolated/Flag Args:"
			for i in a.lone_long_args:
				print "  ",i
		
	else:
		print "It has no args to process"
	raw_input("\n\nPress Enter to Continue ")
