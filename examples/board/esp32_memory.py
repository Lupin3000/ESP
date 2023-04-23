from uos import statvfs
from gc import mem_free, mem_alloc


def get_disc_space() -> tuple:
    """
    get current device disc space
    :return: total, free and used disc space string values as tuple
    """
    tuple_values = statvfs('/')

    string_total_size = tuple_values[1] * tuple_values[2]
    string_free_size = tuple_values[1] * tuple_values[3]
    string_used_size = string_total_size - string_free_size

    return string_total_size, string_free_size, string_used_size


if __name__ == '__main__':
    print('\n[INFO] Disk space & Memory information')
    print(f"{'Memory free' : < 18} : {mem_free()} bytes")
    print(f"{'Memory allocated' : < 18} : {mem_alloc()} bytes")
    str_total, str_free, str_used = get_disc_space()
    print(f"{'Total disc space' : < 18} : {str_total} bytes")
    print(f"{'Free disc space' : < 18} : {str_free} bytes")
    print(f"{'Used disc space' : < 18} : {str_used} bytes\n")
