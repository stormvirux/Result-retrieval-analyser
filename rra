def marks():
	fl = open('output.csv', 'rb')
	string=fl.read()
	fl.close
	str1=re.sub(r"Semester:,.*,Result:  [FS].* CLASS(,|.*,)","",string)
	str2=re.sub(r"P,","",str1)
	usn=re.findall(r"4pa\d\dcs\d\d\d",string)
	u=usn[0]
	string=re.sub(r"\(4pa\d\d(cs|ec|me|te|bt|is)\d\d\d\)","",str2)
	str2=re.sub(r"[a-zA-Z&]*","",string)
	string=re.sub(r",,","",str2)
	str2=re.sub(r"\(\d\d\d\d\),","",string)
	string=re.sub(r"  ","",str2)
	str2=re.sub(r" :,","",string)
	fl = open('out.csv', 'ab')
	string=re.sub(r" . ","",str2)
	marks=re.sub(r"-","",string)
	m=re.sub(r":,\d,:","",marks)
	marks=re.sub(r"(^,|,$)","",m)
	fl.write(u+",")
	fl.write(marks)
	fl.close

def sub():
	fl = open('output.csv', 'rb')
	string=fl.read()
	fl.close
	str1=re.sub(r"Semester:,5,Result:  [FS].* CLASS,","",string)
	str2=re.sub(r"P,","",str1)
	string=re.sub(r"\(4pa\d\d(cs|ec|me|te|bt|is)\d\d\d\)","",str2)
	str2=re.sub(r"[0-9]*","",string) #remove all numbers
	string=re.sub(r"^[A-Z]* [A-Z]* ,","",str2)
	str2=re.sub(r",,","",string)
	string=re.sub(r"\([A-Z]*\)",",",str2)
	usn=re.findall(r"4pa\d\dcs\d\d\d",string)
	str2=re.sub(r":","",string)
	string=re.sub(r"Total Marks,","",str2)
	fl = open('out.csv', 'wb')
	marks=re.sub(r"-","",string)
	string=re.sub(r"Subject,External,Internal,Total,Result,","",marks)
	string = string.split(',')
	print string
	stri = ''
	for each in range(1,len(string)):
			stri += 'External,Internal,Total' + ','
	stri= stri.strip(',')
	fl.write("usn,")
	fl.write(stri)
	fl.write(",Main Total")
	fl.write("\n")
	fl.close

def getincsv():
	sub()
	marks()


def getval():
	import codecs
	x=0
	records=[]
	all_tds=[]
	page_html=open('output.html')
	soup=BeautifulSoup(page_html)
	soup.prettify()
	fl = codecs.open('output.csv', 'wb',encoding="Utf-8")
	for string in soup.stripped_strings:
		fl.write(string)
		fl.write(",")
	fl.close()
	
def parsehtml():
	records=[]
	page_html=open('1.html')
	soup=BeautifulSoup(page_html)
	all_tds = [td for td in soup.findAll("td", width="513")]
	fl = open('output.html', 'wb')
	lol=all_tds[0]
	record = '%s' % (lol)
	fl.write(record)
	fl.close()
	
	
def ret():
	import requests
	print "enter the year:"
	year=raw_input()
	print "enter the role number:"
	rno=raw_input()
	print "enter the branch"
	br=raw_input()
	usn="4pa"+year+br+rno
	payload={'rid':usn,'submit':'submit'}
	r=requests.post("http://results.vtu.ac.in/vitavi.php/post",data=payload)


def main():
	ret()
	parsehtml()
	getval()
	getincsv()
	return 0

if __name__ == '__main__':
	from bs4 import BeautifulSoup
	import re
	main()

