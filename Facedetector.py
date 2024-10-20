import face_recognition

'''
when trying to install this setup please go through the link below for setup
https://github.com/ageitgey/face_recognition?tab=readme-ov-file


Also install "pip3 setuptools" this is not mentioned in the library module 
but unless it is installed it won't work.
'''

#empty list of trusted user images
trusteduserlist=[]

#function that verifies if the user is valid user or not
def checkuser(userimage):
    #intially we set the fact to -1 that means nothing is decided yet
    fact=-1
    #we load up the userimage that was passed as parameter
    unknown_image = face_recognition.load_image_file(userimage)
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    #we traverse through the trusteduser list
    for x in trusteduserlist:
        trusteduser=face_recognition.face_encodings(x)[0]
        results = face_recognition.compare_faces([trusteduser], unknown_encoding)
        
        #we compare the unknown user face to trusted user face list that we have
        if(results[0]==True):
            fact=1
            #if it is a valid user we set the fact to 1 that means we return true
            break
        else:
            #if it is not a valid user we set the fact to 0 that means we return false
            fact=0
    if(fact==1):
        return True
    else:
        return False
        
#function to add new trusted users
def adduser(userimage):
    user1 = face_recognition.load_image_file(userimage)
    trusteduserlist.append(user1)


adduser("Trustedusers/user1.jpg")
adduser("Trustedusers/user2.jpg")
adduser("Trustedusers/user3.jpg")

print("",checkuser("unknownuser1.jpg"))
print("",checkuser("unknownuser2.jpg"))
print("",checkuser("unknownuser3.jpg"))
print("",checkuser("unknownuser4.jpg"))

