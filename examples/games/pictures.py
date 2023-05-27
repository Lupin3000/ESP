from framebuf import FrameBuffer, MONO_HLSB


human_icon = FrameBuffer(
    bytearray(b'\x00\x00\x0c\x00\x0e\x00\x04\x00\x00\x00\x3f\x00\x3f\x00\x3f\x80'
              b'\x7f\x80\x5e\x80\x5e\x80\x1e\x40\x12\x00\x12\x00\x12\x00\x12\x00'
              b'\x12\x00\x12\x00\x12\x00\x12\x00'), 16, 20, MONO_HLSB)

space_ship = FrameBuffer(
    bytearray(b'\x00\x04\x00\x00\x00\x0f\x80\x00\x00\x1f\xc0\x00\x01\x3f\xc0\x00\x00\x3f'
              b'\xe0\x00\x0c\x3f\xc8\x00\x1e\x3f\x9e\x00\x3f\x1c\x3f\x00\x7f\xc0\xff\x00'
              b'\x0f\xff\xfc\x00\x47\xff\xf8\x80\x3c\x7f\x8f\x00\x0e\x21\x0c\x00\x23\xe1'
              b'\xf1\x00\x18\x7f\x06\x00\x07\x00\x38\x00\x79\xff\xe7\x80\x78\x1e\x07\x80'
              b'\x70\x0c\x01\x80\x40\x0c\x00\x80\x40\x00\x00\x80\x40\x00\x00\x80\x40\x00'
              b'\x00\x80\x40\x00\x00\x00\x00\x00\x00\x00'), 32, 25, MONO_HLSB)

alien_screen = FrameBuffer(
    bytearray(
        b'\x00\x00\x07\x7f\xd0\x00\x00\x00\x07\xe0\x00\x00\x03\xff\xff\xf8\x00\x00\x0e\x7f\xe0\x00\x80\x00'
        b'\x04\x00\x00\x00\x03\xff\xff\xff\x00\x00\x5e\xff\xf8\x01\x80\x00\x00\x07\x80\x00\x01\xbf\xff\xff'
        b'\x00\x00\x3f\xff\x88\x01\x00\x00\x00\x03\xf0\x00\x00\xff\xff\xff\x00\x00\x7d\xff\xc0\x00\x00\x00'
        b'\x00\x01\xfe\x00\x01\xff\xff\xff\x00\x00\xf9\xff\x98\x04\x01\x00\x00\x00\xff\x80\x01\xff\xff\xff'
        b'\x00\x00\xfb\xff\xe0\x04\x00\x00\x00\x00\xff\xc0\x00\xff\xff\xff\x00\x01\xff\xff\xc0\x00\x00\x00'
        b'\x00\x00\xff\xf0\x00\xff\xff\xff\x00\x05\xff\xff\xc0\x00\x00\x00\x00\x00\x7f\xf0\x00\x7f\xff\xff'
        b'\x00\x01\xff\xff\x80\x00\x00\x06\x00\x00\x7f\xfc\x00\xff\xff\xff\x00\x01\xff\xfe\x80\x00\x00\x00'
        b'\x00\x00\x3f\xfc\x00\x7f\xff\xff\x00\x0f\xff\xfe\x00\x00\x00\x00\x00\x00\x7e\x7e\x00\x7f\xff\xff'
        b'\x00\x0f\xff\xfe\x00\x18\x00\x01\x80\x00\x3f\x3e\x00\x3f\xff\xff\x00\x07\xff\xfe\x00\x18\x0e\x08'
        b'\x00\x00\x1f\x9f\x00\x3f\xff\xff\x00\x07\xff\xff\x00\x00\x08\x02\x00\x00\x1f\xcf\x00\x3f\xff\xff'
        b'\x00\x0f\xff\xff\x80\x00\x68\x01\x00\x0f\x7f\xc7\x00\x3f\xff\xff\x00\xcf\xff\xfd\x83\x7a\x14\x01'
        b'\x02\x1e\xff\xe3\x00\x7f\xff\xff\x03\xff\xff\xff\xb1\x7f\x06\x01\x30\x7c\xff\xe1\x80\x7f\xff\xff'
        b'\xf7\xff\xff\xff\xc0\xff\xf6\x37\x34\xf1\xf1\xf1\x80\xff\xff\xff\xf8\x7f\xff\xff\xc0\x7f\xff\xff'
        b'\xff\xe3\x7c\xf0\x81\xff\xff\xff\xf8\x1e\xff\xff\x80\x7f\xff\xff\xff\xff\xf8\x70\x83\xff\xff\xff'
        b'\xf8\x1f\xbf\xff\x84\xff\xff\xff\xff\xff\xf8\x70\xc7\xff\xff\xff\xf8\x3f\xdf\xfe\x06\x7f\xff\xff'
        b'\xff\xff\xf9\xb0\x0f\xff\xff\xff\xff\xff\xff\xfe\x67\x7f\xff\xff\xff\xff\xfb\x38\x5f\xff\xff\xff'
        b'\xff\xff\x7b\xfb\xf2\xff\xff\xff\xff\xff\xf2\x48\x7f\xff\xff\xff\xff\xff\xff\xf1\xf1\xff\xff\xf0'
        b'\xff\xff\xf0\x80\x7f\xff\xff\xff\xff\xff\xff\xc3\x81\x9f\xff\xe0\x7f\xff\xfd\x00\x7f\xff\xff\xff'
        b'\xff\xff\xff\xcf\xc4\xff\xff\x80\x7f\xff\xfe\x4c\x3f\xff\xff\xff\xff\xff\xff\x3f\xf2\xef\xff\x00'
        b'\x5f\xff\xfc\x0a\x0f\xff\xff\xff\xff\xff\xf8\x07\xf8\xff\xfe\x00\x5f\xff\xfc\x90\x5f\xff\xff\xff'
        b'\xff\xff\x00\x7f\xff\xff\xfc\x00\x0f\xff\xfd\x24\xbf\xff\xff\xff\xff\xff\x01\xff\xff\xff\xe0\x00'
        b'\x03\xff\xfa\x4c\x3f\xff\xff\xff\xff\xff\xff\xff\xff\xf8\x00\x00\x03\xff\xfc\xdb\x1f\xff\xff\xff'
        b'\xff\xff\xff\xff\xff\xf8\x80\x00\x01\xff\xff\x16\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xf7\x00\x00'
        b'\x00\xff\xff\xf0\x8f\xff\xff\xff\xff\xff\xff\xff\xff\xde\x00\x00\x08\x1f\xff\xfc\x03\xff\xff\xff'
        b'\xff\xff\xff\xff\xff\xfc\x00\x3c\x3f\x7f\xff\xff\x03\xff\xff\xff\xff\xff\xff\xff\xff\xd8\xe3\xb0'
        b'\x67\x9f\xff\xff\xc0\xff\xff\xff\xff\xff\xff\xff\xff\xf8\xbf\x03\x7f\xff\xff\xff\xf0\x0f\xff\xff'
        b'\xff\xff\xff\xff\xff\xeb\xff\x82\xff\xff\xff\xff\xfc\x07\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
        b'\xff\xff\xff\xff\xff\xf7\xff\xff\xff\xfb\xff\xff\xff\xfe\x07\xff\xff\xff\xff\xff\xff\xff\xff\xff'
        b'\xff\xff\xff\xff\xff\xe0\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\x80\x0f'
        b'\xe3\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf7\xe0\x00\x00\x3f\xff\xff\xff\xff\xff\xff'
        b'\xff\xff\xff\xff\xff\xfe\xe0\x00\x1f\xdf\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\x11'
        b'\x9f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\x77\xff\xff\xff\xff\xff\xff\xff\xff'
        b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf7\xff\xff\xff\xff\xff\xff\xff\xff'
        b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
        b'\xff\xff\xff\xff\xff\xfd\xc7\xff\xff\xff\xbb\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe7\xff'
        b'\xff\xff\xbf\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfb\xff\xff\xff\xff'
        b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe9\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf3'
        b'\xff\xff\xff\xe0\xff\xff\xff\xff\xff\xff\xff\xfc\xff\xff\xff\xaf\xff\xff\xff\xf8\xef\xff\xff\xff'
        b'\xff\xff\xff\xec\xff\xff\xff\x7f\xff\xff\xff\xf8\xf3\xff\xff\xff\xff\xff\xff\xeb\xf7\xff\xff\xff'
        b'\xff\xff\xdf\xf8\xf9\xff\xff\xff\xff\xff\xff\xed\xf7\xff\xff\xff\xff\xff\xcf\xf8\xf6\xff\xff\xff'
        b'\xff\xff\xff\x85\xf3\xff\xff\xff\xff\xff\x8f\xc8\xf7\x3f\xff\xff\xff\xff\xff\x03\xf3\xff\xff\xff'
        b'\xff\xff\x0f\x8c\xfd\x9f\xff\xff\xff\x7f\xfc\x07\xf1\xff\xff\xff\xff\xff\x0f\xa4\xd3\xcf\xff\xff'
        b'\xff\xff\xf0\x05\xfd\xff\xff\xff\xff\xfe\x1f\xec\xd1\x67\xff\xff'), 128, 64, MONO_HLSB)
