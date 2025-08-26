

itemsincart = 0

if itemsincart != 2:
    #raise exception("Products not added in the cart") #if condition doesn't match it will throw a exception error message as in  line 6
    pass

#OR
#
# assert (itemsincart == 2) == True


try:
     if int(itemsincart)/2 == 0:
         #print('condition matches')

            raise Exception('itemsincart')
except:
    print("will skip the error")