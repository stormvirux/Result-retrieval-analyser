#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2014 Thaha Muhammed <storm@storm-lappy>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 
def inputIndex():
	import codecs
	x=0
	fl = codecs.open('output.csv', 'wb',encoding="Utf-8")
	fl.write("usn,")
	while x<8:
		fl.write("External,Internal,Total,")
		x+=1
	fl.write("Main Total\n")
	fl.close()

def getval():
	from bs4 import BeautifulSoup
	import codecs
	lol=[]
	record=[]
	x=0
	while x<len(usnl):
		page_html=open("results/"+usnl[x]+".html", 'rb')
		soup=BeautifulSoup(page_html)
		soup.prettify()
		fl = codecs.open('output.csv', 'ab',encoding="Utf-8")
		record=[texts.text for texts in soup.findAll("td",{"align":"center"})]
		for y in soup.findAll("td"):
			if y.parent.name=="tr":
				lol=y.text
		for y in record:
			if "P" in y: record.remove("P")
			elif "F" in y: record.remove("F")
			elif "A" in y: record.remove("A")
		del record[0:4]
		fl.write("\n"+usnl[x]+",")
		if record:
			for y in record:
				fl.write(y)
				fl.write(",")	
			fl.write(lol)
			fl.close()
		x+=1
	
def parsehtml():
	records=[]
	files=glob.glob("results/*.*")
	x=0
	for f in files:
		page_html=open(f)
		soup=BeautifulSoup(page_html)
		all_tds = [td for td in soup.findAll("td", width="513")]
		fl = open("results/"+usnl[x]+".html", 'wb')
		lol=all_tds[0]
		record = '%s' % (lol)
		if record:
			fl.write(record)
		fl.close()
		x=x+1
		
def ret():
	import requests
	x=0
	branches=["cs"]
	print "enter the year:"
	year=raw_input()
	for branch in branches:
		for rno in range(1,11):
			usn="4pa"+year+branch+"%03d"%rno
			payload={'rid':usn,'submit':'submit'}
			r=requests.post("http://results.vtu.ac.in/vitavi.php/post",data=payload)
			fl=open("results/"+usn+".html","wb")
			fl.write(r.text)
			fl.close()
			usnl.append(usn)
			

def main():
	inputIndex()
	ret()
	parsehtml()
	getval()
	return 0

if __name__ == '__main__':
	usn=""
	usnl=[]
	from bs4 import BeautifulSoup
	import re
	import glob
	import os
	inputIndex()
	main()

