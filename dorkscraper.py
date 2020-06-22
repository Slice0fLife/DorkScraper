from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import sys
print("dorkscraper")
print("v0.1")
print("This tool is solely for educational purposes, please use legally. The creator is not responsible for any misuse of this tool")
args= sys.argv
def dorkForPasswordFiles(output_form,tld):
    results = []
    queries = 	["\"MYSQL_ROOT_PASSWORD:\" ext:env OR ext:yml -git", "filetype:env \"DB_PASSWORD\"","\"index of\" \".env\"","\"config.php.bak\" intitle:\"index of\"", 'intext:"Index of /password"','	intitle:"index of" "config.neon" OR "config.local.neon" ', ' 	intitle:"index of" "passwords.xlsx" ']
    if(output_form=="-s"):
        print("Starting selenium. Please make sure the firefox webdriver is installed.")
        driver =  webdriver.Firefox()
        for query in queries:
            driver.get("https://www.google.com/search?q=" + query + tld)
            search_results = driver.find_elements_by_xpath("//div[@class='rc']")
            for search_result in search_results:
                search_result_text=search_result.text
                results.append(search_result_text)
        #Format results to return useful information
        results_string = "".join(results)
        password=re.search("password", results_string)
        print(results_string)
def dorkForAdvisories(output_form, tld):
    results = []
    queries = 	['intext:"TopManage (R) 2002 - 2020"','inurl:wp-content/plugins/kingcomposer','intext:powered by JoomSport - sport WordPress plugin','inurl:wp-content/themes/newspaper',	'inurl:wp-content/plugins/elementor','"powered by Typo3"','	"index of" "plugins/wp-rocket"','inurl:wp-content/plugins/brizy','	index of /wp-content/uploads/backupbuddy', 'inurl:"wp-contentpluginsphoto-gallery"']
    if(output_form=="-s"):
        print("Starting selenium. Please make sure the firefox webdriver is installed.")
        driver =  webdriver.Firefox()
        for query in queries:
            driver.get("https://www.google.com/search?q=" + query + tld)
            search_results = driver.find_elements_by_xpath("//div[@class='rc']")
            for search_result in search_results:
                search_result_text=search_result.text
                results.append(search_result_text)
        #Format results to return useful information
        results_string = "".join(results)
        password=re.search("password", results_string)
        print(results_string)
def dorkForSensitiveDirectories(output_form, tld):
    results = []
    queries = 	['inurl:member filetype:xls', '	intitle:"index of" "oauth-private.key"', 'inurl:_vti_pvt/service.pwd', 'inurl:admin/data* intext:index of', 'intext:"INTERNAL USE ONLY" ext:doc OR ext:pdf OR ext:xls OR ext:xlsx','intitle:"index of" "admin/sql/"','"index of" "svg"','	intitle:"index of" "survey.cgi"', 'index of logs.tar','"Index of" "sass-cache"','"index of" "fileadmin"','intitle:"index of" inurl:ftp intext:admin']
    if(output_form=="-s"):
        print("Starting selenium. Please make sure the firefox webdriver is installed.")
        driver =  webdriver.Firefox()
        for query in queries:
            driver.get("https://www.google.com/search?q=" + query +tld)
            search_results = driver.find_elements_by_xpath("//div[@class='rc']")
            for search_result in search_results:
                search_result_text=search_result.text
                results.append(search_result_text)
        #Format results to return useful information
        results_string = "".join(results)
        password=re.search("password", results_string)
        print(results_string)
def dorkForWebServers(output_form, tld):
    results = []
    queries = 	['inurl:"id=*" & intext:"warning mysql_fetch_array()"','	"index of /private" -site:net -site:com -site:org','inurl:":8088/cluster/apps"','intitle:"index of" "docker.yml"'.'	intitle:"index of" "debug.log" OR "debug-log"','intext:"This is the default welcome page used to test the correct operation of the Apache2 server"','"Powered by phpBB" inurl:"index.php?s" OR inurl:"index.php?style"','	intitle:"index of" "powered by apache " "port 80"','site:ftp.*.com "Web File Manager"', 'intitle:"Welcome to JBoss"']
    if(output_form=="-s"):
        print("Starting selenium. Please make sure the firefox webdriver is installed.")
        driver =  webdriver.Firefox()
        for query in queries:
            driver.get("https://www.google.com/search?q=" + query +tld)
            search_results = driver.find_elements_by_xpath("//div[@class='rc']")
            for search_result in search_results:
                search_result_text=search_result.text
                results.append(search_result_text)
        #Format results to return useful information
        results_string = "".join(results)
        password=re.search("password", results_string)
        print(results_string)
def dorkForVulnerableServers(output_form, tld):
    results = []
    queries = 	['intext:"Powered By Gila CMS"','intitle:"index of" "shell.php"','intitle:"index of" "filemail.pl"','inurl:/+CSCOE+/logon.html','intitle:"index of" "AT-admin.cgi"','intext:"(c) GUnet 2003-2007"','"Powered by Jira Service Desk"','"Powered by vBulletin Version 5.5.4"','inurl:"q=user/password"','inurl:"/user/register" "Powered by Drupal" -CAPTCHA -"Access denied"','	inurl:"index.php?option=com_joomanager"','inurl:/proc/self/cwd','	"dirLIST - PHP Directory Lister" "Banned files: php | php3 | php4 | php5 | htaccess | htpasswd | asp | aspx" "index of" ext:php']
    if(output_form=="-s"):
        print("Starting selenium. Please make sure the firefox webdriver is installed.")
        driver =  webdriver.Firefox()
        for query in queries:
            driver.get("https://www.google.com/search?q=" + query +tld)
            search_results = driver.find_elements_by_xpath("//div[@class='rc']")
            for search_result in search_results:
                search_result_text=search_result.text
                results.append(search_result_text)
        #Format results to return useful information
        results_string = "".join(results)
        password=re.search("password", results_string)
        print(results_string)
def dorkForLoginPortals(output_form, tld):
    results = []
    queries = 	['inurl:"index.php/user/password/" intext:Password Reset','inurl:candidatelogin.aspx','	intext:"Welcome to Intranet" "login"','	inurl:adminlogin.jsp','	index of "jira" inurl:login','"login" intitle:"intext:"Welcome to Member" login"','inurl:".Admin;-aspx }" "~Login"','intitle:"*Admin Intranet Login"','	intitle:"index of" pass.php','	inurl:.*org/login','intitle:"Intranet Login"','intitle:.*edu/login','inurl:employee-login.php']
    if(output_form=="-s"):
        print("Starting selenium. Please make sure the firefox webdriver is installed.")
        driver =  webdriver.Firefox()
        for query in queries:
            driver.get("https://www.google.com/search?q=" + query +tld)
            search_results = driver.find_elements_by_xpath("//div[@class='rc']")
            for search_result in search_results:
                search_result_text=search_result.text
                results.append(search_result_text)
        #Format results to return useful information
        results_string = "".join(results)
        password=re.search("password", results_string)
        print(results_string)
def dorkForFootholds(output_form, tld):
    results = []
    queries = 	['intitle:"index of" "admin/xml"','	inurl:logon/LogonPoint/index.html','inurl:/download_file/ intext:"index of /"','Find Microsoft Lync Server AutoDiscover','inurl:/servicedesk/customer/user/login','inurl:"customer.aspx"','intitle:("Index of") AND intext:("c99.txt" OR "c100.txt")','	intitle:("Mini Shell") AND intext:("Upload File")','intitle:"(SSI Web Shell)" AND intext:"(ls -al)"','	intitle:"freedom is real - 1945"','inurl:"index.php?db="']
    if(output_form=="-s"):
        print("Starting selenium. Please make sure the firefox webdriver is installed.")
        driver =  webdriver.Firefox()
        for query in queries:
            driver.get("https://www.google.com/search?q=" + query +tld)
            search_results = driver.find_elements_by_xpath("//div[@class='rc']")
            for search_result in search_results:
                search_result_text=search_result.text
                results.append(search_result_text)
        #Format results to return useful information
        results_string = "".join(results)
        password=re.search("password", results_string)
        print(results_string)
def dorkForJuicyInformation(output_form, tld):
    results = []
    queries = 	['intext:"Not to be distributed" ext:doc OR ext:pdf OR ext:xls OR ext:xlsx','"Index of" "/access"','index of /backend/prod/config','intitle:"index of" secrets.yml','intitle:"index of /" "*key.pem"','"index of" "siri"','intext:"index of /" "*.yaml"','	index of .svn/text-base/index.php.svn-base','"Index of" "customer.php"','"root.log" ext:log','	intitle:"index of" "dev/config"','index of "logs.zip"','index of "dbbackup"','	intitle:"index of /" "nginx.conf"','	"microsoft internet information services" ext:log']
    if(output_form=="-s"):
        print("Starting selenium. Please make sure the firefox webdriver is installed.")
        driver =  webdriver.Firefox()
        for query in queries:
            driver.get("https://www.google.com/search?q=" + query +tld)
            search_results = driver.find_elements_by_xpath("//div[@class='rc']")
            for search_result in search_results:
                search_result_text=search_result.text
                results.append(search_result_text)
        #Format results to return useful information
        results_string = "".join(results)
        password=re.search("password", results_string)
        print(results_string)
dorkscraper_tld=None
dorkscraper_output_form=args[2]
if (len(args) > 2 ):
    dorkscraper_tld="site:"+args[3]
if(len(args) > 1):
    if(args[1] =="-fp"):
        print("Searching for files contaning passwords.")
        dorkForPasswordFiles(dorkscraper_output_form, dorkscraper_tld)
        #Find advisories and vulnerabilities
    elif(args[1] =="-av"):
        print("Searching for advisories and vulnerabilities")
        dorkForAdvisories(dorkscraper_output_form, dorkscraper_tld)
        #Find sensitive directories.
    elif(args[1]=="-sd"):
        print("Searching for sensitive directories.")
        dorkForSensitiveDirectories(dorkscraper_output_form,dorkscraper_tld)
        #Find web servers.
    elif(args[1]=="-ws"):
        print("Searching for web servers")
        dorkForWebServers(dorkscraper_output_form, dorkscraper_tld)
        #Find vulnerable Servers
    elif(args[1]=="-vs"):
        print("Searching for vulnerable servers.")
        dorkForVulnerableServers(dorkscraper_output_form,dorkscraper_tld)
        #Find pages containing login portals.
    elif(args[1]=="-lp"):
        print("Searching for login portals.")
        dorkForLoginPortals(dorkscraper_output_form, dorkscraper_tld)
        #Find footholds
    elif(args[1] =="-fh"):
        print("Searching for login portals.")
        dorkForFootholds(dorkscraper_output_form, dorkscraper_tld)
        #Find files containing juicy information.
    elif(args[1] =="-ji"):
        print("Searching for juicy information.")
        dorkForJuicyInformation(dorkscraper_output_form, dorkscraper_tld)
    elif(args[1] =="-help"):
        print("General usage. dorkscraper.py <dork> <output> <tld/targeturl>")
        print("-fp searches for files containing passwords. usage: dorkscraper.py -fp")
        print("-av searches for advisories and vulnerabilities. usage: dorkscraper.py -av")
        print("-sd searches for advisories and vulnerabilities. usage: dorkscraper.py -sd")
        print("-ws searches for web servers usage: dorkscraper.py -ws")
        print("-vs searches for vulnerable servers. usage: dorkscraper.py -vs")
        print("-lp searches for login portals. usage: dorkscraper.py -lp")
        print("-fh searches for footholds usage: dorkscraper.py -fh")
        print("-ji searches for files containing juicy information usage: dorkscraper.py -ji")
    else:
        print("Argument not recognized, use dorkscraper.py -help for help.")
