import json
import os 

from rich.prompt import Prompt
from rich import style
from rich.console import Console

console = Console()


def main():
	console.print('\t\t*********************system health*********************',style='bold red')
	console.print('1.Display available RAM',style='bold #7C53E7')
	console.print('2.Display Load avearge',style='bold #7C53E7')
	console.print('3.Display Hostname details',style='bold #7C53E7')
	console.print('4.Display All process count',style='bold #7C53E7')
	console.print('5.Display uptime',style='bold #7C53E7')
	console.print('6.Exit',style='bold #7C53E7')

def display_avail_ram():
	d=[]
	cmd=os.popen('free -m').read()
	for i in cmd.split():
		d.append(i)
	print(d)
	console.print(f'avaiable memory ==>',d[11],style='bold red')

def display_load_avg():
    cmd = 'cat /proc/loadavg'
    res = os.popen(cmd).read()
    console.print(f'load average ===> {res}', style='italic #7C53E7 ')

def hostname_details():
	cmd= 'uname -a '
	cmd1= 'uname'
	res=os.popen(cmd).read()
	res1=os.popen(cmd1).read()
	console.print(f'--------------hostname details-------------------------',style='bold red')
	console.print(f'{res}',style='bold #F908E6 ')
	console.print(f'hostname ===>{res1}',style='bold green ')

def process_count():
	cmd='ps -a | wc -l'
	res =os.popen(cmd).read()
	console.print(f'all process counted ==> {res} ',style='bold blue')

def uptime():
	cmd= 'uptime' 
	res=os.popen(cmd).read()
	console.print(f'uptime ====> {res}',style='bold #F908E6 ')
	
	
while True :
	main()

	ch=int(input('Enter your choice '))
	if   ch == 1:
		display_avail_ram()
	elif ch == 2 :
		display_load_avg()
	elif ch == 3 :
		hostname_details()
	elif ch == 4:
		process_count()
	elif ch == 5:
		uptime()
	elif ch ==6 :
		console.print('------------------Exit----------------',style='bold #F908E6 ')
		break
	else:
		console.print('---------------wrong options-----------please enter valid opation',style='bold red')


