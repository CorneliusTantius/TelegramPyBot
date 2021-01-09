import requests
import json
import os

def fetch_data(uname, upwd):
	loginurl = '' # binusmaya MyClass API URL
	payload = {
            'Username':uname,
            'Password':upwd
            }

	with requests.session() as s:
		getLoginSession = s.post(loginurl, data=payload)
		loginResult = json.loads(getLoginSession.text);
		if loginResult['Status'] == False:
			retVal = str(loginResult['Message'])
		else:
			retVal = GetViconList(s)
	return retVal

def GetViconList(CurrentSession):
	viconUrl = 'https://myclass.apps.binus.ac.id/Home/GetViconSchedule'
	print("> Getting video conference list...")
	viconlist = CurrentSession.get(viconUrl)
	viconResult = json.loads(viconlist.text)
	retval = []
	retStr = '== Your viconlist =='
	for item in viconResult:
	    if(str(item['MeetingId']) != '-'):
	        retval.append({
	        	'date':str(item['DisplayStartDate']),
		        'start time':str(item['StartTime']),
		        'desc':str(item['SsrComponentDescription']),
		        'class':str(item['ClassCode']),
		        'course':str(item['CourseTitleEn']),
		        'zoom url':str(item['MeetingUrl']),
		        'meetingID':str(item['MeetingId']),
		        'meetingPW':str(item['MeetingPassword'])
	        	})
	        retStr += (
	        	'\n================='
	        	'\ndate: '+str(item['DisplayStartDate'])+
	        	'\nstart time: '+str(item['StartTime'])+
		        '\ndesc: '+str(item['SsrComponentDescription'])+
		        '\nclass: '+str(item['ClassCode'])+
		        '\ncourse: '+str(item['CourseTitleEn'])+
		        '\nzoom url: '+str(item['MeetingUrl'])+
		        '\nmeetingID: '+str(item['MeetingId'])+
		        '\nmeetingPW: '+str(item['MeetingPassword'])+'\n')
	return retStr