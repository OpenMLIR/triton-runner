import warnings
import triton

_metadata = {}


def colored_warning(message, category, filename, lineno, file=None, line=None):
    if file is None:
        import sys
        file = sys.stderr
    formatted = f"\033[1m\033[93m{category.__name__}: {message} ({filename}:{lineno})\033[0m\n"
    file.write(formatted)


warnings.showwarning = colored_warning


def check_kernel_name(kernel_name):
    if _metadata['name'] != kernel_name:
        warnings.warn(f"This kernel name {kernel_name} is different with metadata {_metadata['name']}")


def check_triton_version():
    kernel_version = _metadata['triton_version']
    installed_version = triton.__version__
    if kernel_version != installed_version:
        warnings.warn(f"This kernel Triton v{kernel_version} is different with intstalled v{installed_version}")
    if installed_version not in ["3.3.0", "3.3.1"]:
        warnings.warn("This runner is only support Triton v3.3.x.")


def check_cuda_arch_with_capability(kernel_arch, target_arch):
    if kernel_arch != target_arch:
        warnings.warn(f"This kernel capability={kernel_arch} is different with device capability={target_arch}")


def check_cuda_arch(device):
    target = triton.runtime.driver.active.get_current_target()
    kernel_arch = _metadata["target"]["arch"]
    check_cuda_arch_with_capability(target.arch, kernel_arch)


def check_triton(kernel_name, metadata, device):
    global _metadata
    _metadata = metadata
    check_kernel_name(kernel_name)
    check_triton_version()
    check_cuda_arch(device)
