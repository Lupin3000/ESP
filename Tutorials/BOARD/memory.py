from gc import mem_free, mem_alloc


if __name__ == '__main__':
    print('[INFO] ESP heap RAM information')
    print(f'[INFO] Memory free {mem_free()} bytes')
    print(f'[INFO] Memory allocated {mem_alloc()} bytes')
