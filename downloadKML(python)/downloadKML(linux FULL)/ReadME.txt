1.please input your gmail id and password on line 26, 31 downloadKML.py
2.please change download_path on line 34 in the same file
3.please install and run following commands

--install pip
first of all you need install python module
sudo apt update
sudo apt install python3-pip
pip3 –version
python –m pip install selenium

--install headless chrome
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:canonical-chromium-builds/stage
sudo apt-get update
sudo apt-get install chromium-browser 

--install chrome-driver
sudo apt-get update
sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4
sudo apt-get install default-jdk 

wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
wget https://selenium-release.storage.googleapis.com/3.13/selenium-server-standalone-3.13.0.jar
wget http://www.java2s.com/Code/JarDownload/testng/testng-6.8.7.jar.zip
unzip testng-6.8.7.jar.zip
xvfb-run java -Dwebdriver.chrome.driver=/usr/bin/chromedriver -jar selenium-server-standalone.jar
chromedriver --url-base=/wd/hub


--install pykml module on ubuntu to parse the kml file
Sudo –m pip install pykml

And please replace the "import urllib2" to following code on "/usr/local/lib/python3.6/dist-packages/pykml/parser.py", line 8


try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
	
																																													

