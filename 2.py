a = int (input ("Количество секунд "))
if ( a >= 356400 ):
    print ("To much for this code")
else:
    h = int ( a / 3600 )
    m = int (( a - h * 3600 ) / 60)
    s = int ( a - h * 3600 - m * 60)
    print (f"{h:02}:{ m:02}:{s:02}")