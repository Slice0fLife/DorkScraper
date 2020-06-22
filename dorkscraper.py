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
dorkForWebServers                     
        #The program parses the arguments specified.
# #What Google Dork does the user want to run.
# #Find files containing passwords.
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
        #Find vulnerable Servers
    elif(args[1]=="-vs"):
        print("Searching for vulnerable servers.")        
        #Find pages containing login portals.
    elif(args[1]=="-lp"):     
        print("Searching for login portals.")       
        #Find footholds
    elif(args[1] =="-fh"):
        print("Searching for footholds.")        
        #Find files containing juicy information.
    elif(args[1] =="-ji"):
        print("Searching for juicy information.")
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
    #What information do they want to be outputted.  
#Run the Google Dork
#Scrape the contents of search for information.
#Return information to console.
