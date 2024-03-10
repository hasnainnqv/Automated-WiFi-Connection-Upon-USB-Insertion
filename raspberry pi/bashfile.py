import subprocess
import re
import getpass

import time
class Connect_Wifi:
	def __init__(self):
		pass

	def get_networks(self):
		config = "raspberry_pi_wifi/wpa_copy.conf"
		with open(config, 'r') as file:
			matches = file.read()

		networks= {}
		pattern = re.compile(r'network=\{(.*?)\}',re.DOTALL)
		matches = pattern.findall(matches)
		network_list = [] 
		for match in matches:
			key_value = [kv.strip() for kv in match.split('\n') if kv.strip()]
			network_info = {}
			for kv in key_value:
				key, value = [part.strip('"') for part in kv.split('=')]
				network_info[key] = value
			network_list.append(network_info)
		return network_list
		
		
	def execute_sudo(self, sh_file):
		try:
			subprocess.run(['bash',sh_file])
		except subprocess.CalledProcessError as e:
			print(f"error {e}")



	def read_txt(self, path):
		content = open(path,'r')
		content = content.read()
		pattern = re.compile(r'ssid\s*=\s*"([^"]+)"\s*\n\s*pass\s*=\s*"([^"]+)"')
		match = pattern.search(content)
		if match:
			ssid = match.group(1)
			password = match.group(2)
			
		return [ssid,password]

	def get_ssid(self, ssid,password):
		for network in network_list:
			if network['ssid'] == ssid:
				return network['ssid'],network['psk']


	def appending_usb_sh(self, path,ssid,password):
		content = f'''ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={{
	ssid="{ssid}"
	psk="{password}"
	}}
			'''	
		with open(path, 'w+') as conf:
			conf.write(content)

	
	def Run_code(self):
		hostname = getpass.getuser()
		
		result = subprocess.run(['ls',f'/media/{hostname}/'],capture_output=True, text = True)
		time.sleep(4)		
		folder = result.stdout.strip()
		print(folder)
		path = f'/media/{hostname}/{folder}/pass.txt'
		
		
		if open(path,'r'):
			print("true")
		else:
			return "File Not Found i.e no pass.txt"
						
		ssid,password = self.read_txt(path)
		time.sleep(5)
		print(f'{ssid,password}')
		self.network_list = self.get_networks()	

		path = "raspberry_pi_wifi/wpa_copy.conf"		
		self.appending_usb_sh(path, ssid,password)


		sh_file = "raspberry_pi_wifi/modified.sh"
		self.execute_sudo(sh_file)
		time.sleep(10)


