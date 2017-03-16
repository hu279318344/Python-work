import sys
import time

print "Now date is %s" % time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))

this_year = int(time.strftime('%Y',time.localtime(time.time())))
print  type(this_year)
user = "yanghu"


'''
counter = 0
while True:
 if counter < 3:
        name = raw_input('Please input your name:').strip()
        if len(name) == 0:
          print " Empty name, try again"
          continue

         elif name == user:
            pass
         else:
            print "%s is not a valid user, pleas try again!" % name
            counter += 1
            continue
         break
 else:
    print "Too many errors"
    sys.exit()
'''
while True:
    name = raw_input('Please input your name:').strip()
    if len(name) == 0:
                 print " Empty name, try again"
                 continue
    for i in range(3):
            name = raw_input('Please input your name:').strip()
            if name != user :
                print "%s is not a valid user, pleas try again!" % name
                continue
            else:
                pass
            break
    else:
        print "%s Too many errors" % name
        sys.exit()
    break
age = int(raw_input('how old are you?'))
sex = raw_input("Please input your sex:")
dep = raw_input("which department:")
'''
print "name",name,'\n'
print "you are",age,'years old!'
print "so you are were born in:",this_year-age
'''
message = ''' Information of the company staff:
            Name:%s
            Age: %d
            Sex: %s
            Dep: %s
            ''' %(name,age,sex,dep)
print message


if age < 28:
    print "Congratulations! you've got half day's public holiday!"
elif name == user:
    print "Welcome to login, %s" % name
else:
    print "Sorry, you are not login!"