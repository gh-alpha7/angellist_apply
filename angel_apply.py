from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

email=input("enter username : ")
password=input("enter password : ")

print("enter skill,like this" + "javascript c++ c python django python/django html css html/css jquery data structure algorithm mysql database sqlite")
my=""
mysk=input("skill : ")
myskill=mysk.split()
print(myskill)

sub=input(" enter you application letter ")
cdriver='c:/Users/Alpha/Downloads/chromedriver.exe'
browser=webdriver.Ie(cdriver)
browser.get('https://angel.co')
login=browser.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[1]/a[2]')
login.click()

time.sleep(10)


usern=browser.find_element_by_xpath('//*[@id="user_email"]')
passn=browser.find_element_by_xpath('//*[@id="user_password"]')


usern.send_keys(email)
passn.send_keys(password)

logi=browser.find_element_by_xpath('//*[@id="new_user"]/div[2]/input')

logi.submit()



jobs=browser.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[1]/div[2]/div/li[3]/a')
jobs.click()

##element = WebDriverWait(browser, 10)
##keyword=browser.find_element_by_xpath('//*[@id="startups_content"]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]')
##keyword.click()
##
##element = WebDriverWait(browser, 10)
##enter_key=browser.find_element_by_xpath('//*[@id="startups_content"]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/input')
##enter_key.send_keys("india",Keys.ENTER)
##
##time.sleep(10)
##jobbs=browser.find_element_by_xpath('//*[@id="startups_content"]/div[1]/div[5]/div/div/div[2]')
time.sleep(10)

job_num=browser.find_element_by_xpath('//*[@id="startups_content"]/div[1]/div[2]/div[1]/div[2]/div[1]/span')
x=int(job_num.get_attribute('innerHTML'))
print(x)
##for i in range(1,90000):
##    s1=str(20000*i)
##    st="window.scrollTo(0," + s1 +")"
##    browser.execute_script( st)
time.sleep(5)
jobwa=browser.find_elements_by_css_selector('div.header-info')
jobwa[0].click()
print(jobwa)

for i in range(0,80000000):
    s1=str(200*(i+1))
    se="window.scrollTo(0," + s1 +")"
    browser.execute_script( se)
    time.sleep(3)
    try:
        jobwa[i].click()
    except:
        continue
    xj=0
    while True:
        time.sleep(10)
        xi=i+2
        xj=xj+1
        sj=""
        
        sj="["+str(xj) +"]"
            
        st='//*[@id="startups_content"]/div[1]/div[5]/div/div/div['+str(xi)+']/div[6]/div/div/div[3]/div[2]/div'+sj+'/div[1]/div[1]/a'
        st1='//*[@id="startups_content"]/div[1]/div[5]/div/div/div['+str(xi)+']/div[6]/div/div/div[3]/div[2]/div/div[1]/div[1]/a'
            
        
        print(st)
        
        if xj==1:
            try:
                try:
                    click1=browser.find_element_by_xpath(st1)
                    click1.click()
                except:
                    click1=browser.find_element_by_xpath(st)
                    click1.click()
            except:
                break
        else:
            try:
                click1=browser.find_element_by_xpath(st)
                click1.click()
            except:
                break
       
        
        
    

    ##//*[@id="startups_content"]/div[1]/div[5]/div/div/div[2]/div[6]/div/div/div[3]/div[2]/div/div[1]/div[1]/a
    ##//*[@id="startups_content"]/div[1]/div[5]/div/div/div[3]/div[6]/div/div/div[3]/div[2]/div/div[1]/div[1]/a
    ##//*[@id="startups_content"]/div[1]/div[5]/div/div/div[4]/div[6]/div/div/div[3]/div[2]/div[1]/div[1]/div[1]/a
    ##//*[@id="startups_content"]/div[1]/div[5]/div/div/div[4]/div[6]/div/div/div[3]/div[2]/div[2]/div[1]/div[1]/a

        time.sleep(10)
        hand=browser.window_handles
        browser.switch_to_window(hand[1])


        skills=browser.find_element_by_xpath('//*[@id="layouts-base-body"]/div[1]/div[3]/div/div[3]/div[2]')
        skill_string=skills.get_attribute('innerHTML')
        skill_list=skill_string.split(',')


        ans=0
        for j in skill_list:
            for k in myskill:
                if j.lower()==k:
                    ans+=1

        if ans+1>=len(skill_list):
        
            apply=browser.find_element_by_xpath('//*[@id="layouts-base-body"]/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[3]/a')
            apply.click()
    
            browser.switch_to_alert()
            time.sleep(5)


            apply_b=browser.find_element_by_xpath('//*[@id="layouts-base-body"]/div[5]/div/div/div/div[2]/div/textarea')
            apply_b.send_keys(sub)

            final=browser.find_element_by_xpath('//*[@id="layouts-base-body"]/div[5]/div/div/div/div[2]/div/div[2]/button')
            
            final.click()
    
        browser.close()
        browser.switch_to_window(hand[0])
    jobwa[i].click()
       




