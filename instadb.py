import cx_Oracle
con = cx_Oracle.connect("ankit123/ankit")
cur = con.cursor()
print("Select from the below options ")
print("---------------------------------------- ")
print("Press 1 for Max Likes")
print("Press 2 for Min Likes")
print("Press 3 for Music Pictures")
print("Press 4 for Popular Tag")
print("Press 5 for Most Liked User")
print("Press 6 for Old Tagging")
print("Press 7 to delete inactive users")
print("---------------------------------------- ")
choice = int(input("Press the appropriate key depending on your choice \n"))
if (choice == 1):
    cur.execute("SELECT PIC_ID FROM PICTURE WHERE LIKES=(SELECT MAX(LIKES) FROM PICTURE)")
    for i in cur.fetchall():
        print("The picture id with maximum likes is:",i[0])
elif (choice == 2):
    cur.execute("SELECT PIC_ID FROM PICTURE WHERE LIKES=(SELECT MIN(LIKES) FROM PICTURE)")
    print("The picture id with minimum likes are:")
    for i in cur.fetchall():
        print(i[0])
elif (choice == 3):
    cur.execute("SELECT PIC_ID FROM PICTURE WHERE TAGS='MUSIC'")
    print("The picture id related to music are:")
    for i in cur.fetchall():
        print(i[0])
elif (choice == 4):
    cur.execute("SELECT TAGS FROM PICTURE GROUP BY TAGS HAVING COUNT(TAGS)=(SELECT MAX(MYCOUNT) FROM (SELECT COUNT(TAGS) MYCOUNT FROM PICTURE GROUP BY TAGS))");
    print("The most popular tag is:")
    for i in cur.fetchall():
        print(i[0])
elif (choice == 5):
    cur.execute("SELECT FNAME,LNAME FROM USERS WHERE USER_ID=(SELECT USER_ID FROM PICTURE WHERE LIKES=(SELECT MAX(LIKES) FROM PICTURE))");
    print("The user who has been liked most:")
    for i in cur.fetchall():
        print(i[0],i[1])
elif (choice == 6):
    cur.execute("SELECT PIC_ID,TAGS FROM PICTURE WHERE (SYSDATE-DATE_POSTED) > 1095");
    print("The user with a picture tag of more than 3 years is:")
    for i in cur.fetchall():
        print(i[0],i[1])
elif (choice == 7):
    cur.execute("DELETE FROM PICTURE WHERE (SYSDATE-DATE_POSTED) > 365")
    print("The rest of the users are:")
    for i in cur.fetchall():
        print(i)
else:
    print("Sorry wrong choice")
con.close()