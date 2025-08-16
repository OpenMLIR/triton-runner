<h3 align="center">
Multi-Level Triton Runner Tool 🔧
</h3>

<p align="center">
<a href="./doc/"><b>Documentation</b></a> ｜ <a href="https://triton-runner.org"><b>🔗 triton-runner.org</b></a>
</p>

<p align="center">
<a ><b>English</b></a> | <a href="README.zh.md"><b>中文</b></a>
</p>

triton-runner is a lightweight, multi-level execution engine for [OpenAI/Triton](https://github.com/triton-lang/triton), designed to support IR/PTX/cubin launches in complex pass pipelines.

triton-runner is compatible with **Triton v3.4.0 (primary), v3.3.x, or v3.2.0**, and may not work with other versions.

## Quick Installation

You can install the latest stable release of Triton from pip:

```shell
pip install triton-runner
```

## Install from source

```shell
git clone https://github.com/OpenMLIR/triton-runner
cd triton-runner

pip install -e .
```

## Example

> **Note:** The following example requires an NVIDIA GPU with compute capability `sm90 (H100, H200, H20, etc.)`, `sm80 (A100, A30)`, `sm120 (RTX PRO 6000, RTX 5090, etc.)`, `sm86 (A10, RTX 3090, etc.)` or `sm75 (T4, RTX 2080, etc.)`. Please make sure to install the package before running the example.

> If your GPU does not have one of the above compute capabilities, you can use `TRITON_CACHE_DIR=$PWD/.cache` to output the Triton cache to the current directory, and then copy the corresponding cache files to your target machine.

Here's an example command that targets sm90 with Triton v3.4.0. For more target, please refer to [examples](./doc/examples_v3.4.0.md). If your Triton version is v3.3.1 or v3.3.0, please refer to [examples_v3.3.x](./doc/examples_v3.3.x.md) for example commands. If your Triton version is v3.2.0, please refer to [examples_v3.2.0](./doc/examples_v3.2.0.md) for example commands.

### sm90 (H100, H200, H20, etc.)
```shell
python examples/python_runner/matmul.py

python examples/ttir_runner/matmul.py

python examples/ttgir_runner/sm90/matmul-with-tma-v4.py

python examples/llir_runner/sm90/matmul-with-tma-v4.py

python examples/ptx_runner/sm90/matmul-with-tma-v4.py

python examples/cubin_runner/sm90/matmul-with-tma-v4.py
```

## Benchmarks

Benchmarks Referencing [TritonBench](https://github.com/pytorch-labs/tritonbench)
  - `launch_latency`: Measures kernel launch overhead.
  - `matmul`: Provides a benchmark for matrix multiplication performance.

```shell
python benchmark/launch_latency/bench.py

python benchmark/static_shape/matmul.py
```

## ⚠️ Version Compatibility

triton-runner is compatible with **Triton v3.4.0 (primary), v3.3.x, or v3.2.0**.

Compatibility with other versions of Triton is **not guaranteed** and may lead to unexpected behavior or run failures.

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](./LICENSE) file for more details.
