import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
a = 20
print (a)

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x == 60 and pos.z == 241:
        mc.postToChat("BIENVENUE")
