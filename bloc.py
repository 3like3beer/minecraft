import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlock(pos.x+3, pos.y, pos.z, block.STONE_BRICK.id)
mc.setBlock(pos.x+4, pos.y, pos.z, block.STONE_BRICK.id)
mc.setBlock(pos.x+5, pos.y, pos.z, block.STONE_BRICK.id)
mc.setBlock(pos.x+6, pos.y+1, pos.z, block.STONE_BRICK.id)
mc.setBlock(pos.x+3, pos.y+2, pos.z, block.STONE_BRICK.id)
mc.setBlock(pos.x+3, pos.y+3, pos.z, block.STONE_BRICK.id)
mc.setBlock(pos.x+3, pos.y, pos.z+1, block.STONE_BRICK.id)
mc.setBlock(pos.x+3, pos.y, pos.z+2, block.STONE_BRICK.id)
mc.setBlock(pos.x+3, pos.y, pos.z+3, block.STONE_BRICK.id)
mc.setBlock(pos.x+3, pos.y, pos.z+4, block.STONE_BRICK.id)
