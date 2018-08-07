
import subprocess

#wow = u"\u0342"
#print wow
#print u'\u2713'					
#profile = "AbdullahRiaz"+wow+"?Ts iPhone"

#profile = "Blue"
#c = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
#c = [b.split(":")[1][1:-1] for b in c if "Key Content" in b]
#print ("{:<30}|  {:<}".format(profile, c[0]))

file = open('profiles and passwords.txt', 'w+')
a = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]

#a = [ x.replace("'",'*') for x in a]
#a = [ x[ 0 : x.find('*')+1] if x.find('*')!=-1 else x for x in a ]
for i in a:
	print i

print '\n'

a = [ x for x in a if "'" not in x ]
		
for i in a:
	results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
	results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
	try:
		file.write("{:<30}|  {:<}".format(i, results[0])+'\n')
		print ("{:<30}|  {:<}".format(i, results[0]))
	except IndexError:
		file.write("{:<30}|  {:<}".format(i, "")+'\n')
		print ("{:<30}|  {:<}".format(i, ""))