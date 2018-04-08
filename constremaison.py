import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
DIMENSION = 20
pos = mc.player.getTilePos()
x = pos.x+2
y = pos.y
z = pos.z
midx = x + DIMENSION/2
midy = y + DIMENSION/2
mc.setBlocks(x,y, z, x+DIMENSION, y+DIMENSION, z+DIMENSION, block.DIAMOND_BLOCK.id)
mc.setBlocks(x+1, y+1, z, x+DIMENSION-2, y+DIMENSION-2, z+DIMENSION-1, block.AIR.id)