import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
print(pos.x)
print(pos.y)
print(pos.z)
mc.postToChat("x=" + str(pos.x) + " y=" + str(pos.y) + " z=" + str(pos.z) )
