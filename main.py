from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep

import TimeVideoFilter
import Streamerlink #not active now

global streamLink
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = ChromeService(executable_path=(r"C:\Users\HiroKen\PycharmProjects\RobotYoutuber\chromedriver.exe"))#SET PATH FOR CHROMEDRIVER /////// EXAMPLE r"C:\Users\HiroKen\source\repos\TwitchClipsDownloader\chromedriver.exe"
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window() #Maximize chrome window // you can delete this if you want

streamLink = ["https://www.twitch.tv/STREAMERNAME/videos?filter=clips&range=7D",
              "https://www.twitch.tv/STREAMERNAME/videos?filter=clips&range=24H"
              ] #Stream link ex = https://www.twitch.tv/STREAMERNAME/videos?filter=clips&range=7D 
                #Use videos?filter=clips&range= in end and put 24H or 7D for the time of the classification of the clips

for link in streamLink: #repeat the process the number of times there are lines in streamLink
    f = open("Clips.txt", "r+") #open "Clips.txt"
    Clips = f.readlines() #read all lines from the file "Clips.txt"
    try: #try and skip if it finds an error to avoid the crash / freeze
        driver.get(link) #go to the streamer's channel
        sleep(5) #sleep for loading / connection ..... 
        links = driver.find_element_by_xpath("//*[@data-a-target='preview-card-image-link']") #get the most viewed clip
        links = str(links.get_attribute('href')) #get the most viewed clip "filter"
        if Clips.__contains__(links + "\n"): #open Clips.txt and check if he contains the links
            print("already got this clip")
            f.close() #close clip.txt
        else:
            print("downloading clip....") 
            f.write("\n" + links + "\n") #open Clips.txt
            driver.get(links) #click on the last most viewed clip
            sleep(5) #sleep to avoid errors, loading / connection .....
            links = driver.find_element_by_xpath("//*[contains(@src, 'https://production.assets.clips')]") #get download link
            links = str(links.get_attribute("src")) #get download link "filter"
            driver.get(links) #go to the download link
            f.close() #close Clips.txt
            sleep(3) #sleep for loading / connection .....
    except:
        pass #pass all error
             #fix and display error = work in progress....

sleep(7) #increase this sleep if you have bad connection .....
driver.quit() #close chrome


TimeVideoFilter.GetClipPath() #file creation for each best of
