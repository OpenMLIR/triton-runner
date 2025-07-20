import triton
import json
from triton.backends.nvidia.driver import make_launcher, compile_module_from_src
from collections import namedtuple
from .check_utils import check_triton

_metadata = {}
_device = triton.runtime.driver.active.get_current_device()
_stream = triton.runtime.driver.active.get_current_stream(_device)


def get_cufunction(json_path, cubin_path, kernel_name):
    global _metadata
    _metadata = json.loads(open(json_path, "r").read())
    check_triton(kernel_name, _metadata, _device)
    kernel = open(cubin_path, "rb").read()
    module, function, n_regs, n_spills = triton.runtime.driver.active.utils.load_binary(
        kernel_name, kernel, _metadata["shared"], _device)
    return function


def get_grid_xyz(grid):
    assert grid is not None
    grid_size = len(grid)
    grid_0 = grid[0]
    grid_1 = grid[1] if grid_size > 1 else 1
    grid_2 = grid[2] if grid_size > 2 else 1
    return grid_0, grid_1, grid_2


def get_grid_size(grid):
    grid_0, grid_1, grid_2 = get_grid_xyz(grid)
    return grid_0 * grid_1 * grid_2


def get_compile_metadata():
    _metadata["cluster_dims"] = tuple(_metadata["cluster_dims"])
    # JSON serialization dumps the target as a dict. Restore it to a GPUTarget.
    target = _metadata["target"]
    _metadata["target"] = triton.backends.compiler.GPUTarget(target["backend"], target["arch"], target["warp_size"])
    KernelMetadata = namedtuple("KernelMetadata", sorted(list(_metadata.keys())))
    return KernelMetadata(**_metadata)


def get_backend(compile_metadata_target):
    return triton.compiler.make_backend(compile_metadata_target)


def get_packed_metadata():
    compile_metadata = get_compile_metadata()
    backend = get_backend(compile_metadata.target)
    return backend.pack_metadata(compile_metadata)


def get_global_scratch(grid):
    if _metadata["global_scratch_size"] > 0:
        alloc_size = get_grid_size(grid) * _metadata["global_scratch_size"]
        return triton.runtime._allocation._allocator(alloc_size, _metadata["global_scratch_align"], _stream)
    return None


def get_kernel_global_scratch(grid, metadata):
    if metadata.global_scratch_size > 0:
        alloc_size = get_grid_size(grid) * metadata.global_scratch_size
        return _allocation._allocator(alloc_size, metadata.global_scratch_align, _stream)
    return None


def get_mod(signature_str):
    signature = dict(enumerate(signature_str.split()))
    src = make_launcher(None, signature)
    return compile_module_from_src(src, "__triton_launcher")


def cubin_launch_config(function, signature_str, bound_args, grid):
    global_scratch = get_global_scratch(grid)
    packed_metadata = get_packed_metadata()
    launch_metadata, launch_enter_hook, launch_exit_hook = None, None, None
    launch_cooperative_grid = _metadata["launch_cooperative_grid"]
    return (get_mod(signature_str), *get_grid_xyz(grid), _stream, function, launch_cooperative_grid, global_scratch,
            packed_metadata, launch_metadata, launch_enter_hook, launch_exit_hook, bound_args)


def kernel_launch_config(kernel, signature_str, bound_args, grid):
    kernel._init_handles()
    launch_metadata = kernel.launch_metadata(grid, _stream, *bound_args)
    global_scratch = get_kernel_global_scratch(grid, kernel.metadata)
    launch_enter_hook, launch_exit_hook = None, None
    return (get_mod(signature_str), *get_grid_xyz(grid), _stream, kernel.function,
            kernel.metadata.launch_cooperative_grid, global_scratch, kernel.packed_metadata, launch_metadata,
            launch_enter_hook, launch_exit_hook, bound_args)
