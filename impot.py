import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
z1=237
z2=239
X1=52
X2=54

ABRI_x=X2 + 5
ABRI_Y=300
ABRI_Z=z2 + 1
impot = 0
DansEnclo = 0

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x>X1 and pos.x<X2 and pos.z>z1 and pos.z<z2:
        DansEnclo = DansEnclo+1
        mc.postToChat("il te reste " + str(4-DansEnclo) + " secondes")

    else:
        DansEnclo=0
    if DansEnclo>3:
        mc.player.setPos(ABRI_x,ABRI_Y,ABRI_Z)
        DansEnclo = 0