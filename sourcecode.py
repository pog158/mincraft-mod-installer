import os
import shutil
import requests
import tkinter as tk
from tkinter import messagebox

def get_mod_name(mod_url):
    return os.path.basename(mod_url)

def install_selected_mods(selected_mods):
    # Get the user's AppData directory
    appdata_dir = os.getenv('APPDATA')
    minecraft_dir = os.path.join(appdata_dir, '.minecraft')
    mods_dir = os.path.join(minecraft_dir, 'mods')
    
    # Check if the mods directory exists, if not, create it
    if not os.path.exists(mods_dir):
        os.makedirs(mods_dir)
    
    for mod_name, mod_url in selected_mods.items():
        if mod_url is not None:
            try:
                # Extract the filename from the URL
                mod_path = os.path.join(mods_dir, mod_name)
                
                # Download the mod file
                response = requests.get(mod_url, stream=True)
                with open(mod_path, 'wb') as mod_file:
                    shutil.copyfileobj(response.raw, mod_file)
                
                print(f"Mod '{mod_name}' installed successfully!")
            except Exception as e:
                print(f"Error installing mod '{mod_name}': {str(e)}")
    
    messagebox.showinfo("Success", "Mods installed successfully!")

def select_mods(section_mods):
    selected_mods = {}
    root = tk.Tk()
    root.title("Select mods")
    root.geometry("400x300")

    label = tk.Label(root, text="Select mods")
    label.pack(pady=10)

    for section, mods in section_mods.items():
        section_label = tk.Label(root, text=f"Section: {section}")
        section_label.pack(anchor=tk.W)

        for mod_name, mod_url in mods.items():
            var = tk.BooleanVar()
            var.set(False)
            checkbutton = tk.Checkbutton(root, text=mod_name, variable=var)
            checkbutton.pack(anchor=tk.W)
            selected_mods[mod_name] = (mod_url, var)

    def install_selected_mods_wrapper():
        install_selected_mods({mod_name: mod_url for mod_name, (mod_url, var) in selected_mods.items() if var.get()})
        root.destroy()

    install_button = tk.Button(root, text="Install Selected Mods", command=install_selected_mods_wrapper)
    install_button.pack(pady=10)

    root.mainloop()

# Define the sections and mods with mod names and URLs
section_mods = {
    "QOL, no cheats": {
        "NotEnoughUpdates-2.1.jar": "https://github.com/Moulberry/NotEnoughUpdates/releases/download/2.1.0/NotEnoughUpdates-2.1.jar",
        "NotEnoughCoins-1.14.8.jar": "https://github.com/NotEnoughCoins/NotEnoughCoins/releases/download/v1.14.8/NotEnoughCoins-1.14.8.jar",
        "Skytils-1.9.0-pre4.1.jar": "https://github.com/Skytils/SkytilsMod/releases/download/v1.9.0-pre4/Skytils-1.9.0-pre4.1.jar",
        "Dungeon_Rooms-3.4.0.jar": "https://github.com/Quantizr/DungeonRoomsMod/releases/download/v3.4.0/Dungeon_Rooms-3.4.0.jar",
        "dungeonsguide-4.0.0-beta9.3-standalone.jar": "https://github.com/Dungeons-Guide/Skyblock-Dungeons-Guide/releases/download/v4.0.0-beta9.4/dungeonsguide-4.0.0-beta9.4-standalone.jar",
        "essential.jar (needed for most mods)": "https://downloads.essential.gg/v1/mods/essential/container/updates/stable/forge_1-8-9?action=download",
        "Patcher-1.8.7.jar": "https://static.sk1er.club/repo/mods/patcher/1.8.7/1.8.9/Patcher-1.8.7%20(1.8.9).jar",
        "optifine.jar": "https://optifine.net/downloadx?f=OptiFine_1.8.9_HD_U_M5.jar&x=39a78773684d719a72ed157b1ffb96dc",
        "ChatTriggers.jar": "https://github.com/ChatTriggers/ChatTriggers/releases/download/2.2.0/ctjs-2.2.0-1.8.9.jar",
        "SkyblockAddons": "https://github.com/BiscuitDevelopment/SkyblockAddons/releases/download/v1.7.3/SkyblockAddons-1.7.3+7380-for-MC-1.8.9.jar",
        "skyblockClient-Updater.jar": "https://github.com/SkyblockClient/SkyblockClient-Updater/releases/download/v1.3.5/SkyClient-Updater-1.8.9-forge-1.3.5.jar"
    },
    "cheats": {
        "Skyskipped": "https://github.com/Cephetir/SkySkipped/releases/download/3.6/SkySkipped-3.6.1.jar",
        "Pizza_Loader_V2.jar (from pizzz discord https://blacked.gg/discord)": "https://cdn.discordapp.com/attachments/1202389230228344883/1202389235135545354/Pizza_Loader_V2.jar?ex=6604a63c&is=65f2313c&hm=6c8f4dabc89a45ded4404513671135c4b60513de80fce687a2465614255f17c8&",
        "cheetos.jar (from cheetos discord https://discord.gg/jzms3sY84R)": "https://cdn.discordapp.com/attachments/1117868351880957952/1186243077631909978/ChromaHUD-3.0.jar?ex=660147f5&is=65eed2f5&hm=fa3232b97fde8997bffdefe56516d3dfdf137edcbd273aa3d101e806b8f19466&"
    }
}

# Launch mod selection GUI
select_mods(section_mods)
