# **Semantic Kernel 入门手册**

***注意:*** 本书的内容基于 Semantic Kernel dotnet-1.16.2 and python-1.3.0 and java-1.2.0

![cover](imgs/cover.png)

随着大模型兴起，人工智能进入到 2.0 时代，与过往人工智能技术相比门槛降低了，可应用性增强，而且不在局限在数据科学的领域上，有更多不同的工种和人群参与到大模型的应用场景中。对于传统工程项目或者企业应用如何进入到大模型的领域当中呢，框架是必须的。特别对于传统项目，如何更快，低成本地接入大模型是企业所必须思考的。在大模型的元年 2023 年，开源社区有非常多的基于大模型应用的框架和解决方案，我本人比较喜欢 LangChain, BentoML, prompt flow , autogen 以及 Semantic Kernel。但纵观来说 , Semantic Kernel 更适合传统工程以及多语言体系的工程团队使用, LangChain 适合数据科学人员进行使用，至于 BenToML 适合多模型部署的场景。在 2023 年 12 月，Semantic Kernel 正式发布 1.0.1 基于 .NET 版本之际，也希望通过本手册给大家一些学习入门的方法。虽然 Semantic Kernel 还有很多的不完善的地方，但不阻碍大家学习和使用。

本手册主要围绕 .NET ，Java 以及 Python 两个版本的 Semantic Kernel 版本实现去带大家进行入门，结合 Azure OpenAI Service 给需要掌握大模型应用开发的各位进行指导。本手册会尽量跟随 Semantic Kernel 的发行版本同步更新，让大家可以掌握最新的 Semantic Kernel 技巧。以下是本手册对应的章节以及对应代码，请根据需要进行学习：



| 课程名   | 介绍   |      <center>.NET<br/>示例</center>      |  <center>Python<br/>示例</center>   |  <center>Java<br/>示例</center>   |
|----------|:----------|:-------------:|------:|------:|
| [了解大型语言模型](https://github.com/kinfey/SemanticKernelCookBook/tree/main/docs/cn/00.IntroduceLLM.md) | 认识大模型，包括 OpenAI, Azure OpenAI Service 以及 Hugging face 上的大模型 |  |  |  |
| [用 SDK 访问 Azure OpenAI Service](https://github.com/kinfey/SemanticKernelCookBook/tree/main/docs/cn/01.UsingAzureOpenAIServiceWithSDK.md)  | 使用 SDK 用最熟悉的编程语言访问 Azure OpenAI Service  | <center>[进入](https://github.com/kinfey/SemanticKernelCookBook/blob/main/notebooks/dotNET/01/dotNETSDKAOAIDemo.ipynb)</center> | <center>[进入](https://github.com/kinfey/SemanticKernelCookBook/blob/main/notebooks/python/01/PythonSDKAOAIDemo.ipynb)</center> | <center>[进入](https://github.com/kinfey/SemanticKernelCookBook/blob/main/notebooks/java/01/JavaSDKAOAIDemo.ipynb)</center> |
| [Semantic Kernel 基础](https://github.com/kinfey/SemanticKernelCookBook/tree/main/docs/cn/02.IntroduceSemanticKernel.md) | 什么是 Semantic Kernel ? 它的优点和缺点是什么？ Semantic Kernel 相关概念等  | <center>[进入](https://github.com/kinfey/SemanticKernelCookBook/blob/main/notebooks/dotNET/02/LearnSK.ipynb)</center> | <center>[进入](https://github.com/kinfey/SemanticKernelCookBook/blob/main/notebooks/python/02/LearnSK.ipynb)</center> | <center>[进入](https://github.com/kinfey/SemanticKernelCookBook/blob/main/notebooks/java/02/LearnSK.ipynb)</center> |
| [开启大模型的技能之门 - Plugins](https://github.com/kinfey/SemanticKernelCookBook/tree/main/docs/cn/03.Plugins.md) |  我们知道和大模型交流需要使用提示工程？ 对于企业的应用都有不少针对业务的提示工程和大模型交流，在 Semantic Kernel 我们把它称为 Plugins。本节我们会介绍如何使用 Semantic Kernel 的 Plugins 以及如何定义属于自己的 Plugins   |  <center>[进入](https://github.com/kinfey/SemanticKernelCookBook/blob/main/notebooks/dotNET/03/PluginWithSK.ipynb)</center>   |   <center>[进入](https://github.com/kinfey/SemanticKernelCookBook/blob/main/notebooks/python/03/PluginWithSK.ipynb)</center> |   <center>[进入](https://github.com/kinfey/SemanticKernelCookBook/blob/main/notebooks/java/03/PluginWithSK.ipynb)</center> |
| [Planner - 让大模型有规划地工作](https://github.com/kinfey/SemanticKernelCookBook/tree/main/docs/cn/04.Planner.md) | 人类完成一个工作需要按步就班，大模型也一样。 Semantic Kernel 有非常强大的计划任务规划能力 - Planner，本章我们会和大家一一细说如何定义和使用 Planner 让您的应用更具智能化 | <center>[进入](https://github.com/kinfey/SemanticKernelCookBook/blob/main/notebooks/dotNET/04/PlannerWithSK.ipynb)</center> |    <center>[进入](https://github.com/kinfey/SemanticKernelCookBook/blob/main/notebooks/python/04/PlannerWithSK.ipynb)</center> | <center>[进入](https://github.com/kinfey/SemanticKernelCookBook/blob/main/notebooks/java/04/PlannerWithSK.ipynb)</center>|
| [嵌入式的技巧 - Embeddings](https://github.com/kinfey/SemanticKernelCookBook/tree/main/docs/cn/05.Embeddings.md)  |  构建 RAG 应用是现阶段最多人使用的大模型解决方案，通过 Semantic Kernel 可以非常方便地构建 RAG 应用，本章会从最基础部分开始让大家通过 Semantic Kernel 完成 Embeddings 的工作 | <center>[进入](https://github.com/kinfey/SemanticKernelCookBook/blob/main/notebooks/dotNET/05/EmbeddingsWithSK.ipynb)</center>   |  <center>[进入](https://github.com/kinfey/SemanticKernelCookBook/blob/main/notebooks/python/05/EmbeddingsWithSK.ipynb)</center> |<center>[进入](https://github.com/kinfey/SemanticKernelCookBook/blob/main/notebooks/java/05/EmbeddingsWithSK.ipynb)</center>|
| 项目实战 | 通过三个项目实战，让大家动手真正了解 Semantic Kernel 的应用  | <center>[进入](https://github.com/kinfey/SemanticKernelCookBook/tree/main/workshop/dotNET)</center> | <center>[进入](https://github.com/kinfey/SemanticKernelCookBook/tree/main/workshop/python)</center> |<center>[进入](https://github.com/kinfey/SemanticKernelCookBook/tree/main/workshop/java)</center>|





