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

可以使用 pip 安装 Triton 的最新稳定[发行版](https://pypi.org/project/triton-runner/#history)。

```shell
pip install triton-runner
```

## 源码安装

```shell
git clone https://github.com/OpenMLIR/triton-runner
cd triton-runner

pip install -e .
```

## ✨ 功能

- [多层级执行](README.md#multi-level-execution)
- [TTIR 调试](README.md##ttir-debug)
- [性能测试](README.md##benchmarks)


## [[开发文档] triton-runner ——— 知乎专栏](https://www.zhihu.com/column/c_1940119129400013405)

以下是当前文档内容，最新版本会实时更新在[知乎专栏](https://www.zhihu.com/column/c_1940119129400013405)。

[Triton多层级runner v0.1.5：支持缓存机制，Benchmark更友好 (9c28df1)](https://zhuanlan.zhihu.com/p/1931261279072396108)

[Triton黑魔法：多层级 runner 工具(795ff3d)](https://zhuanlan.zhihu.com/p/1927486699484717368)

[Triton黑魔法：cubin runner(539d549)](https://zhuanlan.zhihu.com/p/1925826891702576935)

## 作者相关文章

[浅析 Triton 执行流程](https://zhuanlan.zhihu.com/p/712640431)

[深度剖析 Triton编译器 MatMul优化（一）—— FMA](https://zhuanlan.zhihu.com/p/1922542705797465957)

[深度剖析 Triton编译器 MatMul优化（二）—— MMA](https://zhuanlan.zhihu.com/p/1922921325296615496)

[深度剖析 Triton编译器 MatMul优化（三）—— TMA](https://zhuanlan.zhihu.com/p/1924011555437155686)

## ⚠️ Triton版本限制

triton-runner 兼容的 Triton 版本包括 v3.4.0（主要版本）、v3.3.x 和 v3.2.0。

## 📄 License

本项目采用 **MIT License**，详细内容请参阅 [LICENSE](./LICENSE) 文件。
