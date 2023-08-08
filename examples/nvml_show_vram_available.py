import pynvml

GPU_to_query = 0 # Select GPU

# Modified from ChatGPT
def get_free_vram_gpu(GPU_to_query:int):
    pynvml.nvmlInit()
    handle = pynvml.nvmlDeviceGetHandleByIndex(GPU_to_query)
    mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
    free_vram_bytes = mem_info.free

    # Convert bytes to human-readable format
    def sizeof_fmt(num, suffix='B'):
        for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
            if abs(num) < 1024.0:
                return "%3.1f %s%s" % (num, unit, suffix)
            num /= 1024.0
        return "%.1f %s%s" % (num, 'Yi', suffix)

    return sizeof_fmt(free_vram_bytes)

print(get_free_vram_gpu(GPU_to_query))
