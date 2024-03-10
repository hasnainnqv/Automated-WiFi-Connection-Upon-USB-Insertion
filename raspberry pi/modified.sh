sudo chmod 666 /etc/wpa_supplicant/wpa_supplicant.conf
sudo cp /home/admin/Downloads/raspberry_pi_wifi/wpa_copy.conf  /etc/wpa_supplicant/wpa_supplicant.conf

sudo systemctl restart wpa_supplicant
sudo systemctl restart dhcpcd
