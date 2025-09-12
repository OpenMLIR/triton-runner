<h3 align="center">
Multi-Level Triton Runner Tool 🔧
</h3>

<p align="center">
<a href="./doc/"><b>文档</b></a> | <a href="https://zhuanlan.zhihu.com/column/c_1940119129400013405"><b>开发文档</b></a> ｜ <a href="https://triton-runner.org"><b>🔗 triton-runner.org</b></a>
</p>

<p align="center">
<a href="README.md"><b>English</b></a> | <a><b>中文</b></a>
</p>

triton-runner 是一个面向 [OpenAI/Triton](https://github.com/triton-lang/triton) 的多层级 runner 工具，用于调试 Triton IR，支持在多个编译阶段直接运行 GPU kernel，包括 ttir、ttgir、llir、ptx、cubin。该工具旨在提升 Triton 用户对编译流程的可观测性与可控性，同时降低对 Triton 源码的编译Pass pipeline的限制，从而进行性能调优和调试。

triton-runner 兼容 **Triton v3.4.0 (主要版本), v3.3.x, or v3.2.0**。

## 快速安装

You can install the latest stable release of Triton from pip:

```shell
pip install triton-runner
```

## 源码安装

```shell
git clone https://github.com/OpenMLIR/triton-runner
cd triton-runner

pip install -e .
```

## 样例

目前提供了sm90 (H100, H200, H20, etc.), sm80 (A100, A30), sm120 (RTX PRO 6000, RTX 5090, etc.), sm86 (A10, RTX 3090, etc.) or sm75 (T4, RTX 2080, etc.) 这5个[compute capability](https://developer.nvidia.com/cuda-gpus) 的示例，比如H20在Triton v.3.4.0 可以运行如下命令。

```shell
python examples/python_runner/matmul.py

python examples/ttir_runner/matmul.py

python examples/ttgir_runner/sm90/matmul-with-tma-v4.py

python examples/llir_runner/sm90/matmul-with-tma-v4.py

python examples/ptx_runner/sm90/matmul-with-tma-v4.py

python examples/cubin_runner/sm90/matmul-with-tma-v4.py
```

更多target示例，请参阅 [examples](./doc/examples_v3.4.0.md)。如果没有你的target示例，你需要使用`TRITON_CACHE_DIR=$PWD/.cache` 得到对应的源文件之后再运行。

如果你的 Triton 版本是 v3.3.1 或 v3.3.0，请参阅 [examples_v3.3.x](./doc/examples_v3.3.x.md) 获取命令。

如果你的 Triton 版本是 v3.2.0，请参阅 [examples_v3.2.0](./doc/examples_v3.2.0.md) 获取命令。

## 调试 TTIR(主分支)

支持了在Triton v3.4.0的TTIR级别的调试，如 `tt.load`、 `arith.addf`、 `tt.trans`等.

```shell
python debug_tool/ttir/01-vector_add/debug_load.py

python debug_tool/ttir/01-vector_add/debug_addf.py

python debug_tool/ttir/02-matrix_transpose/debug_2d_load.py

python debug_tool/ttir/02-matrix_transpose/debug_2d_trans.py
```

## Benchmarks

Benchmarks 参照 [TritonBench](https://github.com/pytorch-labs/tritonbench)项目

  - `launch_latency`：测量 kernel 启动的延迟开销。

  - `matmul`：用于评估矩阵乘法的性能表现。

```shell
python benchmark/launch_latency/bench.py

python benchmark/static_shape/matmul.py
```

## ⚠️ Triton版本限制

triton-runner 兼容的 Triton 版本包括 v3.4.0（主要版本）、v3.3.x 和 v3.2.0。

## 📄 License

本项目采用 **MIT License**，详细内容请参阅 [LICENSE](./LICENSE) 文件。

## 项目文档

[Triton多层级runner v0.1.5：支持缓存机制，Benchmark更友好 (9c28df1)](https://zhuanlan.zhihu.com/p/1931261279072396108)

[Triton黑魔法：多层级 runner 工具(795ff3d)](https://zhuanlan.zhihu.com/p/1927486699484717368)

[Triton黑魔法：cubin runner(539d549)](https://zhuanlan.zhihu.com/p/1925826891702576935)

## 相关文章

[深度剖析 Triton编译器 MatMul优化（三）—— TMA](https://zhuanlan.zhihu.com/p/1924011555437155686)

[深度剖析 Triton编译器 MatMul优化（二）—— MMA](https://zhuanlan.zhihu.com/p/1922921325296615496)

[深度剖析 Triton编译器 MatMul优化（一）—— FMA](https://zhuanlan.zhihu.com/p/1922542705797465957)

[浅析 Triton 执行流程](https://zhuanlan.zhihu.com/p/712640431)
