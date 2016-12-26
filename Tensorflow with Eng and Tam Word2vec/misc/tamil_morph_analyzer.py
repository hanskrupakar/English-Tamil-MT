#!/usr/bin/env python
#-*- coding: utf-8 -*- 

import tamil, popen2

isWhat = 0		
SetPrefix = 0		
SetSuffix = 0		

tenseSuffix = [u'க்க்இன்ற்',u'க்இன்ற்',u'க்க்இற்',u'க்இற்',u'இன்',u'த்த்',u'ந்த்',u'ட்ட்',u'ற்ற்',u'த்',u'ட்',u'ற்',u'ப்ப்',u'க்க்',u'ப்',u'க்',u'வ்']
verbSuffix = [u'ஏன்',u'ஆய்',u'ஈர்க்அள்',u'ஆன்',u'அன்',u'ஆள்',u'அள்',u'ஆர்',u'அர்',u'அத்உ',u'உம்',u'ஓம்',u'ஆர்க்அள்',u'உ',u'அ']
nounSuffix = [u'ஐ',u'க்அள்',u'உக்க்உ',u'க்க்உ',u'ஆக்அ',u'ஆல்',u'அல்',u'ஒட்உ',u'உட்அன்',u'உடை',u'இல்',u'கண்',u'இட்அம்',u'இர்உந்த்உ',u'இன்',u'அத்உ']

def processStem(string):
	stemmerPath = "tamil-stemmer-build/snowball-with-tamil/stemwords"
	# This is the path of package Tamil-Stemmer installed in computer.
	fin, fout = popen2.popen2( stemmerPath + " -l ta")
	fout.write(string)
	fout.close()
	toBeReturn = fin.readline()
	fin.close()
	return toBeReturn

def getStem(string):
	for i in (0,2) :
		string = processStem(string)
	string = string.decode('utf8')
	toBeReturn = string.replace('\n','')
	return toBeReturn

def combineMeiUyirString(string) :
	stringList = tamil.utf8.get_letters(string)
	toBeReturn = ''
	for i in stringList :
		toBeReturn += u''.join(tamil.utf8.splitMeiUyir(i))
	return u''.join(toBeReturn)

def suffixRemove(string,toBeReturn) :
	for i in range(0,len(string)) :
		if(string[i] == toBeReturn[0]) :
			del toBeReturn[0]			
		else :
			if(i == 0) :
				global SetPrefix
				SetPrefix = 1
				return u''
			toBeReturn = u''.join(toBeReturn)
			toBeReturn = combineMeiUyirString(toBeReturn)
			toBeReturn = toBeReturn.lstrip(string[i])
			toBeReturn = tamil.utf8.get_letters(toBeReturn)
	return u''.join(toBeReturn)

def prefixRemove(string,toBeReturn) :
	toBeReturnAltered = u''
	for i in range(0,len(toBeReturn)) :
		if(toBeReturn[i] != string[0]) :
			toBeReturnAltered += toBeReturn[i]
		elif(toBeReturn[i] == string[0]) :
			break
	return u''.join(toBeReturnAltered)

def getPrefixSuffix(string1,string2) :
	global SetSuffix
	toBeReturnPrefix = prefixRemove(string1,string2)
	dummy = u''.join(string2)
	dummy = dummy.replace(toBeReturnPrefix,u'')
	SetSuffix = 1
	toBeReturnSuffix = suffixRemove(string1,tamil.utf8.get_letters(dummy))
	toBeReturnSuffix = u''.join(toBeReturnSuffix)
	return (toBeReturnPrefix,toBeReturnSuffix)

def tenseSuffixTagging(string) :
	global isWhat
	dummy = 0
	if(u'க்க்இன்ற்'  in string and dummy == 0) :
		string = string.replace(u'க்க்இன்ற்' ,u'<க்கின்று{PRESENT}>')
		isWhat = 2
		dummy = 1
	elif(u'க்இன்ற்'  in string and dummy == 0) :
		string = string.replace(u'க்இன்ற்' ,u'<கின்று{PRESENT}>')
		isWhat = 2
		dummy = 1
	elif(u'க்க்இற்'  in string and dummy == 0) :
		string = string.replace(u'க்க்இற்' ,u'<க்கிறு{PRESENT}>')
		isWhat = 2
		dummy = 1
	elif(u'க்இற்'  in string and dummy == 0) :
		string = string.replace(u'க்இற்' ,u'<கிறு{PRESENT}>')
		isWhat = 2
		dummy = 1
	elif(u'இன்'  in string and dummy == 0) :
		string = string.replace(u'இன்' ,u'<இன்{PAST}>')
		isWhat = 2
		dummy = 1
	elif(u'த்த்' in string and dummy == 0) :
		string = string.replace(u'த்த்',u'<த்த்{PAST}>')
		isWhat = 2
		dummy = 1
	elif(u'ந்த்' in string and dummy == 0) :
		string = string.replace(u'ந்த்',u'<ந்த்{PAST}>')
		isWhat = 2
		dummy = 1
	elif(u'ட்ட்' in string and dummy == 0) :
		string = string.replace(u'ட்ட்',u'<ட்ட்{PAST}>')
		isWhat = 2
		dummy = 1
	elif(u'ற்ற்' in string and dummy == 0) :
		string = string.replace(u'ற்ற்',u'<ற்ற்{PAST}>')
		isWhat = 2
		dummy = 1
	elif(u'த்' in string and dummy == 0) :
		string = string.replace(u'த்',u'<த்{PAST}>')
		isWhat = 2
		dummy = 1
	elif(u'ட்' in string and dummy == 0) :
		string = string.replace(u'ட்',u'<ட்{PAST}>')
		isWhat = 2
		dummy = 1
	elif(u'ற்' in string and dummy == 0) :
		string = string.replace(u'ற்',u'<ற்{PAST}>')
		isWhat = 2
		dummy = 1
	elif(u'ப்ப்' in string and dummy == 0) :
		string = string.replace(u'ப்ப்',u'<ப்ப்{FUTURE}>')
		isWhat = 2
		dummy = 1
	elif(u'க்க்' in string and dummy == 0) :
		string = string.replace(u'க்க்',u'<க்க்{FUTURE}>')
		isWhat = 2
		dummy = 1
	elif(u'ப்' in string and dummy == 0) :
		string = string.replace(u'ப்',u'<ப்{FUTURE}>')
		isWhat = 2
		dummy = 1
	elif(u'க்' in string and dummy == 0) :
		string = string.replace(u'க்',u'<க்{FUTURE}>')
		isWhat = 2
		dummy = 1
	elif(u'வ்' in string and dummy == 0) :
		string = string.replace(u'வ்',u'<வ்{FUTURE}>')
		isWhat = 2
		dummy = 1
	else :
		None
	return string

def verbSuffixTagging(string) :
	global isWhat
	dummy = 0
	if(u'ஏன்' in string and dummy == 0) :
		string = tenseSuffixTagging(string)
		string = string.replace(u'ஏன்',u'<ஏன்{1S}>')
		isWhat = 2
		dummy = 1
	elif(u'ஓம்' in string and dummy == 0) :
		string = tenseSuffixTagging(string)
		string = string.replace(u'ஓம்',u'<ஓம்{1PL}>')
		isWhat = 2
		dummy = 1
	elif(u'ஆய்' in string and dummy == 0) :
		string = tenseSuffixTagging(string)
		string = string.replace(u'ஆய்',u'<ஆய்{2S}>')
		isWhat = 2
		dummy = 1
	elif(u'ஈர்க்அள்' in string and dummy == 0) :
		string = tenseSuffixTagging(string)
		string = string.replace(u'ஈர்க்அள்',u'<ஈர்கள்{2PL}>')
		isWhat = 2
		dummy = 1
	elif(u'ஆன்' in string and dummy == 0) :
		string = tenseSuffixTagging(string)
		string = string.replace(u'ஆன்',u'<ஆன்{3SM}>')
		isWhat = 2
		dummy = 1
	elif(u'அன்' in string and dummy == 0 and u'அள்' not in string and u'அர்' not in string) :
		string = tenseSuffixTagging(string)
		string = string.replace(u'அன்',u'<அன்{3SM}>')
		isWhat = 2
		dummy = 1
	elif(u'ஆள்' in string and dummy == 0) :
		string = tenseSuffixTagging(string)
		string = string.replace(u'ஆள்',u'<ஆள்{3SF}>')
		isWhat = 2
		dummy = 1
	elif(u'அள்' in string and dummy == 0) :
		string = tenseSuffixTagging(string)
		string = string.replace(u'அள்',u'<அள்{3SF}>')
		isWhat = 2
		dummy = 1
	elif(u'ஆர்' in string and dummy == 0) :
		string = tenseSuffixTagging(string)
		string = string.replace(u'ஆர்',u'<ஆர்{3SMF}>')
		isWhat = 2
		dummy = 1
	elif(u'அர்' in string and dummy == 0) :
		string = tenseSuffixTagging(string)
		string = string.replace(u'அர்',u'<அர்{3SMF}>')
		isWhat = 2
		dummy = 1
	elif(u'அத்உ' in string and dummy == 0) :
		string = tenseSuffixTagging(string)
		string = string.replace(u'அத்உ',u'<அது{3SN}>')
		isWhat = 2
		dummy = 1
	elif(u'உம்' in string and dummy == 0) :
		string = tenseSuffixTagging(string)
		string = string.replace(u'உம்',u'<உம்{3PLN}>')
		isWhat = 2
		dummy = 1
	elif(u'ஆர்க்அள்' in string and dummy == 0) :
		string = tenseSuffixTagging(string)
		string = string.replace(u'ஆர்க்அள்',u'<ஆர்கள்{3PLMF}>')
		isWhat = 2
		dummy = 1
	else :
		None

	if(string[-1] == u'அ') :
		string = tenseSuffixTagging(string)
		string = string.replace(u'அ',u'<அ{3PLN}>')
		isWhat = 2
	if(string[-1] == u'ஆ') :
		string = tenseSuffixTagging(string)
		string = string.replace(u'ஆ',u'<ஆ{}>')
		isWhat = 2
	if(string[-1] == u'உ') :
		string = tenseSuffixTagging(string)
		string = string.replace(u'உ',u'<உ{3SN}>')
		isWhat = 2
	if(u'ஆல்' in string) :
		string = tenseSuffixTagging(string)
		string = string.replace(u'ஆல்',u'<ஆல்{INST}>')
		isWhat = 2
	if(u'அல்' in string) :
		string = tenseSuffixTagging(string)
		string = string.replace(u'அல்',u'<அல்{INST}>')
		isWhat = 2

	return string

def nounSuffixTagging(string) :
	global isWhat
	if(u'இர்உந்த்உ' in string) :
		string = string.replace(u'இர்உந்த்உ',u'<இருந்து{ABL}>')
		isWhat = 1
	if(u'இட்அம்' in string) :
		string = string.replace(u'இட்அம்',u'<இடம்{LOC}>')
		isWhat = 1
	if(u'உட்அன்' in string) :
		string = string.replace(u'உட்அன்',u'<உடன்{SOC}>')
		isWhat = 1
	if(u'உட்ஐ' in string) :
		string = string.replace(u'உட்ஐ',u'<உடை{SOC}>')
		isWhat = 1
	if(u'உக்க்உ' in string) :
		string = string.replace(u'உக்க்உ',u'<உக்கு{DAT}>')
		isWhat = 1
	if(u'க்க்உ' in string) :
		string = string.replace(u'க்க்உ',u'<க்கு{DAT}>')
		isWhat = 1
	if(u'ஒட்உ' in string) :
		string = string.replace(u'ஒட்உ',u'<ஒடு{SOC}>')
		isWhat = 1
	if(u'ஆக்அ' in string) :
		string = string.replace(u'ஆக்அ',u'<ஆக{BEN}>')
		isWhat = 1
	if(u'ஆல்' in string) :
		for i in tenseSuffix :
			if(i in string) :
				isWhat = 2
				break
		if(isWhat != 2)	:
			string = string.replace(u'ஆல்',u'<ஆல்{INST}>')
			isWhat = 1
	if(u'அல்' in string) :
		for i in tenseSuffix :
			if(i in string) :
				isWhat = 2
				break
		if(isWhat != 2)	:
			string = string.replace(u'அல்',u'<அல்{INST}>')
			isWhat = 1
	if(u'இல்' in string) :
		string = string.replace(u'இல்',u'<இல்{LOC}>')
		isWhat = 1
	if(u'க்அண்' in string) :
		string = string.replace(u'க்அண்',u'<கண்{LOC}>')
		isWhat = 1
	if(u'அத்உ' in string) :
		for i in tenseSuffix :
			if(i in string and i != u'த்') :
				isWhat = 2
				break
		if(isWhat != 2) :
			string = string.replace(u'அத்உ',u'<அது{GEN}>')
			isWhat = 1
	if(u'இன்' in string) :
		for i in verbSuffix :
			if(i in string) :
				isWhat = 2
				break
		if(isWhat != 2) :
			string = string.replace(u'இன்',u'<இன்{GEN}>')
			isWhat = 1
	if(u'உம்' in string) :
		for i in tenseSuffix :
			if(i in string) :
				isWhat = 2
				break
		if(isWhat != 2)	:
			string = string.replace(u'உம்',u'<உம்{GEN}>')
			isWhat = 1
	if(u'க்அள்' in string) :
		string = string.replace(u'க்அள்',u'<கள்{PL}>')
		isWhat = 1
	if(u'ஐ' in string) :
		string = string.replace(u'ஐ',u'<ஐ{ACC}>')
		isWhat = 1
	return string

def tamilMorphologicalAnalyzer(sample_text) :
	sample_text_letters = u''
	suffix = u''
	prefix = u''
	stem = u''
	stem_letters = u''
	morphTag = u''

	stem = getStem(sample_text)
	stem_letters = tamil.utf8.get_letters(stem)
	sample_text = sample_text.decode('utf8')
	sample_text_letters = tamil.utf8.get_letters(sample_text)
	suffix = suffixRemove(stem_letters,sample_text_letters)
	if(SetPrefix == 1) :
		prefix,suffix = getPrefixSuffix(stem_letters,sample_text_letters)
	if(SetSuffix == 0) :
		suffix = combineMeiUyirString(suffix) 
	morphTag = stem + suffix
	morphTag = morphTag.replace(stem,('<%s{ROOT}>' % stem))
	morphTag = nounSuffixTagging(morphTag)
	if(isWhat == 0 or isWhat == 2)	 :
		morphTag = verbSuffixTagging(morphTag)
	if(isWhat == 2) :
		morphTag = morphTag.replace('ROOT','VP')
	if(isWhat == 1):
		morphTag = morphTag.replace('ROOT','NP')
	morphTag = prefix + morphTag
	return morphTag