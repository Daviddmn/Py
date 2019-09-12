from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\user\\Desktop\\chromedriver.exe') # პარამეტრად შევა მისამართი ქრომდარივერის რომელსაც გადმოვწერთ სელენიუმის მთავარი ვებსაიტიდან
##ამ ორი ხაზის შემდეგ თუ გავუშვებთ კოდს, ამოვარდება ბრაუზერის ფანჯარა, ამის შემდეგ ჩვენი სურვილისამებრ მოვახდენთ ავტომატიზაციას.                                                                                  

driver.get('https://www.website.com/home/us/') # ამით შევა მოცემულ ბმულზე.

z=driver.find_element_by_css_selector('a') # შეეცდება css სელექტორი 'a' ს ელემენტი და მისამართი იპოვოს თუ იპოვის
z.click() # მაგ ელემენტს დააკლიკებს,
z.back() # ამით უკან დაბრუნება მოხდება 


