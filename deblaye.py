import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
dimension = int(raw_input("dimension de l'espace a deblayer ?"))


mc.postToChat("x=" + str(pos.x) + " y=" + str(pos.y) + " z=" + str(pos.z))

mc.setBlocks(pos.x , pos.y , pos.z ,
            pos.x + dimension, pos.y + dimension,pos.z + dimension, block.AIR.id)


