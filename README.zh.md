<h3 align="center">
Multi-Level Triton Runner(Debugging) 🔧
</h3>

<p align="center">
<a href="./doc/"><b>文档</b></a> | <a href="https://zhuanlan.zhihu.com/column/c_1940119129400013405"><b>开发文档</b></a> ｜ <a href="https://triton-runner.org"><b>🔗 triton-runner.org</b></a>
</p>

<p align="center">
<a href="README.md"><b>English</b></a> | <a><b>中文</b></a>
</p>

Triton Runner 是一个面向 [OpenAI/Triton](https://github.com/triton-lang/triton) 的多层级 runner 工具，用于调试 Triton IR，支持在多个编译阶段直接运行 GPU kernel，包括 Python Triton、Python Gluon、TTIR(Triton IR)、TTGIR(Triton GPU IR)、LLIR(LLVM IR)、PTX、cubin。该工具旨在提升 Triton 用户对编译流程的可观测性与可控性，同时降低对 Triton 源码的编译Pass pipeline的限制，从而进行性能调优和调试。

Triton Runner 兼容 Triton **v3.4.0(主要版本)**, v3.3.x, v3.2.0, v3.1.0 or v3.0.0。

Triton Runner 还提供了在 Triton v3.4.0 的1D/2D tensor调试。

## 快速安装

可以使用 pip 安装 Triton 的最新稳定[发行版](https://pypi.org/project/triton-runner/#history)。

```shell
pip install triton-runner
```

## 源码安装

```shell
git clone https://github.com/toyaix/triton-runner
cd triton-runner

pip install -e .
```

## ✨ 功能

- [一、 多层级执行](README.md#i-multi-level-runner)
- [二、 多层级调试](README.md#ii-multi-level-debugging)
- [三、 Benchmarks](README.md#iii-benchmarks)
- [四、 解决Triton Issue](README.md#iv-solving-triton-issues)


## 使用文档

以下是当前文档内容，最新版本会实时更新在[[尝试] 算子开发 ——— 知乎专栏](https://www.zhihu.com/column/c_1900572918569760497)。

[GPU调试新利器？Triton Runner使用文档(v.2.2)](https://zhuanlan.zhihu.com/p/1953369848705971938)

## [[开发文档] triton-runner ——— 知乎专栏](https://www.zhihu.com/column/c_1940119129400013405)

以下是当前文档内容，最新版本会实时更新在[知乎专栏](https://www.zhihu.com/column/c_1940119129400013405)。

[Triton Runner v0.2.0 : 支持调试，多版本支持(4b85c7a)](https://zhuanlan.zhihu.com/p/1951383935830454570)

[Triton多层级runner v0.1.5：支持缓存机制，Benchmark更友好(9c28df1)](https://zhuanlan.zhihu.com/p/1931261279072396108)

[Triton黑魔法：多层级 runner 工具(795ff3d)](https://zhuanlan.zhihu.com/p/1927486699484717368)

[Triton黑魔法：cubin runner(539d549)](https://zhuanlan.zhihu.com/p/1925826891702576935)

## 作者相关文章

[浅析 Triton 执行流程](https://zhuanlan.zhihu.com/p/712640431)

[深度剖析 Triton编译器 MatMul优化（一）—— FMA](https://zhuanlan.zhihu.com/p/1922542705797465957)

[深度剖析 Triton编译器 MatMul优化（二）—— MMA](https://zhuanlan.zhihu.com/p/1922921325296615496)

[深度剖析 Triton编译器 MatMul优化（三）—— TMA](https://zhuanlan.zhihu.com/p/1924011555437155686)
