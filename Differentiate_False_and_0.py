# პროგრამულ ენაში False უდრის 0-ს და True უდრის 1-ს (int)
# მაგალითად ლისტში (სიაში) გვაქვს ინტეჯერები და ქეივორდები, მაგ: a = [1,2,0,1,0,1,None,0,False]
# და გვინდა რომ ამ ლისტიდან ამოვშალოთ 0 ები მაგრამ არა False, რადგან 0 იც იგივე False ია 
# ამისთვის საჭიროა for ციკლი და is კეივორდი

a = [1,2,0,1,0,1,None,0,False]

for x in a: 
    if x is 0:
        continue
    print(x)
    
# is ით მოხდა კონკრეტულად 0 ის გამოტოვება თუ გამოვყენებდით == მოხდებოდა false ის გამოტოვებაც.

# In computer 0 is False and 1 is True, if we got list with integer 0 and keyword False, and we need to remove only integer 0
# we have to use keyword is , if we'll use == integer 0 and keyword False will be removed both from list array.
