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
	page_html=open('output.html')
	soup=BeautifulSoup(page_html)
	soup.prettify()
	fl = codecs.open('output.csv', 'ab',encoding="Utf-8")
	record=[texts.text for texts in soup.findAll("td",{"align":"center"})]
	print record
	for x in soup.findAll("td"):
		if x.parent.name=="tr":
			lol=x.text
	for x in record:
		if "P" in x: record.remove("P")
		elif "F" in x: record.remove("F")
		elif "A" in x: record.remove("A")
	del record[0:4]
	print record
	fl.write(usn)
	for x in record:
		fl.write(x)
		fl.write(",")
	fl.write(lol)
	fl.close()
	
def parsehtml():
	records=[]
	files=glob.glob("results/*.*")
	for f in files:
		page_html=open(f)
		soup=BeautifulSoup(page_html)
		all_tds = [td for td in soup.findAll("td", width="513")]
		fl = open(usnl[x]+".html", 'wb')
		lol=all_tds[0]
		record = '%s' % (lol)
		fl.write(record)
		fl.close()
		x=x+1
		
def ret():
	import requests
	branches=["cs","ec","me","is","bt","te"]
	print "enter the year:"
	year=raw_input()
	for branch in branches:
		for rno in range(1,120):
			usn="4pa"+year+branch+"%3d"%rno
			payload={'rid':usn,'submit':'submit'}
			r=requests.post("http://results.vtu.ac.in/vitavi.php/post",data=payload)
			fl=open("results/"+usn+".html","wb")
			fl.write(r.text)
			fl.close()
			usnl.add(usn)
			

def main():
	ret()
	parsehtml()
	getval()
	return 0

if __name__ == '__main__':
	usn=""
	usnl=[]
	x=0
	from bs4 import BeautifulSoup
	import re
	inputIndex()
	main()

