
# Doomsday client bypassing screenshare loader
The loader automates the environment setup and execution of the client.

Auto-Environment: Automatically creates the C:\Symbols directory if it doesn't exist.

Dependency Check: Verifies if temp.pdb (the JAR executable) is present.

Auto-Download: Fetches the latest version directly from the official source if the file is missing.

Execution: Launches the client via Java.


For better bypass use my string cleaner. 


# What you can do more?

   Quick tutorial on enabling and disabling prefetch.
 This will barely help you bypass anything
A good screensharer will look for if you ever disabled **Prefetch**. 

1. Open the “Registry Editor” using Windows search or do Win+R and type in `regedit`
2. Goto or put in the adress `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters`
3. Double-click on “EnablePrefetcher” to open this key. In “Value data” put “0” to turn Prefetch off.
4. Launch doomsdaybypass.exe
5. Double-click on “EnablePrefetcher” to open this key. In “Value data” put “3” to turn Prefetch on.
