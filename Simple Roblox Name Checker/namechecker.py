import robloxpy
print("""\
               ___.    .__            __             .__              __                      __                      .___                                      
_______   ____ \_ |__  |  |    ____  |  | __   ____  |  |__    ____  |  | __  ____ _______  _/  |_  ____  ______    __| _/ ____    ____    ____    ____ _______ 
\_  __ \ /  _ \ | __ \ |  |   /  _ \ |  |/ / _/ ___\ |  |  \ _/ __ \ |  |/ /_/ __ \_  __ \ \   __\/  _ \ \____ \  / __ | /  _ \  / ___\  / ___\ _/ __ \_  __  \
 |  | \/(  <_> )| \_\ \|  |__(  <_> )|    <  \  \___ |   Y  \  ___/ |    < \  ___/ |  | \/  |  | (  <_> )|  |_> >/ /_/ |(  <_> )/ /_/  >/ /_/  >\  ___/ |  | \/
 |__|    \____/ |___  /|____/ \____/ |__|_ \  \___  >|___|  / \___  >|__|_ \ \___  >|__|     |__|  \____/ |   __/ \____ | \____/ \___  / \___  /  \___  >|__|   
                    \/                    \/      \/      \/      \/      \/     \/                       |__|         \/       /_____/ /_____/       \/          
    """)
usernames = input("What is the name of your usernames folder?")
x = 0
while x <3:
    unclaimed_file = open("unclaimed.txt", "a")
    word_file = open(usernames, "r")
    word_array = word_file.readlines()

    print("[INFO] {0} words were read from the provided file.".format(len(word_array)))
    print("Starting :)")

    for x in range(len(word_array)):

        word = word_array[x].strip()
        Id = robloxpy.User.External.GetID(word)

        try:
            int(Id)
            print("Username: " + word + " is not available.")
        except:
            print("Username: " + word + " might be available")
            unclaimed_file.write(word + ",")
    print("All names are checked :)")
    unclaimed_file.close()


exit()

