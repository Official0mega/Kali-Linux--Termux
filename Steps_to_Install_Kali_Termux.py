How to Fix Rootfs Corrupted in Kali Linux NetHunter? | installer again or download the file manually


Step1. Install termux with this link = https://f-droid.org/en/packages/com.termux/

Android. ([Play Store release](https://play.google.com/store/apps/details?id=com.termux) is no more updated, so is not recommended.)


Step2.

* Open Termux App. Info 

* Clear Data and Cache

* Open Termux again and run the following commands:
 ```
## pkg update && pkg upgrade -y 

## pkg install git

## pkg install wget
 
##  apt update && apt install python python2 openssh -y


Step3. 
Go to Google Search and type the key words:

"roots fs corrupted solved technically Meer" 

## you should be in this website after typing the above key words(Smoking Achieves): https://technicalmeer.com/tag/kali-linux/ 

## Now... Scroll down till you get to "How to Fix Rootfs Corrupted in Kali Linux NetHunter?" 


## Click on "Read More" 

## You can check your architect by following command.:

getprop ro.product.cpu.abi

## you can download the file in (---secs).. Wait till it is completed. 
Then click on 
"DOWNLOAD Rootfs Files"

## download " (DOWNLOAD 64 bit Rootfs File) arm64-v8a " 64bit"
## download " (DOWNLOAD 32 bit Rootfs File) armeabi or armeabi-v7a"


 
# Please download the files according to your architecture.
 You can check your architect by following command. 

## After download the file update or upgrade your termux by following commands. 

## ## pkg update && pkg upgrade -y 

## pkg install git

## pkg install wget
 
##  apt update && apt install python python2 openssh -y

## wget -O install-nethunter-termux https://offs.ec/2MceZWr 

## Now we will give storage permissions to our termux.
Type this command:

termux-setup-storage 

## now run simply few commands to copy the roots file into
 Home directory and extract the file by following commands.


Type these commands one by one:
## cd storage
	ls
	
	cd downloads
	
	ls
	
	cp filename(kalifs-arm64-full.tar.xz) /$HOME

	cd

	ls

	chmod +x *

	ls


## Good! Now we are in the final step which is to run the following command.

	./install-nethunter-termux

	nh


Nice! You Fix Rootfs Corrupted. Now you will successfully download and install official kali Linux on Android phone.

Below is the Link to get more info about Securing your Kali and other info.


* https://www.makeuseof.com/how-to-change-root-password-kali-linux/

* https://www.codelivly.com/termux-tutorial-with-complete-termux-commands/ 

* https://www.makeuseof.com/how-to-change-root-password-kali-linux/
