This is  a simple python based script. It has a CFG file in the zip which explains how to edit the values in order to change the default filename and file path for Baldur's Gate 3 modsettings.lsx.

Default Path:
%LOCALAPPDATA%\Larian Studios\Baldur's Gate 3\PlayerProfiles\Public



Since the script modifies files in the user's App Data directory, administrator privileges may be required.
Second, make sure not to run the mod twice after install as I'm not sure if that may or may not cause errors.

Source Code:

Github Repository

Note:
I realize not everyone may be having issues, but for me and my friends we had to scour nexus for hours to find someone who had managed to pinpoint the issue, and I got annoyed doing it manually every time I wanted to try a mod.

The issue is, that the mod manager currently deletes the "GustavDev" info in the modsettings.lsx file, this will first extract the specific info for your game and then reapply it once your mods are install.

To use it:

1. Make sure your modsettings.lsx file in your Local AppData is unchanged and normal.

2. Extract the zip anywhere; into its own folder ideally.

3. Run the exe, it should create a game_version.lsx file in the tool's folder, this stores the information needed to patch your modsettings.lsx file for the current version of the game (This will need to be deleted and the process repeated every time the game is updated, but does not need to be opened or modified).

4. Apply your mods using the BG3 mod manager.

5. Run the .exe again, you can double check the modsettings.lsx file if something goes awry. It should have added a mod with the name of "GustavDev" and added something at the top of your mod order.

Thats it! Your mods should work! Also, this fix should work for future versions of Baldur's Gate 3.


To update this tool for a new version of Baldur's gate 3 or if you want to add more mods and your game_version.lsx file is missing:


1. Delete your modsettings.lsx file in Local Appdata, than run your game. (This will create a new baseline file)

2. If the game has updated, delete your game_version.lsx file in the tool's folder. Then run the tool as if it is a first time use.

I imagine this will become obsolete as the BG3 Mod Manager is updated, but it should work perpetually.
