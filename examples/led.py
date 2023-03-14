import pyb
spi = pyb.SPI(7, 25000000, 0, 0)

spi.write_mem(0x1A101000, (1 << 10))
spi.write_mem(0x1A101008, (1 << 10))
