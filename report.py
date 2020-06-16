from menu import *
import json

def personalReport(reportData, username):
    file = open('Report/'+username+'.txt','a')
    file.write(reportData)
    
def report(total, ordered_list, username):

    file = open('Report/report.txt','a')
    report_data = '\n' + '\t\t' + '*'*40 + '\n'

    now = datetime.now()
    date = '-'.join(list(map(str,[now.day,now.month,now.year])))

    now_utc = datetime.now(timezone('UTC'))
    time = now_utc.astimezone(timezone('Asia/Kolkata'))
    time = time.strftime("%I:%M:%S %p" )

    report_data += '\t\t' + date.center(40,' ') + '\n' + '\t\t' + time.center(40,' ') + '\n' + '\t\t' + '-'*40 + '\n'
    
    for i,item in enumerate(ordered_list):
        temp = '\t\t  ' + str(i+1) + ' '*2 +  item.name.ljust(15,' ') + str(item.quantity) + ' x ' + str(item.price) + ' = ' + 'Rs. '+str(item.total) + '\n'
        report_data += temp
        
    report_data += '\t\t' + '_'*40 + '\n' + '\t\t' + '  Total' + ' '*20 + 'Rs. ' + str(total) + '\n\n'
    report_data += '\t\t' + '*'*40 + '\n'
    
    personalReport(report_data, username)

    with open('Users/user.json') as json_file: 
        userDataFile = json.load(json_file)
        
    report_data +='\t\t'+username.center(40,' ') + '\n' + '\t\t' + userDataFile[username]['Phone Number'].center(40,' ')+'\n\n'
    report_data += '\t\t' + '*'*40 + '\n\n'                                                                                                       
    
    file.write(report_data)

def view_report(username):
        report = open('Report/'+username+'.txt','r').read()
        print(report)