from gc import mem_free, mem_alloc


print('[INFO] ESP heap RAM information')
print(f'[INFO] Memory free {mem_free()} bytes')
print(f'[INFO] Memory allocated {mem_alloc()} bytes')
