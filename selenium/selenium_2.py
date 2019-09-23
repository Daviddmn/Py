#არსებობს ბევრი სხვა ხერხები ელემენტის საპოვნელად, აღარ ჩამოვთვლი...
# ახლა, გვაქვს ასეთი სიტვაცია, გვინდა რომ გავაკეთოთ ავტომატიზაცია რომელიც შეიყვანს ავტომატურად ლოგინს და პაროლს და დალოგინდება.

from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\geo\\Desktop\\chromedriver.exe')
driver.get('https://forum.somethying.com/index.php?login/')

z=driver.find_element_by_name('login') # ვიპოვოთ ლოგინის&პაროლის შესაყვანი ველი
z.send_keys('hello little friend')        #ამ კოდით შესაყვან ველში შევიყვანთ ჩვენთვის სასურველ ტექსტს.

# ამის მერე იგივე მეთოდით მოვძებნოთ ელემენტი 'ღილაკი' რომლითაც გავაგზავნით მონაცემებს ფორმ ით 
#გაგზავნა მოხდება z.click()  '.click()' მეშვეობით

