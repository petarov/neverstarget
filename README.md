<p align="left">
<img src="assets/neverstarget.png" alt="Exploding star image" width="180"/>
</p>

neverstarget
==============

All of your starred Github projects in one list. You never check on them anyway.

# How to use

1. Create a new, empty repository on GitHub under your **user** account (not an orga).
2. Copy this repo without its history and push it to yours:

   ```sh
   git clone --depth 1 https://github.com/petarov/neverstarget.git my-stars
   cd my-stars
   rm -rf .git
   git init -b main
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/<your-login>/<your-repo>.git
   git push -u origin main
   ```

3. Make sure GitHub Actions is enabled, i.e., open the repo's **Actions** tab and enable workflows.
4. The push to `main` starts the **Update README with star lists** workflow. You can also run it any time from **Actions/Run workflow**.
5. The workflow regenerates `README.md` with your public star lists and commits it back to `main`.

# Starred

## 🖲AI (80)

LLMs, ML, RL, etc.

- **[huggingface/deep-rl-class](https://github.com/huggingface/deep-rl-class)** — This repo contains the Hugging Face Deep Reinforcement Learning Course.
- **[tinygrad/tinygrad](https://github.com/tinygrad/tinygrad)** — You like pytorch? You like micrograd? You love tinygrad! ❤️
- **[openai/gym](https://github.com/openai/gym)** — `(archived)` A toolkit for developing and comparing reinforcement learning algorithms.
- **[tensorflow/models](https://github.com/tensorflow/models)** — Models and examples built with TensorFlow
- **[eriklindernoren/ML-From-Scratch](https://github.com/eriklindernoren/ML-From-Scratch)** — Machine Learning From Scratch. Bare bones NumPy implementations of machine learning models and algorithms with a focus on accessibility. Aims to cover everything from linear regression to deep learning.
- **[jantic/DeOldify](https://github.com/jantic/DeOldify)** — `(archived)` A Deep Learning based project for colorizing and restoring old images (and video!)
- **[flairNLP/flair](https://github.com/flairNLP/flair)** — A very simple framework for state-of-the-art Natural Language Processing (NLP)
- **[rushter/MLAlgorithms](https://github.com/rushter/MLAlgorithms)** — Minimal and clean examples of machine learning algorithms implementations
- **[nidhaloff/igel](https://github.com/nidhaloff/igel)** — a delightful machine learning tool that allows you to train, test, and use models without writing code
- **[postgresml/postgresml](https://github.com/postgresml/postgresml)** — Postgres with GPUs for ML/AI apps.
- **[apple-aiml-research/ml-stable-diffusion](https://github.com/apple-aiml-research/ml-stable-diffusion)** — Stable Diffusion with Core ML on Apple Silicon
- **[huggingface/transformers.js](https://github.com/huggingface/transformers.js)** — State-of-the-art Machine Learning for the web. Run 🤗 Transformers directly in your browser, with no need for a server!
- **[meta-llama/llama](https://github.com/meta-llama/llama)** — Inference code for Llama models
- **[mlc-ai/mlc-llm](https://github.com/mlc-ai/mlc-llm)** — Universal LLM Deployment Engine with ML Compilation
- **[bigscience-workshop/petals](https://github.com/bigscience-workshop/petals)** — 🌸 Run LLMs at home, BitTorrent-style. Fine-tuning and inference up to 10x faster than offloading
- **[ollama/ollama](https://github.com/ollama/ollama)** — Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.
- **[Nixtla/statsforecast](https://github.com/Nixtla/statsforecast)** — Lightning ⚡️ fast forecasting with statistical and econometric models.
- **[abi/screenshot-to-code](https://github.com/abi/screenshot-to-code)** — Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue)
- **[lllyasviel/Fooocus](https://github.com/lllyasviel/Fooocus)** — Focus on prompting and generating
- **[agno-agi/agno](https://github.com/agno-agi/agno)** — The self-managing agent platform
- **[karpathy/llm.c](https://github.com/karpathy/llm.c)** — LLM training in simple, raw C/CUDA
- **[khoj-ai/khoj](https://github.com/khoj-ai/khoj)** — Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.
- **[open-webui/open-webui](https://github.com/open-webui/open-webui)** — User-friendly AI Interface (Supports Ollama, OpenAI API, ...)
- **[microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)** — 21 Lessons, Get Started Building with Generative AI
- **[f/prompts.chat](https://github.com/f/prompts.chat)** — f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.
- **[Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)** — Stop renting your intelligence. Own it with AnythingLLM. Everything you need for a powerful local-first agent experience
- **[janhq/jan](https://github.com/janhq/jan)** — Jan is an open source alternative to ChatGPT that runs 100% offline on your computer.
- **[stanfordnlp/CoreNLP](https://github.com/stanfordnlp/CoreNLP)** — CoreNLP: A Java suite of core NLP tools for tokenization, sentence segmentation, NER, parsing, coreference, sentiment analysis, etc.
- **[microsoft/BitNet](https://github.com/microsoft/BitNet)** — Official inference framework for 1-bit LLMs
- **[huggingface/smollm](https://github.com/huggingface/smollm)** — Everything about the SmolLM and SmolVLM family of models
- **[langchain4j/langchain4j](https://github.com/langchain4j/langchain4j)** — LangChain4j is an idiomatic, open-source Java library for building LLM-powered applications on the JVM. It offers a unified API over popular LLM providers and vector stores, and makes implementing tool calling (including MCP support), agents and RAG easy. It integrates seamlessly with enterprise Java frameworks like Quarkus and Spring Boot.
- **[sashabaranov/go-openai](https://github.com/sashabaranov/go-openai)** — OpenAI, GPT 6.1, GPT-Image-2, Whisper API clients for Go. Zero-dependency.
- **[DataTalksClub/machine-learning-zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp)** — Learn ML engineering for free in 4 months! Register here 👇🏼
- **[deepseek-ai/DeepSeek-LLM](https://github.com/deepseek-ai/DeepSeek-LLM)** — DeepSeek LLM: Let there be answers
- **[openai/whisper](https://github.com/openai/whisper)** — Robust Speech Recognition via Large-Scale Weak Supervision
- **[lmstudio-ai/lms](https://github.com/lmstudio-ai/lms)** — LM Studio CLI
- **[unslothai/unsloth](https://github.com/unslothai/unsloth)** — Local UI to run and train LLMs and diffusion models. Supports GGUF, MLX, Qwen3.8, DeepSeek-V4.1, MiniMax-H3, Gemma 4, FLUX and more.
- **[nari-labs/dia](https://github.com/nari-labs/dia)** — A TTS model capable of generating ultra-realistic dialogue in one pass.
- **[voideditor/void](https://github.com/voideditor/void)** — `(archived)`
- **[devoxx/DevoxxGenieIDEAPlugin](https://github.com/devoxx/DevoxxGenieIDEAPlugin)** — DevoxxGenie is an agentic plugin for IntelliJ IDEA that uses local LLM's (Ollama, LMStudio, GPT4All, Jan and Llama.cpp) and Cloud based LLMs to help review, test, explain your project code. Latest version now also supports Spec Driven Development with CLI Runners.
- **[WasmEdge/WasmEdge](https://github.com/WasmEdge/WasmEdge)** — WasmEdge is a lightweight, high-performance, and extensible WebAssembly runtime for cloud native, edge, and decentralized applications. It powers serverless apps, embedded functions, microservices, smart contracts, and IoT devices.
- **[microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners)** — 12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all
- **[omarsar/nlp_overview](https://github.com/omarsar/nlp_overview)** — Overview of Modern Deep Learning Techniques Applied to Natural Language Processing
- **[adbar/German-NLP](https://github.com/adbar/German-NLP)** — Curated list of open-access/open-source/off-the-shelf resources and tools developed with a particular focus on German
- **[oracle/tribuo](https://github.com/oracle/tribuo)** — Tribuo - A Java machine learning library
- **[tobiassteidle/Reinforcement-Learning](https://github.com/tobiassteidle/Reinforcement-Learning)** — Solutions for different Reinforcement Learning environments
- **[facebookresearch/audiocraft](https://github.com/facebookresearch/audiocraft)** — Audiocraft is a library for audio processing and generation with deep learning. It features the state-of-the-art EnCodec audio compressor / tokenizer, along with MusicGen, a simple and controllable music generation LM with textual and melodic conditioning.
- **[deeplearning4j/deeplearning4j](https://github.com/deeplearning4j/deeplearning4j)** — Suite of tools for deploying and training deep learning models using the JVM. Highlights include model import for keras, tensorflow, and onnx/pytorch, a modular and tiny c++ library for running math code and a java based math library on top of the core c++ library. Also includes samediff: a pytorch/tensorflow like library for running deep learn...
- **[zotroneneis/machine_learning_basics](https://github.com/zotroneneis/machine_learning_basics)** — Plain python implementations of basic machine learning algorithms
- **[googlecreativelab/teachable-machine-v1](https://github.com/googlecreativelab/teachable-machine-v1)** — `(archived)` Explore how machine learning works, live in the browser. No coding required.
- **[BrainJS/brain.js](https://github.com/BrainJS/brain.js)** — 🤖 GPU accelerated Neural networks in JavaScript for Browsers and Node.js
- **[PracticumAI/getting_started](https://github.com/PracticumAI/getting_started)** — Introduction to Artificial Intelligence, PracticumAI, and the tools we will use in the course
- **[exo-explore/exo](https://github.com/exo-explore/exo)** — Run frontier AI locally.
- **[tmc/langchaingo](https://github.com/tmc/langchaingo)** — LangChain for Go, the easiest way to write LLM-based programs in Go
- **[apple-aiml-research/ml-sharp](https://github.com/apple-aiml-research/ml-sharp)** — Sharp Monocular View Synthesis in Less Than a Second
- **[antirez/voxtral.c](https://github.com/antirez/voxtral.c)** — Pure C inference of Mistral Voxtral Realtime 4B speech to text model
- **[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw)** — Fast, small, and fully autonomous AI personal assistant infrastructure, any OS, any platform — deploy anywhere, swap anything 🦀
- **[mgechev/skillgrade](https://github.com/mgechev/skillgrade)** — "Unit tests" for your agent skills
- **[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)** — Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.
- **[Aider-AI/aider](https://github.com/Aider-AI/aider)** — aider is AI pair programming in your terminal
- **[karpathy/autoresearch](https://github.com/karpathy/autoresearch)** — AI agents running research on single-GPU nanochat training automatically
- **[stanford-scs/jai](https://github.com/stanford-scs/jai)** — Jail your AI agent
- **[primaprashant/awesome-voice-typing](https://github.com/primaprashant/awesome-voice-typing)** — Curated list of open-source speech-to-text and voice typing tools for Linux, macOS, Windows, Android, and iOS. Offline, local, and cloud.
- **[antirez/ds4](https://github.com/antirez/ds4)** — DeepSeek 4 Flash and PRO local inference engine for Metal, CUDA and ROCm
- **[shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)** — from vibe coding to agentic engineering - practice makes claude perfect
- **[AlexsJones/llmfit](https://github.com/AlexsJones/llmfit)** — Hundreds of models & providers. One command to find what runs on your hardware.
- **[ggozad/oterm](https://github.com/ggozad/oterm)** — the terminal client for LLMs
- **[odysseus-dev/odysseus](https://github.com/odysseus-dev/odysseus)** — Self-hosted AI workspace.
- **[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)** — AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary
- **[Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)** — The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. The fastest local inference engine in the world.
- **[ai-job-search-dev/ai-job-search](https://github.com/ai-job-search-dev/ai-job-search)** — The job search that runs on your machine. AI job application framework built on Claude Code: evaluate postings, tailor CVs, write cover letters, prep interviews. Fork it and own it.
- **[earendil-works/pi](https://github.com/earendil-works/pi)** — AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI
- **[yc-software/qm](https://github.com/yc-software/qm)** — Multiplayer agent harness for teams
- **[block/buzz](https://github.com/block/buzz)** — A hive mind communication platform
- **[microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners)** — 12 Weeks, 24 Lessons, AI for All!
- **[drumih/turbo-fieldfare](https://github.com/drumih/turbo-fieldfare)** — Gemma 4 26B-A4B inference in ~2 GB of RAM on any M-series MacBook
- **[firelex/jeff](https://github.com/firelex/jeff)** — Millisecond decisions, any domain: a 0.8B open "System 1" model that picks between your options with calibrated probabilities. One base, swappable LoRA adapters, on your own hardware.
- **[storytold/craft-anything](https://github.com/storytold/craft-anything)** — Craft Anything: understand how any software works, and craft your own.
- **[can1357/oh-my-pi](https://github.com/can1357/oh-my-pi)** — ⌥ Coding agent with the IDE wired in. Built by Stencil Labs.
- **[0cv/herdr-mobile-relay](https://github.com/0cv/herdr-mobile-relay)** — Approve and monitor Herdr agents remotely from your phone, a mobile web app for Android/iOS smartphones with push notifications, QR setup, and multi-computer relays over Cloudflare, WebRTC or Tailscale connections.

## 🖥️ desktop/cli-apps (52)

Useful apps or extensions to run on the desktop

- **[fengtan/ldap-explorer](https://github.com/fengtan/ldap-explorer)** — LDAP client for VS Code
- **[cooperspencer/gickup](https://github.com/cooperspencer/gickup)**
- **[jesseduffield/lazydocker](https://github.com/jesseduffield/lazydocker)** — The lazier way to manage everything docker
- **[quackduck/devzat](https://github.com/quackduck/devzat)** — The devs are over here at devzat, chat over SSH!
- **[nvbn/thefuck](https://github.com/nvbn/thefuck)** — Magnificent app which corrects your previous console command.
- **[denizsafak/abogen](https://github.com/denizsafak/abogen)** — Generate audiobooks from EPUBs, PDFs and text with synchronized captions.
- **[permissionlesstech/bitchat](https://github.com/permissionlesstech/bitchat)** — bluetooth mesh chat, IRC vibes
- **[buddhi1980/mandelbulber2](https://github.com/buddhi1980/mandelbulber2)** — Official repository for Mandelbulber v2
- **[bnanes/shrink-pdf](https://github.com/bnanes/shrink-pdf)** — Reduce PDF file size by applying jpeg compression to embedded images
- **[cubicbyte/reddit-account-generator](https://github.com/cubicbyte/reddit-account-generator)** — Automatically generate reddit accounts
- **[smallstep/cli](https://github.com/smallstep/cli)** — 🧰 A zero trust swiss army knife for working with X509, OAuth, JWT, OATH OTP, etc.
- **[syncthing/syncthing](https://github.com/syncthing/syncthing)** — Open Source Continuous File Synchronization
- **[Col-E/Recaf](https://github.com/Col-E/Recaf)** — The modern Java bytecode editor
- **[WerWolv/ImHex](https://github.com/WerWolv/ImHex)** — 🔍 A Hex Editor for Reverse Engineers, Programmers and people who value their retinas when working at 3 AM.
- **[SVG-Edit/svgedit](https://github.com/SVG-Edit/svgedit)** — Powerful SVG-Editor for your browser
- **[maildev/maildev](https://github.com/maildev/maildev)** — :mailbox: SMTP Server + Web Interface for viewing and testing emails during development.
- **[nidhaloff/igel](https://github.com/nidhaloff/igel)** — a delightful machine learning tool that allows you to train, test, and use models without writing code
- **[muesli/duf](https://github.com/muesli/duf)** — Disk Usage/Free Utility - a better 'df' alternative
- **[rylio/ytdl](https://github.com/rylio/ytdl)** — `(archived)` YouTube download library and CLI written in Go
- **[certnanny/sscep](https://github.com/certnanny/sscep)** — SSCEP is a command line client for the SCEP protocol
- **[junegunn/fzf](https://github.com/junegunn/fzf)** — :cherry_blossom: A command-line fuzzy finder
- **[imsnif/bandwhich](https://github.com/imsnif/bandwhich)** — Terminal bandwidth utilization tool
- **[tomnomnom/assetfinder](https://github.com/tomnomnom/assetfinder)** — Find domains and subdomains related to a given domain
- **[wtfutil/wtf](https://github.com/wtfutil/wtf)** — The personal information dashboard for your terminal
- **[MontFerret/ferret](https://github.com/MontFerret/ferret)** — Declarative data automation language and Go runtime for structured extraction workflows.
- **[johnfactotum/foliate](https://github.com/johnfactotum/foliate)** — Read e-books in style
- **[square/certigo](https://github.com/square/certigo)** — A utility to examine and validate certificates in a variety of formats
- **[sharkdp/bat](https://github.com/sharkdp/bat)** — A cat(1) clone with wings.
- **[restic/restic](https://github.com/restic/restic)** — Fast, secure, efficient backup program
- **[dinedal/textql](https://github.com/dinedal/textql)** — Execute SQL against structured text like CSV or TSV
- **[JoeDog/siege](https://github.com/JoeDog/siege)** — Siege is an http load tester and benchmarking utility
- **[brunodev85/winlator](https://github.com/brunodev85/winlator)** — Android application for running Windows applications with Wine and Box86/Box64
- **[malmeloo/FindMy.py](https://github.com/malmeloo/FindMy.py)** — 🍏 + 🎯 + 🐍 = Query Apple's FindMy Network with Python!
- **[rclone/rclone](https://github.com/rclone/rclone)** — "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files
- **[nukeop/nuclear](https://github.com/nukeop/nuclear)** — Streaming music player that finds free music for you
- **[IrosTheBeggar/mStream](https://github.com/IrosTheBeggar/mStream)** — The easiest music streaming server available
- **[ExistentialAudio/BlackHole](https://github.com/ExistentialAudio/BlackHole)** — BlackHole is a modern macOS audio loopback driver that allows applications to pass audio to other applications with zero additional latency.
- **[cryptomator/cryptomator](https://github.com/cryptomator/cryptomator)** — Cryptomator for Windows, macOS, and Linux: Secure client-side encryption for your cloud storage, ensuring privacy and control over your data.
- **[klaudiosinani/taskbook](https://github.com/klaudiosinani/taskbook)** — Tasks, boards & notes for the command-line habitat
- **[postgrespro/mamonsu](https://github.com/postgrespro/mamonsu)**
- **[fish-shell/fish-shell](https://github.com/fish-shell/fish-shell)** — The user-friendly command line shell.
- **[xo/usql](https://github.com/xo/usql)** — Universal command-line interface for SQL databases
- **[libfuse/sshfs](https://github.com/libfuse/sshfs)** — A network filesystem client to connect to SSH servers
- **[arduino/arduino-ide](https://github.com/arduino/arduino-ide)** — Arduino IDE 2.x
- **[molstar/VSCoding-Sequence](https://github.com/molstar/VSCoding-Sequence)** — VSCode Extension for interactively visualising protein structure data in the editor
- **[peco/peco](https://github.com/peco/peco)** — Simplistic interactive filtering tool
- **[tmarice/fast_masked_mail_creator](https://github.com/tmarice/fast_masked_mail_creator)** — Fast Masked Mail Creator
- **[walterlow/freecut](https://github.com/walterlow/freecut)** — FreeCut is a professional-grade video editor that runs entirely in your browser. Professional video editing, zero installation. Create stunning videos with multi-track editing, keyframe animations, real-time preview, and high-quality exports.
- **[matthart1983/netwatch](https://github.com/matthart1983/netwatch)** — Network diagnostics in your terminal. Inspect traffic, connections and network behaviour. Built with Rust.
- **[jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac)** —  This project is dedicated to collecting high-quality macOS software and organizing them systematically by different categories for easy search and use.
- **[storytold/photocraft](https://github.com/storytold/photocraft)** — PhotoCraft: An open-source photo editor written from scratch in pure Rust
- **[santinic/how2](https://github.com/santinic/how2)** — AI for the Command Line

## 🛠️ dev-tools (64)

Tools and frameworks - language independent

- **[semgrep/semgrep](https://github.com/semgrep/semgrep)** — Lightweight static analysis for many languages. Find bug variants with patterns that look like source code.
- **[Wilfred/difftastic](https://github.com/Wilfred/difftastic)** — a structural diff that understands syntax 🟥🟩
- **[sinclairtarget/git-who](https://github.com/sinclairtarget/git-who)** — Git blame for file trees
- **[tauri-apps/tauri](https://github.com/tauri-apps/tauri)** — Build smaller, faster, and more secure desktop and mobile applications with a web frontend.
- **[xataio/pgroll](https://github.com/xataio/pgroll)** — PostgreSQL zero-downtime migrations made easy
- **[microsoft/garnet](https://github.com/microsoft/garnet)** — Garnet is a remote cache-store from Microsoft Research that offers strong performance (throughput and latency), scalability, storage, recovery, cluster sharding, key migration, and replication features. Garnet can work with existing Redis clients.
- **[nats-io/nats-server](https://github.com/nats-io/nats-server)** — High-Performance server for NATS.io, the cloud and edge native messaging system.
- **[pocket-id/pocket-id](https://github.com/pocket-id/pocket-id)** — The most user-friendly OpenID Connect Certified™ and OAuth 2.0 provider that lets users sign in to your applications with passkeys.
- **[mahmoud/boltons](https://github.com/mahmoud/boltons)** — 🔩 Like builtins, but boltons. 250+ constructs, recipes, and snippets which extend (and rely on nothing but) the Python standard library. Nothing like Michael Bolton.
- **[sb2nov/resume](https://github.com/sb2nov/resume)** — Software developer resume in Latex
- **[sigstore/gitsign](https://github.com/sigstore/gitsign)** — Keyless Git signing using Sigstore
- **[ax/apk.sh](https://github.com/ax/apk.sh)** — Makes reverse engineering Android apps easier, automating repetitive tasks like pulling, decoding, rebuilding and patching an APK.
- **[charmbracelet/gum](https://github.com/charmbracelet/gum)** — A tool for glamorous shell scripts 🎀
- **[shadow/shadow](https://github.com/shadow/shadow)** — Shadow is a discrete-event network simulator that directly executes real application code, enabling you to simulate distributed systems with thousands of network-connected processes in realistic and scalable private network experiments using your laptop, desktop, or server running Linux.
- **[Budibase/budibase](https://github.com/Budibase/budibase)** — AI agents, automations and apps that run your operations. Model agnostic.
- **[pocketbase/pocketbase](https://github.com/pocketbase/pocketbase)** — `(archived)` Open Source realtime backend in 1 file
- **[skanaar/nomnoml](https://github.com/skanaar/nomnoml)** — The sassy UML diagram renderer
- **[indygreg/apple-platform-rs](https://github.com/indygreg/apple-platform-rs)** — Rust crates supporting Apple platform development
- **[WasmEdge/WasmEdge](https://github.com/WasmEdge/WasmEdge)** — WasmEdge is a lightweight, high-performance, and extensible WebAssembly runtime for cloud native, edge, and decentralized applications. It powers serverless apps, embedded functions, microservices, smart contracts, and IoT devices.
- **[google/flatbuffers](https://github.com/google/flatbuffers)** — FlatBuffers: Memory Efficient Serialization Library
- **[Col-E/Recaf](https://github.com/Col-E/Recaf)** — The modern Java bytecode editor
- **[grafana/k6](https://github.com/grafana/k6)** — A modern load testing tool, using Go and JavaScript
- **[maildev/maildev](https://github.com/maildev/maildev)** — :mailbox: SMTP Server + Web Interface for viewing and testing emails during development.
- **[mike-neck/graalvm-native-image-plugin](https://github.com/mike-neck/graalvm-native-image-plugin)** — A Gradle plugin which creates a native executable via GraalVM's native-image. This is a thin wrapper of the native-image command.
- **[brianvoe/gofakeit](https://github.com/brianvoe/gofakeit)** — Random fake data generator written in go
- **[Impedimenta/Suitcase](https://github.com/Impedimenta/Suitcase)** — A flexible command line tool for instantly deploying user interfaces for simple commands and scripts.
- **[public-api-lists/public-api-lists](https://github.com/public-api-lists/public-api-lists)** — A curated list of free public APIs — searchable, community-maintained, with a free JSON API.
- **[hybridgroup/gobot](https://github.com/hybridgroup/gobot)** — Golang framework for robotics, drones, and the Internet of Things (IoT)
- **[JoeDog/siege](https://github.com/JoeDog/siege)** — Siege is an http load tester and benchmarking utility
- **[RandyGaul/cute_headers](https://github.com/RandyGaul/cute_headers)** — Collection of cross-platform one-file C/C++ libraries with no dependencies, primarily used for games
- **[zxing/zxing](https://github.com/zxing/zxing)** — ZXing ("Zebra Crossing") barcode scanning library for Java, Android
- **[apple/pkl](https://github.com/apple/pkl)** — A configuration as code language with rich validation and tooling.
- **[nothings/stb](https://github.com/nothings/stb)** — stb single-file public domain libraries for C/C++
- **[antirez/sds](https://github.com/antirez/sds)** — Simple Dynamic Strings library for C
- **[troydhanson/uthash](https://github.com/troydhanson/uthash)** — C macros for hash tables and more
- **[srdja/Collections-C](https://github.com/srdja/Collections-C)** — A library of generic data structures for the C language.
- **[mxschmitt/playwright-go](https://github.com/mxschmitt/playwright-go)** — Playwright for Go a browser automation library to control Chromium, Firefox and WebKit with a single API.
- **[amachanic/sp_whoisactive](https://github.com/amachanic/sp_whoisactive)** — sp_whoisactive
- **[cloudwego/goref](https://github.com/cloudwego/goref)** — Go heap object reference analysis tool
- **[xo/usql](https://github.com/xo/usql)** — Universal command-line interface for SQL databases
- **[libfuse/sshfs](https://github.com/libfuse/sshfs)** — A network filesystem client to connect to SSH servers
- **[psviderski/unregistry](https://github.com/psviderski/unregistry)** — Push docker images directly to remote servers without an external registry
- **[mountain-loop/yaak](https://github.com/mountain-loop/yaak)** — The most intuitive desktop API client. Organize and execute REST, GraphQL, WebSockets, Server Sent Events, and gRPC 🦬
- **[woodpecker-ci/woodpecker](https://github.com/woodpecker-ci/woodpecker)** — Woodpecker is a simple, yet powerful CI/CD engine with great extensibility.
- **[d2lang/d2](https://github.com/d2lang/d2)** — D2 is a modern diagram scripting language that turns text to diagrams.
- **[skylot/jadx](https://github.com/skylot/jadx)** — Dex to Java decompiler
- **[benbjohnson/litestream](https://github.com/benbjohnson/litestream)** — Streaming replication for SQLite.
- **[svg/svgo](https://github.com/svg/svgo)** — SVG Optimizer for Node.js and CLI. ⚙️
- **[piercefreeman/autopg](https://github.com/piercefreeman/autopg)** — 🐘 Auto-optimizations for Postgres
- **[c3lang/c3c](https://github.com/c3lang/c3c)** — Compiler for the C3 language
- **[community-scripts/ProxmoxVE](https://github.com/community-scripts/ProxmoxVE)** — Proxmox VE Helper-Scripts (Community Edition)
- **[gradle/gradle-profiler](https://github.com/gradle/gradle-profiler)** — A tool for gathering profiling and benchmarking information for Gradle builds
- **[NikolayS/rpg](https://github.com/NikolayS/rpg)** — rpg — modern Postgres terminal written in Rust. psql-compatible, with built-in DBA diagnostics and AI assistant
- **[casey/just](https://github.com/casey/just)** — 🤖 Just a command runner
- **[wojtczyk/trust](https://github.com/wojtczyk/trust)** — TRUST – Coding Rust like it's 1989
- **[axllent/mailpit](https://github.com/axllent/mailpit)** — An email and SMTP testing tool with API for developers
- **[modem-dev/hunk](https://github.com/modem-dev/hunk)** — Review-first terminal diff viewer for agentic coders
- **[proto-tap/sql-tap](https://github.com/proto-tap/sql-tap)** — Watch SQL traffic in real-time with a TUI
- **[pgdogdev/pgdog](https://github.com/pgdogdev/pgdog)** — PostgreSQL connection pooler, load balancer and database sharder.
- **[royalbhati/sqltoerdiagram](https://github.com/royalbhati/sqltoerdiagram)** — ER diagram generator. Paste CREATE TABLE statements and get a clean, interactive ERD — runs 100% in your browser, nothing uploaded
- **[checkmake/checkmake](https://github.com/checkmake/checkmake)** — Linter/analyzer for Makefiles
- **[libredb/libredb-studio](https://github.com/libredb/libredb-studio)** — One browser tab for PostgreSQL, MySQL, Oracle, SQL Server, MongoDB, Redis, SQLite, Couchbase, ClickHouse, Druid, DuckDB, Turso and more. An open-source SQL IDE with SSO, audit trail and AI-assisted queries MIT licensed, with nothing held back behind an enterprise wall.
- **[lysyi3m/macos-terminal-themes](https://github.com/lysyi3m/macos-terminal-themes)** — Color schemes for default macOS Terminal.app
- **[usebruno/bruno](https://github.com/usebruno/bruno)** — Opensource IDE For Exploring and Testing API's (lightweight alternative to Postman/Insomnia)

## 🕹️ gfx-&-game-dev (95)

Various gamedev libs, frameworks or complete games

- **[jakecoffman/cp](https://github.com/jakecoffman/cp)** — A pure Go physics library with no dependencies. Unofficial Chipmunk2D port.
- **[yoshisuga/MAME4iOS](https://github.com/yoshisuga/MAME4iOS)** — Multiple Arcade Machine Emulator for iOS, iPadOS, tvOS, macOS (Catalyst)
- **[CharlesPikachu/Games](https://github.com/CharlesPikachu/Games)** — Games: Create interesting games in pure python.
- **[latitudegames/AIDungeon](https://github.com/latitudegames/AIDungeon)** — `(archived)` Infinite adventures await!
- **[asciimoo/drawille](https://github.com/asciimoo/drawille)** — Pixel graphics in terminal with unicode braille characters
- **[kitao/pyxel](https://github.com/kitao/pyxel)** — A retro game engine for Python
- **[hajimehoshi/ebiten](https://github.com/hajimehoshi/ebiten)** — A dead simple 2D game engine for Go
- **[EngoEngine/engo](https://github.com/EngoEngine/engo)** — Engo is an open-source 2D game engine written in Go.
- **[go-p5/p5](https://github.com/go-p5/p5)** — `(archived)` p5 is a simple package that provides primitives resembling the ones exposed by p5js.org
- **[m110/airplanes](https://github.com/m110/airplanes)** — A 2D shoot 'em up game made with Go, Ebitengine, and donburi. Featuring ECS (Entity Component System).
- **[rtrussell/BBCSDL](https://github.com/rtrussell/BBCSDL)** — BBC BASIC for SDL 2.0: for Windows, Linux (86), MacOS, Raspberry Pi, Android and iOS.
- **[Trilarion/opensourcegames](https://github.com/Trilarion/opensourcegames)** — Technical infos of open source games.
- **[radek-sprta/awesome-game-remakes](https://github.com/radek-sprta/awesome-game-remakes)** — Actively maintained open-source game remakes.
- **[ebitenui/ebitenui](https://github.com/ebitenui/ebitenui)** — User interface engine and widget library for Ebitengine
- **[godot-escoria/escoria-demo-game](https://github.com/godot-escoria/escoria-demo-game)** — Game example for the point'n'click adventure framework Escoria
- **[sedyh/awesome-ebitengine](https://github.com/sedyh/awesome-ebitengine)** — A curated list of awesome Ebitengine frameworks, libraries and software
- **[g3n/engine](https://github.com/g3n/engine)** — Go 3D Game Engine (http://g3n.rocks)
- **[olivergreening/gameoff-2023](https://github.com/olivergreening/gameoff-2023)**
- **[quasilyte/roboden-game](https://github.com/quasilyte/roboden-game)** — An indirect control real-time strategy game about robot colonies
- **[straker/kontra](https://github.com/straker/kontra)** — A lightweight JavaScript gaming micro-library, optimized for js13kGames.
- **[Kavex/GameDev-Resources](https://github.com/Kavex/GameDev-Resources)** — `(archived)` :video_game: :game_die: A wonderful list of Game Development resources.
- **[00-Evan/shattered-pixel-dungeon](https://github.com/00-Evan/shattered-pixel-dungeon)** — Shattered Pixel Dungeon is an open-source traditional roguelike dungeon crawler with randomized levels and enemies, and hundreds of items to collect and use. It's based on the source code of Pixel Dungeon, by Watabou.
- **[vcmi/vcmi](https://github.com/vcmi/vcmi)** — Open-source engine for Heroes of Might and Magic III
- **[deavid/unhaunter](https://github.com/deavid/unhaunter)** — Terror Game about ghosts
- **[oakmound/oak](https://github.com/oakmound/oak)** — A pure Go game engine
- **[gopxl/pixel](https://github.com/gopxl/pixel)** — A hand-crafted 2D game library in Go.
- **[s-macke/VoxelSpace](https://github.com/s-macke/VoxelSpace)** — Terrain rendering algorithm in less than 20 lines of code
- **[JannisX11/blockbench](https://github.com/JannisX11/blockbench)** — Blockbench - A low poly 3D model editor
- **[maurymarkowitz/101-BASIC-Computer-Games](https://github.com/maurymarkowitz/101-BASIC-Computer-Games)** — Type-in programs from the original 101 BASIC Computer Games, in their original DEC and Dartmouth dialects. No, this is *not* the same as BASIC Computer Games.
- **[deepnight/ldtk](https://github.com/deepnight/ldtk)** — Modern, lightweight and efficient 2D level editor
- **[carlini/printf-tac-toe](https://github.com/carlini/printf-tac-toe)** — tic-tac-toe in a single call to printf
- **[calebwin/stdg](https://github.com/calebwin/stdg)** — 2D graphics in any programming language with just print statements
- **[shader-park/shader-park-core](https://github.com/shader-park/shader-park-core)** — A JavaScript library for creating real-time 2D and 3D shaders. JS -> Shader. https://shaderpark.com/ https://twitter.com/shaderpark
- **[bladecoder/bladecoder-adventure-engine](https://github.com/bladecoder/bladecoder-adventure-engine)** — Classic point and click adventure game engine and editor
- **[amueller/word_cloud](https://github.com/amueller/word_cloud)** — A little word cloud generator in Python
- **[Mukosame/Anime2Sketch](https://github.com/Mukosame/Anime2Sketch)** — A sketch extractor for anime/illustration.
- **[TencentARC/GFPGAN](https://github.com/TencentARC/GFPGAN)** — GFPGAN aims at developing Practical Algorithms for Real-world Face Restoration.
- **[xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)** — Real-ESRGAN aims at developing Practical Algorithms for General Image/Video Restoration.
- **[4ian/GDevelop](https://github.com/4ian/GDevelop)** — 🎮 Open-source, cross-platform 2D/3D/multiplayer game engine designed for everyone.
- **[3b1b/manim](https://github.com/3b1b/manim)** — Animation engine for explanatory math videos
- **[LibreSprite/LibreSprite](https://github.com/LibreSprite/LibreSprite)** — Animated sprite editor & pixel art tool -- Fork of the last GPLv2 commit of Aseprite
- **[jdxyw/generativeart](https://github.com/jdxyw/generativeart)** — Generative Art in Go
- **[ianhan/BitmapFonts](https://github.com/ianhan/BitmapFonts)** — My collection of bitmap fonts pulled from various demoscene archives over the years
- **[channingbreeze/games](https://github.com/channingbreeze/games)** — 一个基于Phaser的小游戏集合
- **[angelikatyborska/mazes](https://github.com/angelikatyborska/mazes)** — A maze generator made with PhoenixLiveView.
- **[enkimute/ganja.js](https://github.com/enkimute/ganja.js)** — :triangular_ruler: Javascript Geometric Algebra Generator for Javascript, c++, c#, rust, python. (with operator overloading and algebraic literals) -
- **[textadventures/quest](https://github.com/textadventures/quest)** — Create text adventure games
- **[aemkei/tixy](https://github.com/aemkei/tixy)** — (t,i,x,y) => "creative code golfing"
- **[game-icons/icons](https://github.com/game-icons/icons)** — All SVG icons available on https://game-icons.net
- **[electronicarts/CnC_Remastered_Collection](https://github.com/electronicarts/CnC_Remastered_Collection)** — `(archived)` Command & Conquer: Remastered Collection
- **[bkaradzic/bgfx](https://github.com/bkaradzic/bgfx)** — Cross-platform, graphics API agnostic, "Bring Your Own Engine/Framework" style rendering library.
- **[freeserf/freeserf](https://github.com/freeserf/freeserf)** — Settlers 1 (Serf City) clone.
- **[OpenDiablo2/OpenDiablo2](https://github.com/OpenDiablo2/OpenDiablo2)** — `(archived)` An open source re-implementation of Diablo 2
- **[nuno-faria/tiler](https://github.com/nuno-faria/tiler)** — 👷 Build images with images
- **[raysan5/raylib](https://github.com/raysan5/raylib)** — A simple and easy-to-use library to enjoy videogames programming
- **[ellisonleao/magictools](https://github.com/ellisonleao/magictools)** — :video_game: :pencil: A list of Game Development resources to make magic happen.
- **[CytopiaTeam/Cytopia](https://github.com/CytopiaTeam/Cytopia)** — :deciduous_tree::house_with_garden::office::evergreen_tree: A city building simulation game
- **[viewizard/astromenace](https://github.com/viewizard/astromenace)** — Hardcore 3D space scroll-shooter with spaceship upgrade possibilities.
- **[rwv/chinese-dos-games](https://github.com/rwv/chinese-dos-games)** — 🎮 Chinese DOS games collections.
- **[eduard-permyakov/permafrost-engine](https://github.com/eduard-permyakov/permafrost-engine)** — An OpenGL RTS game engine written in C
- **[flame-engine/flame](https://github.com/flame-engine/flame)** — A Flutter based game engine.
- **[pixijs/pixijs](https://github.com/pixijs/pixijs)** — The HTML5 Creation Engine: Create beautiful digital content with the fastest, most flexible 2D WebGL renderer.
- **[lichess-org/lila](https://github.com/lichess-org/lila)** — ♞ lichess.org: the forever free, adless and open source chess server ♞
- **[SFTtech/openage](https://github.com/SFTtech/openage)** — Clone of the Age of Empires II engine 🚀
- **[endless-sky/endless-sky](https://github.com/endless-sky/endless-sky)** — Space exploration, trading, and combat game.
- **[Calinou/awesome-gamedev](https://github.com/Calinou/awesome-gamedev)** — A collection of free software and free culture resources for making amazing games. (mirror)
- **[stared/science-based-games-list](https://github.com/stared/science-based-games-list)** — Science-based games - a collaborative list
- **[naev/naev](https://github.com/naev/naev)** — Naev has moved to codeberg! This is just a mirror.
- **[gloomyson/SC_Js](https://github.com/gloomyson/SC_Js)** — Classic RTS game using html5 canvas and javascript, only js codes, all copyrighted materials removed
- **[triestpa/Atlas-Of-Thrones](https://github.com/triestpa/Atlas-Of-Thrones)** — An interactive "Game of Thrones" map powered by Leaflet, PostGIS, and Redis.
- **[stillmotion/terminal-games](https://github.com/stillmotion/terminal-games)** — Terminal-based clones of popular arcade games.
- **[makaroni4/guitar_bro](https://github.com/makaroni4/guitar_bro)** — Guitar Bro – browser game that helps you learn notes on guitar
- **[bgrins/javascript-astar](https://github.com/bgrins/javascript-astar)** — A* Search / Pathfinding Algorithm in Javascript
- **[AlmasB/FXGL](https://github.com/AlmasB/FXGL)** — Java / JavaFX / Kotlin Game Library (Engine)
- **[crosire/reshade](https://github.com/crosire/reshade)** — A generic post-processing injector for games and video software.
- **[crosire/reshade-shaders](https://github.com/crosire/reshade-shaders)** — A collection of post-processing shaders written for ReShade.
- **[mxgmn/WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse)** — Bitmap & tilemap generation from a single example with the help of ideas from quantum mechanics
- **[bolknote/SedChess](https://github.com/bolknote/SedChess)** — Шахматы, написанные на языке утилиты sed
- **[nosir/obelisk.js](https://github.com/nosir/obelisk.js)** — Build pixel isometric graphics with HTML5 canvas
- **[hakimel/Meny](https://github.com/hakimel/Meny)** — A three dimensional and space effecient menu
- **[OgarProject/Ogar](https://github.com/OgarProject/Ogar)** — `(archived)` An open source Agar.io server implementation, written with Node.js.
- **[mrdoob/texgen.js](https://github.com/mrdoob/texgen.js)** — JavaScript Texture Generator
- **[zfedoran/pixel-sprite-generator](https://github.com/zfedoran/pixel-sprite-generator)** — JavaScript procedural sprite generator
- **[clockworklabs/SpacetimeDB](https://github.com/clockworklabs/SpacetimeDB)** — Development at the speed of light
- **[veltman/clmystery](https://github.com/veltman/clmystery)** — A command-line murder mystery
- **[kaplayjs/kaplay](https://github.com/kaplayjs/kaplay)** — 🦖 A JavaScript/TypeScript Game Library that feels like a game.
- **[hpjansson/chafa](https://github.com/hpjansson/chafa)** — 📺🗿 Terminal graphics for the 21st century.
- **[nikopueringer/CorridorKey](https://github.com/nikopueringer/CorridorKey)** — Perfect Green Screen Keys
- **[freeorion/freeorion](https://github.com/freeorion/freeorion)** — Source code repository of the FreeOrion project.
- **[dmotz/trystero](https://github.com/dmotz/trystero)** — ✨🤝✨ Instant peer-to-peer multiplayer for the web — no server required.
- **[vengi-voxel/vengi](https://github.com/vengi-voxel/vengi)** — free and open source voxel art tools - editor, thumbnailer and format converter
- **[aldegad/sprite-gen](https://github.com/aldegad/sprite-gen)** — Generate clean 2D game sprites & animation atlases — component-row pipeline: state rows, alpha cleanup, frame extraction, runtime atlases. Codex/Claude skill.
- **[dday9/t-pico](https://github.com/dday9/t-pico)** — Minimal CSS Framework for semantic HTML forked from PicoCSS
- **[toji/gl-matrix](https://github.com/toji/gl-matrix)** — Javascript Matrix and Vector library for High Performance WebGL apps
- **[processing/p5.js](https://github.com/processing/p5.js)** — p5.js is a client-side JS platform that empowers artists, designers, students, and anyone to learn to code and express themselves creatively on the web. It is based on the core principles of Processing. Looking for p5.js 2.0? http://beta.p5js.org

## 🩵 go-dev (65)

Golang libs

- **[jinzhu/now](https://github.com/jinzhu/now)** — Now is a time toolkit for golang
- **[AllenDang/giu](https://github.com/AllenDang/giu)** — Cross platform rapid GUI framework for golang based on Dear ImGui.
- **[fyne-io/fyne](https://github.com/fyne-io/fyne)** — Cross platform GUI toolkit in Go inspired by Material Design
- **[nil-go/konf](https://github.com/nil-go/konf)** — The simplest config loader for Go that reads/watches from file, env, flag and clouds (AWS, Azure, GCP).
- **[Netflix/go-env](https://github.com/Netflix/go-env)** — a golang library to manage environment variables
- **[destel/rill](https://github.com/destel/rill)** — Go toolkit for clean, composable, channel-based concurrency.
- **[samber/oops](https://github.com/samber/oops)** — 🔥 Error handling library with context, assertion, stack trace and source fragments
- **[gookit/goutil](https://github.com/gookit/goutil)** — 💪 Helper Utils(900+): int, byte, string, array/slice, map, struct, dump, convert/format, error, web/http, cli/flag, OS/ENV, filesystem, system, test/assert, time and more. Go 常用的工具函数：数字，字符串，数组，Map，结构体，反射，文本，文件，错误，时间日期，特殊处理，格式化，常用信息获取等等
- **[twpayne/go-jsonstruct](https://github.com/twpayne/go-jsonstruct)** — Generate Go structs from multiple JSON or YAML objects.
- **[Zomato/espresso](https://github.com/Zomato/espresso)** — espresso
- **[dustin/go-humanize](https://github.com/dustin/go-humanize)** — Go Humans! (formatters for units to human friendly sizes)
- **[sqlc-dev/sqlc](https://github.com/sqlc-dev/sqlc)** — Generate type-safe code from SQL
- **[stephenafamo/bob](https://github.com/stephenafamo/bob)** — SQL query builder and ORM/Factory generator for Go with support for PostgreSQL, MySQL and SQLite
- **[gobuffalo/plush](https://github.com/gobuffalo/plush)** — The powerful template system that Go needs
- **[go-rod/rod](https://github.com/go-rod/rod)** — A Chrome DevTools Protocol driver for web automation and scraping.
- **[gocolly/colly](https://github.com/gocolly/colly)** — Elegant Scraper and Crawler Framework for Golang
- **[charmbracelet/gum](https://github.com/charmbracelet/gum)** — A tool for glamorous shell scripts 🎀
- **[gopxl/pixel](https://github.com/gopxl/pixel)** — A hand-crafted 2D game library in Go.
- **[jakecoffman/cp](https://github.com/jakecoffman/cp)** — A pure Go physics library with no dependencies. Unofficial Chipmunk2D port.
- **[EngoEngine/engo](https://github.com/EngoEngine/engo)** — Engo is an open-source 2D game engine written in Go.
- **[rivo/tview](https://github.com/rivo/tview)** — Terminal UI library with rich, interactive widgets — written in Golang
- **[pocketbase/pocketbase](https://github.com/pocketbase/pocketbase)** — `(archived)` Open Source realtime backend in 1 file
- **[wailsapp/wails](https://github.com/wailsapp/wails)** — Create beautiful applications using Go
- **[progrium/darwinkit](https://github.com/progrium/darwinkit)** — Native Mac APIs for Go. Previously known as MacDriver
- **[gokrazy/gokrazy](https://github.com/gokrazy/gokrazy)** — turn your Go program(s) into an appliance running on the Raspberry Pi 3, Pi 4, Pi 5, Pi Zero 2 W, or PCs (x86_64 or ARM64)!
- **[lucor/lian](https://github.com/lucor/lian)** — lian is a license analyzer for Go binaries and modules
- **[ent/ent](https://github.com/ent/ent)** — An entity framework for Go
- **[dariubs/GoBooks](https://github.com/dariubs/GoBooks)** — List of Golang books
- **[xlzd/gotp](https://github.com/xlzd/gotp)** — Golang OTP(One-Time Password) Library.
- **[smallstep/certificates](https://github.com/smallstep/certificates)** — 🛡️ A private certificate authority (X.509 & SSH) & ACME server for secure automated certificate management, so you can use TLS everywhere & SSO for SSH.
- **[x-izumin/grapi](https://github.com/x-izumin/grapi)** — 😮 A surprisingly easy API server and generator in gRPC and Go
- **[go-chi/chi](https://github.com/go-chi/chi)** — lightweight, idiomatic and composable router for building Go HTTP services
- **[labstack/echo](https://github.com/labstack/echo)** — High performance, minimalist Go web framework
- **[charmbracelet/bubbletea](https://github.com/charmbracelet/bubbletea)** — A powerful little TUI framework 🏗
- **[brianvoe/gofakeit](https://github.com/brianvoe/gofakeit)** — Random fake data generator written in go
- **[go-echarts/go-echarts](https://github.com/go-echarts/go-echarts)** — 🎨 The adorable charts library for Golang.
- **[goreleaser/goreleaser](https://github.com/goreleaser/goreleaser)** — Release engineering, simplified
- **[inancgumus/learngo](https://github.com/inancgumus/learngo)** — ❤️ 1000+ Hand-Crafted Go Examples, Exercises, and Quizzes. 🚀 Learn Go by fixing 1000+ tiny programs.
- **[hoanhan101/ultimate-go](https://github.com/hoanhan101/ultimate-go)** — The Ultimate Go Study Guide
- **[wazero/wazero](https://github.com/wazero/wazero)** — wazero: the zero dependency WebAssembly runtime for Go developers
- **[shomali11/go-interview](https://github.com/shomali11/go-interview)** — Collection of Technical Interview Questions solved with Go
- **[golang-ui/nuklear](https://github.com/golang-ui/nuklear)** — This project provides Go bindings for nuklear.h — a small ANSI C GUI library.
- **[revive-lint/revive](https://github.com/revive-lint/revive)** — 🔥 Fast, strict, configurable, extensible, and beautiful linter for Go
- **[urfave/cli](https://github.com/urfave/cli)** — A declarative, simple, fast, and fun package for building command line tools in Go
- **[micro/go-micro](https://github.com/micro/go-micro)** — A framework for agents, tools and services
- **[a8m/golang-cheat-sheet](https://github.com/a8m/golang-cheat-sheet)** — An overview of Go syntax and features.
- **[gonum/gonum](https://github.com/gonum/gonum)** — Gonum is a set of numeric libraries for the Go programming language. It contains libraries for matrices, statistics, optimization, and more
- **[avelino/awesome-go](https://github.com/avelino/awesome-go)** — A curated list of awesome Go frameworks, libraries and software
- **[dunglas/vulcain](https://github.com/dunglas/vulcain)** — 🔨 Fast and idiomatic client-driven REST APIs.
- **[anthonynsimon/bild](https://github.com/anthonynsimon/bild)** — Image processing algorithms in pure Go
- **[tdewolff/canvas](https://github.com/tdewolff/canvas)** — Vector graphics in Go
- **[hybridgroup/gobot](https://github.com/hybridgroup/gobot)** — Golang framework for robotics, drones, and the Internet of Things (IoT)
- **[sashabaranov/go-openai](https://github.com/sashabaranov/go-openai)** — OpenAI, GPT 6.1, GPT-Image-2, Whisper API clients for Go. Zero-dependency.
- **[ory/oathkeeper](https://github.com/ory/oathkeeper)** — A cloud native Identity & Access Proxy / API (IAP) and Access Control Decision API that authenticates, authorizes, and mutates incoming HTTP(s) requests. Inspired by the BeyondCorp / Zero Trust white paper. Written in Go.
- **[tidwall/tile38](https://github.com/tidwall/tile38)** — Real-time Geospatial and Geofencing
- **[vuvuzela/vuvuzela](https://github.com/vuvuzela/vuvuzela)** — Private messaging system that hides metadata
- **[mxschmitt/playwright-go](https://github.com/mxschmitt/playwright-go)** — Playwright for Go a browser automation library to control Chromium, Firefox and WebKit with a single API.
- **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** — A Go implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.
- **[upper/db](https://github.com/upper/db)** — Data Access Layer (DAL) for PostgreSQL, CockroachDB, MySQL, SQLite and MongoDB with ORM-like features.
- **[cloudwego/goref](https://github.com/cloudwego/goref)** — Go heap object reference analysis tool
- **[stretchr/objx](https://github.com/stretchr/objx)** — Go package for dealing with maps, slices, JSON and other data.
- **[tmc/langchaingo](https://github.com/tmc/langchaingo)** — LangChain for Go, the easiest way to write LLM-based programs in Go
- **[goforj/godump](https://github.com/goforj/godump)** — Configurable Go value and struct dumps with colorized output, type visibility controls, and field redaction.
- **[uber-go/guide](https://github.com/uber-go/guide)** — The Uber Go Style Guide.
- **[roneli/goqux](https://github.com/roneli/goqux)** — Library for simple CRUD, scanning & pagination using query builder in golang

## 📟hack-&-devices (19)

- **[RamboRogers/rfhunter](https://github.com/RamboRogers/rfhunter)** — RFHunter is a device to find hidden Cameras at AirBNBs
- **[hybridgroup/go-haystack](https://github.com/hybridgroup/go-haystack)** — Track personal Bluetooth devices via Apple's "Find My" network using OpenHaystack and Macless-Haystack with tools written in Go/TinyGo. No Apple hardware required! Build your own beacon using Xiao-BLE, ESP32-C3/S3, & many other boards.
- **[minimaxir/hacker-news-undocumented](https://github.com/minimaxir/hacker-news-undocumented)** — Some of the hidden norms about Hacker News not otherwise covered in the Guidelines and the FAQ.
- **[NARKOZ/hacker-scripts](https://github.com/NARKOZ/hacker-scripts)** — Based on a true story
- **[F5OEO/rpitx](https://github.com/F5OEO/rpitx)** — RF transmitter for Raspberry Pi
- **[gokrazy/gokrazy](https://github.com/gokrazy/gokrazy)** — turn your Go program(s) into an appliance running on the Raspberry Pi 3, Pi 4, Pi 5, Pi Zero 2 W, or PCs (x86_64 or ARM64)!
- **[bskari/pi-rc](https://github.com/bskari/pi-rc)** — `(archived)` Turn your Raspberry Pi into a radio controller for RC toys.
- **[lawsonkeith/picar](https://github.com/lawsonkeith/picar)** — Raspberry Pi controlled RC car using WiFi and a smartphone.
- **[thingsboard/thingsboard](https://github.com/thingsboard/thingsboard)** — All-in-one IoT Platform - Device management, data collection, processing and visualization.
- **[greatscottgadgets/hackrf](https://github.com/greatscottgadgets/hackrf)** — low cost software radio platform
- **[bemasher/rtlamr](https://github.com/bemasher/rtlamr)** — An rtl-sdr receiver for Itron ERT compatible smart meters operating in the 900MHz ISM band.
- **[vuvuzela/vuvuzela](https://github.com/vuvuzela/vuvuzela)** — Private messaging system that hides metadata
- **[larsp/co2monitor](https://github.com/larsp/co2monitor)** — CO₂ & Temperature monitor
- **[Eplox/TCP-Starvation](https://github.com/Eplox/TCP-Starvation)**
- **[cure53/H5SC](https://github.com/cure53/H5SC)** — HTML5 Security Cheatsheet - A collection of HTML5 related XSS attack vectors
- **[librepods-org/librepods](https://github.com/librepods-org/librepods)** — AirPods liberated from Apple's ecosystem.
- **[geo-tp/ESP32-Bit-Pirate](https://github.com/geo-tp/ESP32-Bit-Pirate)** — A Hardware Hacking Tool with Web-Based CLI That Speaks Every Protocol
- **[jomjol/AI-on-the-edge-device](https://github.com/jomjol/AI-on-the-edge-device)** — Easy to use device for connecting "old" measuring units (water, power, gas, ...) to the digital world
- **[devbis/z03mmc](https://github.com/devbis/z03mmc)** — Xiaomi LYWSD03MMC Zigbee Firmware

## ☕️ java-dev (72)

Java libs

- **[coekie/flowtracker](https://github.com/coekie/flowtracker)** — Track data flowing through Java programs
- **[togglz/togglz](https://github.com/togglz/togglz)** — Feature Flags for the Java platform
- **[kordamp/jarviz](https://github.com/kordamp/jarviz)** — ☕️ JAR file analyzer
- **[szeiger/perfio](https://github.com/szeiger/perfio)**
- **[testcontainers/testcontainers-java](https://github.com/testcontainers/testcontainers-java)** — Testcontainers is a Java library that supports JUnit tests, providing lightweight, throwaway instances of common databases, Selenium web browsers, or anything else that can run in a Docker container.
- **[ta4j/ta4j](https://github.com/ta4j/ta4j)** — A Java library for technical analysis.
- **[ff4j/ff4j](https://github.com/ff4j/ff4j)** — Feature Flags for Java made easy
- **[AlmasB/FXGL](https://github.com/AlmasB/FXGL)** — Java / JavaFX / Kotlin Game Library (Engine)
- **[bladecoder/bladecoder-adventure-engine](https://github.com/bladecoder/bladecoder-adventure-engine)** — Classic point and click adventure game engine and editor
- **[bnanes/shrink-pdf](https://github.com/bnanes/shrink-pdf)** — Reduce PDF file size by applying jpeg compression to embedded images
- **[Splitties/refreshVersions](https://github.com/Splitties/refreshVersions)** — Life is too short to google for dependencies and versions
- **[cashapp/licensee](https://github.com/cashapp/licensee)** — Gradle plugin which validates the licenses of your dependency graph match what you expect
- **[jooby-project/jooby](https://github.com/jooby-project/jooby)** — The modular web framework for Java and Kotlin
- **[sproket/Persism](https://github.com/sproket/Persism)** — A zero ceremony ORM for Java
- **[Hakky54/mutual-tls-ssl](https://github.com/Hakky54/mutual-tls-ssl)** — 🔐 Tutorial of setting up Security for your API with one way authentication with TLS/SSL and mutual authentication for a java based web server and a client with both Spring Boot. Different clients are provided such as Apache HttpClient, OkHttp, Spring RestTemplate, Spring WebFlux WebClient Jetty and Netty, the old and the new JDK HttpClient, the old and the new Jersey Client, Google HttpClient, Unirest, Retrofit, Feign, Methanol, vertx, Scala client Finagle, Featherbed, Dispatch Reboot, AsyncHttpClient, Sttp, Akka, Requests Scala, Http4s Blaze, Kotlin client Fuel, http4k, Kohttp and ktor. Also other server examples are available such as jersey with grizzly. Also gRPC, WebSocket and ElasticSearch examples are included
- **[ben-manes/caffeine](https://github.com/ben-manes/caffeine)** — A high performance caching library for Java
- **[immutables/immutables](https://github.com/immutables/immutables)** — Java annotation processor to create immutable objects and builders, for records too. Sweep boilerplate code under the rug!
- **[nickd3000/minvio](https://github.com/nickd3000/minvio)** — Processing-style sketches in plain Java. Minvio handles the window + draw loop so you can focus on graphics and experiments.
- **[baomidou/mybatis-plus](https://github.com/baomidou/mybatis-plus)** — An powerful enhanced toolkit of MyBatis for simplify development
- **[dbeaver/dbeaver](https://github.com/dbeaver/dbeaver)** — Free universal database tool and SQL client
- **[uber/NullAway](https://github.com/uber/NullAway)** — A tool to help eliminate NullPointerExceptions (NPEs) in your Java code with low build-time overhead
- **[Hakky54/ayza](https://github.com/Hakky54/ayza)** — 🔐 An SSL library for configuring http client or server. Rich with features such as hot reloading ssl and trusting additional certificates during runtime, combining multiple keystores, loading pem files and os/jdk certificates, logging certificate information during ssl handshake, bypassing ssl configuration from other libraries and more
- **[Auties00/Cobalt](https://github.com/Auties00/Cobalt)** — Standalone unofficial fully-featured Whatsapp Web and Mobile API for Java and Kotlin
- **[OpenHFT/Chronicle-Bytes](https://github.com/OpenHFT/Chronicle-Bytes)** — Chronicle Bytes has a similar purpose to Java NIO's ByteBuffer with many extensions
- **[vigna/fastutil](https://github.com/vigna/fastutil)** — fastutil extends the Java™ Collections Framework by providing type-specific maps, sets, lists and queues.
- **[OpenHFT/Zero-Allocation-Hashing](https://github.com/OpenHFT/Zero-Allocation-Hashing)** — Zero-allocation hashing for Java
- **[aeron-io/agrona](https://github.com/aeron-io/agrona)** — High Performance data structures and utility methods for Java
- **[jdbi/jdbi](https://github.com/jdbi/jdbi)** — The Jdbi library provides convenient, idiomatic access to relational databases in Java and other JVM technologies such as Kotlin, Clojure or Scala.
- **[VerbalExpressions/JavaVerbalExpressions](https://github.com/VerbalExpressions/JavaVerbalExpressions)** — Java regular expressions made easy.
- **[fusesource/jansi](https://github.com/fusesource/jansi)** — Jansi is a small java library that allows you to use ANSI escape sequences to format your console output which works even on windows.
- **[tinylog-org/tinylog](https://github.com/tinylog-org/tinylog)** — tinylog is a lightweight logging framework for Java, Kotlin, Scala, and Android
- **[mike-neck/graalvm-native-image-plugin](https://github.com/mike-neck/graalvm-native-image-plugin)** — A Gradle plugin which creates a native executable via GraalVM's native-image. This is a thin wrapper of the native-image command.
- **[oracle/tribuo](https://github.com/oracle/tribuo)** — Tribuo - A Java machine learning library
- **[mizosoft/methanol](https://github.com/mizosoft/methanol)** — ⚗️ Lightweight HTTP extensions for Java & Kotlin
- **[kohlschutter/junixsocket](https://github.com/kohlschutter/junixsocket)** — Unix Domain Sockets for all Java versions 7 and newer (AF_UNIX), AF_TIPC, AF_VSOCK, and more
- **[getsentry/sentry-java](https://github.com/getsentry/sentry-java)** — A Sentry SDK for Java, Android and other JVM languages.
- **[G00fY2/version-compare](https://github.com/G00fY2/version-compare)** — Lightweight library for Android, Java and Kotlin to compare version strings.
- **[Blazebit/blaze-persistence](https://github.com/Blazebit/blaze-persistence)** — Rich Criteria API for JPA providers
- **[oblac/jodd](https://github.com/oblac/jodd)** — Jodd! Lightweight. Java. Zero dependencies. Use what you like.
- **[google/play-work](https://github.com/google/play-work)** — `(archived)`
- **[lysine-dev/okio](https://github.com/lysine-dev/okio)** — A modern I/O library for Android, Java, and Kotlin Multiplatform.
- **[pingidentity/ldapsdk](https://github.com/pingidentity/ldapsdk)** — UnboundID LDAP SDK for Java
- **[langchain4j/langchain4j](https://github.com/langchain4j/langchain4j)** — LangChain4j is an idiomatic, open-source Java library for building LLM-powered applications on the JVM. It offers a unified API over popular LLM providers and vector stores, and makes implementing tool calling (including MCP support), agents and RAG easy. It integrates seamlessly with enterprise Java frameworks like Quarkus and Spring Boot.
- **[iluwatar/java-design-patterns](https://github.com/iluwatar/java-design-patterns)** — Design patterns implemented in Java
- **[kdn251/interviews](https://github.com/kdn251/interviews)** — Everything you need to know to get the job.
- **[akullpp/awesome-java](https://github.com/akullpp/awesome-java)** — A curated list of awesome frameworks, libraries and software for the Java programming language.
- **[deeplearning4j/deeplearning4j](https://github.com/deeplearning4j/deeplearning4j)** — Suite of tools for deploying and training deep learning models using the JVM. Highlights include model import for keras, tensorflow, and onnx/pytorch, a modular and tiny c++ library for running math code and a java based math library on top of the core c++ library. Also includes samediff: a pytorch/tensorflow like library for running deep learn...
- **[OpenFeign/feign](https://github.com/OpenFeign/feign)** — Feign makes writing java http clients easier
- **[perwendel/spark](https://github.com/perwendel/spark)** — A simple expressive web framework for java. Spark has a kotlin DSL https://github.com/perwendel/spark-kotlin
- **[NanoHttpd/nanohttpd](https://github.com/NanoHttpd/nanohttpd)** — Tiny, easily embeddable HTTP server in Java.
- **[google/error-prone](https://github.com/google/error-prone)** — Catch common Java mistakes as compile-time errors
- **[raphw/byte-buddy](https://github.com/raphw/byte-buddy)** — Runtime code generation for the Java virtual machine.
- **[joelittlejohn/jsonschema2pojo](https://github.com/joelittlejohn/jsonschema2pojo)** — Generate Java types from JSON or JSON Schema and annotate those types for data-binding with Jackson, Gson, etc
- **[auth0/java-jwt](https://github.com/auth0/java-jwt)** — Java implementation of JSON Web Token (JWT)
- **[cxxr/better-java](https://github.com/cxxr/better-java)** — Resources for writing modern Java
- **[jankotek/mapdb](https://github.com/jankotek/mapdb)** — MapDB provides concurrent Maps, Sets and Queues backed by disk storage or off-heap-memory. It is a fast and easy to use embedded Java database engine.
- **[bytedeco/javacpp](https://github.com/bytedeco/javacpp)** — The missing bridge between Java and native C++
- **[JCTools/JCTools](https://github.com/JCTools/JCTools)**
- **[tdebatty/java-string-similarity](https://github.com/tdebatty/java-string-similarity)** — Implementation of various string similarity and distance algorithms: Levenshtein, Jaro-winkler, n-Gram, Q-Gram, Jaccard index, Longest Common Subsequence edit distance, cosine similarity ...
- **[geotools/geotools](https://github.com/geotools/geotools)** — Official GeoTools repository
- **[hcoles/pitest](https://github.com/hcoles/pitest)** — State of the art mutation testing system for the JVM
- **[google/conscrypt](https://github.com/google/conscrypt)** — Conscrypt is a Java Security Provider that implements parts of the Java Cryptography Extension and Java Secure Socket Extension.
- **[sqids/sqids-java](https://github.com/sqids/sqids-java)** — Official Java port of Sqids. Generate short unique IDs from numbers.
- **[klehmann/domino-jna](https://github.com/klehmann/domino-jna)** — Java project to access the IBM/HCL Domino C API using Java Native Access (JNA)
- **[vert-x3/vertx-awesome](https://github.com/vert-x3/vertx-awesome)** — A curated list of awesome Vert.x resources, libraries, and other nice things.
- **[vert-x3/vertx-web](https://github.com/vert-x3/vertx-web)** — HTTP web applications for Vert.x
- **[skylot/jadx](https://github.com/skylot/jadx)** — Dex to Java decompiler
- **[mamba-studio/TypedMemory](https://github.com/mamba-studio/TypedMemory)** — A Java 25 library for mapping records to strongly typed off-heap memory using the FFM API.
- **[bytecodealliance/endive](https://github.com/bytecodealliance/endive)** — The JVM native WebAssembly runtime
- **[dylibso/chicory](https://github.com/dylibso/chicory)** — Native JVM WebAssembly runtime
- **[gradle/gradle-completion](https://github.com/gradle/gradle-completion)** — Gradle tab completion for bash and zsh
- **[runningcode/gradle-doctor](https://github.com/runningcode/gradle-doctor)** — The right prescription for your Gradle build.

## 💡 knowledge (82)

Books, data, lists, recipes, etc.

- **[rlabbe/Kalman-and-Bayesian-Filters-in-Python](https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python)** — Kalman Filter book using Jupyter Notebook. Focuses on building intuition and experience, not formal proofs. Includes Kalman filters,extended Kalman filters, unscented Kalman filters, particle filters, and more. All exercises include solutions.
- **[codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)** — Master programming by recreating your favorite technologies from scratch.
- **[mcinglis/c-style](https://github.com/mcinglis/c-style)** — `(archived)` My favorite C programming practices.
- **[danielmiessler/SecLists](https://github.com/danielmiessler/SecLists)** — SecLists is the security tester's companion. It's a collection of multiple types of lists used during security assessments, collected in one place. List types include usernames, passwords, URLs, sensitive data patterns, fuzzing payloads, web shells, and many more.
- **[gto76/python-cheatsheet](https://github.com/gto76/python-cheatsheet)** — Comprehensive Python Cheatsheet
- **[Olshansk/postgres_for_everything](https://github.com/Olshansk/postgres_for_everything)** — How to reduce complexity and move faster? Just Postgres for everything.
- **[webpro/programming-principles](https://github.com/webpro/programming-principles)** — Categorized overview of programming principles & design patterns
- **[BNU-Wang-MSN-Lab/FAVEE-HPP](https://github.com/BNU-Wang-MSN-Lab/FAVEE-HPP)**
- **[git-tips/tips](https://github.com/git-tips/tips)** — Most commonly used git tips and tricks.
- **[zakirullin/cognitive-load](https://github.com/zakirullin/cognitive-load)** — 🧠 Cognitive load is what matters
- **[little-book-of/linear-algebra](https://github.com/little-book-of/linear-algebra)** — A concise, beginner-friendly introduction to the core ideas of linear algebra.
- **[ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev)** — A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev
- **[jonathandion/awesome-emails](https://github.com/jonathandion/awesome-emails)** — ✉️ An awesome list of resources to build better emails.
- **[little-book-of/algorithms](https://github.com/little-book-of/algorithms)** — Bake a cake with care, follow steps the recipe gives, that’s an algorithm.
- **[DovAmir/awesome-design-patterns](https://github.com/DovAmir/awesome-design-patterns)** — A curated list of software and architecture related design patterns.
- **[ByteByteGoHq/system-design-101](https://github.com/ByteByteGoHq/system-design-101)** — Explain complex systems using visuals and simple terms. Help you prepare for system design interviews.
- **[EuropeanRemote/european-remote-software-companies](https://github.com/EuropeanRemote/european-remote-software-companies)** — List of the remote software companies hiring in Europe
- **[remoteintech/remote-jobs](https://github.com/remoteintech/remote-jobs)** — Source for remoteintech.company — a community-maintained directory of remote-friendly tech companies
- **[poteto/hiring-without-whiteboards](https://github.com/poteto/hiring-without-whiteboards)** — ⭐️ Companies that don't have a broken hiring process
- **[mtdvio/every-programmer-should-know](https://github.com/mtdvio/every-programmer-should-know)** — A collection of (mostly) technical things every software developer should know about
- **[sb2nov/resume](https://github.com/sb2nov/resume)** — Software developer resume in Latex
- **[jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university)** — A complete computer science study plan to become a software engineer.
- **[hackerkid/Mind-Expanding-Books](https://github.com/hackerkid/Mind-Expanding-Books)** — :books: Find your next book to read!
- **[jonathanpaulson/grabby_aliens](https://github.com/jonathanpaulson/grabby_aliens)**
- **[dariubs/GoBooks](https://github.com/dariubs/GoBooks)** — List of Golang books
- **[microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners)** — 12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all
- **[lukasz-madon/awesome-remote-job](https://github.com/lukasz-madon/awesome-remote-job)** — A curated list of awesome remote jobs and resources. Inspired by https://github.com/vinta/awesome-python
- **[Kostadin/Places-in-Bulgaria](https://github.com/Kostadin/Places-in-Bulgaria)** — Населени места в България, пощенски кодове, ЕКАТТЕ кодове, телефонни кодове, GPS координати, области, общини и кметства
- **[bradtraversy/design-resources-for-developers](https://github.com/bradtraversy/design-resources-for-developers)** — Curated list of design and UI resources from stock photos, web templates, CSS frameworks, UI libraries, tools and much more
- **[3b1b/manim](https://github.com/3b1b/manim)** — Animation engine for explanatory math videos
- **[ossu/computer-science](https://github.com/ossu/computer-science)** — 🎓 Path to a free self-taught education in Computer Science!
- **[LeCoupa/awesome-cheatsheets](https://github.com/LeCoupa/awesome-cheatsheets)** — 👩‍💻👨‍💻 Awesome cheatsheets for popular programming languages, frameworks and development tools. They include everything you should know in one single file.
- **[cli-guidelines/cli-guidelines](https://github.com/cli-guidelines/cli-guidelines)** — A guide to help you write better command-line programs, taking traditional UNIX principles and updating them for the modern day.
- **[jerryn70/GoodbyeAds](https://github.com/jerryn70/GoodbyeAds)**
- **[leonardomso/awesome-fsm](https://github.com/leonardomso/awesome-fsm)** — 🤖 A curated list of awesome resources related to finite state machines and statecharts.
- **[inancgumus/learngo](https://github.com/inancgumus/learngo)** — ❤️ 1000+ Hand-Crafted Go Examples, Exercises, and Quizzes. 🚀 Learn Go by fixing 1000+ tiny programs.
- **[hoanhan101/ultimate-go](https://github.com/hoanhan101/ultimate-go)** — The Ultimate Go Study Guide
- **[shomali11/go-interview](https://github.com/shomali11/go-interview)** — Collection of Technical Interview Questions solved with Go
- **[a8m/golang-cheat-sheet](https://github.com/a8m/golang-cheat-sheet)** — An overview of Go syntax and features.
- **[public-api-lists/public-api-lists](https://github.com/public-api-lists/public-api-lists)** — A curated list of free public APIs — searchable, community-maintained, with a free JSON API.
- **[guyinatuxedo/nightmare](https://github.com/guyinatuxedo/nightmare)**
- **[ankane/awesome-legal](https://github.com/ankane/awesome-legal)** — Awesome free legal documents for companies
- **[teivah/algodeck](https://github.com/teivah/algodeck)** — An Open-Source Collection of Flash Cards to Help You Preparing Your Algorithms & Data Structures and System Design Interviews 💯
- **[thewhitetulip/awk-anti-textbook](https://github.com/thewhitetulip/awk-anti-textbook)** — learn awk by example
- **[avelino/awesome-go](https://github.com/avelino/awesome-go)** — A curated list of awesome Go frameworks, libraries and software
- **[awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted)** — A list of Free Software network services and web applications which can be hosted on your own servers
- **[ellisonleao/magictools](https://github.com/ellisonleao/magictools)** — :video_game: :pencil: A list of Game Development resources to make magic happen.
- **[mgechev/google-interview-preparation-problems](https://github.com/mgechev/google-interview-preparation-problems)** — leetcode problems I solved to prepare for my Google interview.
- **[vert-x3/advanced-vertx-guide](https://github.com/vert-x3/advanced-vertx-guide)** — A gentle guide for advanced Vert.x users
- **[amirrajan/survivingtheappstore](https://github.com/amirrajan/survivingtheappstore)** — My book on getting to the #1 Spot in the App Store. Buy my games to support me.
- **[kelseyhightower/nocode](https://github.com/kelseyhightower/nocode)** — The best way to write secure and reliable applications. Write nothing; deploy nowhere.
- **[life4/textdistance](https://github.com/life4/textdistance)** — 📐 Compute distance between sequences. 30+ algorithms, pure python implementation, common interface, optional external libs usage.
- **[JerBouma/FinanceToolkit](https://github.com/JerBouma/FinanceToolkit)** — Transparent and Efficient Financial Analysis
- **[ZaneH/piano-trainer](https://github.com/ZaneH/piano-trainer)** — 🎹 Memorize piano scales with ease! A piano practice program w/ MIDI support. Consider it an interactive reference manual
- **[Calinou/awesome-gamedev](https://github.com/Calinou/awesome-gamedev)** — A collection of free software and free culture resources for making amazing games. (mirror)
- **[stared/science-based-games-list](https://github.com/stared/science-based-games-list)** — Science-based games - a collaborative list
- **[iluwatar/java-design-patterns](https://github.com/iluwatar/java-design-patterns)** — Design patterns implemented in Java
- **[kdn251/interviews](https://github.com/kdn251/interviews)** — Everything you need to know to get the job.
- **[akullpp/awesome-java](https://github.com/akullpp/awesome-java)** — A curated list of awesome frameworks, libraries and software for the Java programming language.
- **[rainyear/javascript-in-one-pic](https://github.com/rainyear/javascript-in-one-pic)** — Learn javascript in one picture.
- **[cxxr/better-java](https://github.com/cxxr/better-java)** — Resources for writing modern Java
- **[binhnguyennus/awesome-scalability](https://github.com/binhnguyennus/awesome-scalability)** — The Patterns of Scalable, Reliable, and Performant Large-Scale Systems
- **[slikts/concurrency-glossary](https://github.com/slikts/concurrency-glossary)** — 🦑 Informal definitions of terms used in concurrency modeling
- **[karan/Projects](https://github.com/karan/Projects)** — :page_with_curl: A list of practical projects that anyone can solve in any programming language.
- **[Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code)** — Coding articles to level up your development skills
- **[chubin/cheat.sh](https://github.com/chubin/cheat.sh)** — the only cheat sheet you need
- **[LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words)** — List of Dirty, Naughty, Obscene, and Otherwise Bad Words
- **[arialdomartini/Back-End-Developer-Interview-Questions](https://github.com/arialdomartini/Back-End-Developer-Interview-Questions)** — A list of back-end related questions you can be inspired from to interview potential candidates, test yourself or completely ignore
- **[coells/100days](https://github.com/coells/100days)** — 100 days of algorithms
- **[lhartikk/naivechain](https://github.com/lhartikk/naivechain)** — A blockchain implementation in 200 lines of code
- **[arogozhnikov/python3_with_pleasure](https://github.com/arogozhnikov/python3_with_pleasure)** — A short guide on features of Python 3 with examples
- **[heyalexej/awesome-images](https://github.com/heyalexej/awesome-images)** — A curated list of amazingly awesome free (stock) photo resources inspired by all the other awesomes.
- **[tldr-pages/tldr](https://github.com/tldr-pages/tldr)** — Collaborative cheatsheets for console commands 📚.
- **[georgezouq/awesome-ai-in-finance](https://github.com/georgezouq/awesome-ai-in-finance)** — 🔬 A curated list of awesome LLMs & deep learning strategies & tools in financial market.
- **[pedropark99/zig-book](https://github.com/pedropark99/zig-book)** — An open, technical and introductory book for the Zig programming language 📚📖
- **[sharkbench/sharkbench](https://github.com/sharkbench/sharkbench)** — Benchmarking programming languages and web frameworks.
- **[rendercv/rendercv](https://github.com/rendercv/rendercv)** — Resume builder for academics and engineers
- **[trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge)** — A collection of inspiring lists, manuals, cheatsheets, blogs, hacks, one-liners, cli/web tools and more.
- **[career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops)** — Open-source AI job search agent and job finder: scan job boards, score each job 1-5 against your CV before you apply, tailor an ATS-friendly resume and cover letter, get interview prep and an application tracker. It helps you fill in each application; you press Submit. Runs locally in Codex, OpenCode and other AI CLIs, or as a Claude Code plugin.
- **[dr5hn/countries-states-cities-database](https://github.com/dr5hn/countries-states-cities-database)** — 🌍 Discover our global repository of countries, states, and cities! 🏙️ Get comprehensive data in JSON, SQL, PSQL, SQLSERVER, MONGODB, SQLITE, XML, YAML, and CSV formats. Access ISO2, ISO3 codes, country code, capital, native language, timezones (for countries), and more. #countries #states #cities
- **[BraveOPotato/NoSignups](https://github.com/BraveOPotato/NoSignups)** — A list of tools that are open-source, in-browser, and require no-signups!
- **[ericdrowell/BigOCheatSheet](https://github.com/ericdrowell/BigOCheatSheet)**

## 🤖 MCP (10)

MCP Tools

- **[radiosilence/fastmail-cli](https://github.com/radiosilence/fastmail-cli)** — CLI and MCP server for Fastmail — email, contacts, masked email, attachments, text extraction. JMAP + CardDAV + GraphQL.
- **[open-webui/open-webui](https://github.com/open-webui/open-webui)** — User-friendly AI Interface (Supports Ollama, OpenAI API, ...)
- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** — A collection of MCP servers.
- **[casdoor/casdoor](https://github.com/casdoor/casdoor)** — An open-source Agent-first Identity and Access Management (IAM) /LLM MCP & agent gateway and auth server with web UI supporting OpenClaw, MCP, OAuth, OIDC, SAML, CAS, LDAP, SCIM, WebAuthn, TOTP, MFA, Face ID, Google Workspace, Azure AD
- **[LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP)** — MCP Server for Ghidra
- **[modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector)** — Deterministic testing tools for MCP servers
- **[mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)** — A Go implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools.
- **[centralmind/gateway](https://github.com/centralmind/gateway)** — Universal MCP-Server for your Databases optimized for LLMs and AI-Agents.
- **[ai-tools-all/grep_app_mcp](https://github.com/ai-tools-all/grep_app_mcp)** — MCP for grep.app
- **[petarov/starghlist](https://github.com/petarov/starghlist)** — MCP server to manage your GitHub starred repositories and lists

## 📱mdm (12)

- **[microsoftconnect/ms-intune-app-sdk-ios](https://github.com/microsoftconnect/ms-intune-app-sdk-ios)** — Intune App SDK for iOS enables data protection and mobile app management features in iOS mobile apps with Microsoft Intune
- **[micromdm/nanomdm](https://github.com/micromdm/nanomdm)** — NanoMDM is a minimalist Apple MDM server and library heavily inspired by MicroMDM
- **[bruienne/depy](https://github.com/bruienne/depy)** — Apple DEP module for Python
- **[jessepeterson/mdmb](https://github.com/jessepeterson/mdmb)** — mdmb is a tool for simulating Apple devices interacting with Apple MDM servers.
- **[zentralopensource/zentral](https://github.com/zentralopensource/zentral)** — Zentral is a control plane for secure, observable Apple endpoints in enterprises. Configure, observe, and enforce the desired state of every Apple endpoint. Manage that desired state as code through GitOps and Terraform.
- **[mdmdirector/mdmdirector](https://github.com/mdmdirector/mdmdirector)**
- **[jessepeterson/kmfddm](https://github.com/jessepeterson/kmfddm)** — KMFDDM is an Apple Declarative Device Management (DDM) server. It works together with NanoMDM.
- **[apple/device-management](https://github.com/apple/device-management)** — Device management schema data for MDM.
- **[rtrouton/profiles](https://github.com/rtrouton/profiles)** — Management profiles for OS X / macOS
- **[munki/munki](https://github.com/munki/munki)** — Managed software installation for macOS —
- **[micromdm/micromdm](https://github.com/micromdm/micromdm)** — Mobile Device Management server
- **[fleetdm/fleet](https://github.com/fleetdm/fleet)** — Open device management

## 🎸music-audio (17)

Audio tools and music making

- **[facebookresearch/audiocraft](https://github.com/facebookresearch/audiocraft)** — Audiocraft is a library for audio processing and generation with deep learning. It features the state-of-the-art EnCodec audio compressor / tokenizer, along with MusicGen, a simple and controllable music generation LM with textual and melodic conditioning.
- **[milkytracker/MilkyTracker](https://github.com/milkytracker/MilkyTracker)** — A Fasttracker II compatible music editor
- **[schismtracker/schismtracker](https://github.com/schismtracker/schismtracker)** — An oldschool sample-based music composition tool.
- **[steffest/BassoonTracker](https://github.com/steffest/BassoonTracker)** — Webbased old-school Amiga music tracker in plain old javascript - Plays and edits Amiga Mod files and FastTracker XM files
- **[kmatheussen/radium](https://github.com/kmatheussen/radium)** — A graphical music editor. A next generation tracker.
- **[kometbomb/klystrack](https://github.com/kometbomb/klystrack)** — A chiptune tracker
- **[nukeop/nuclear](https://github.com/nukeop/nuclear)** — Streaming music player that finds free music for you
- **[Tonejs/Tone.js](https://github.com/Tonejs/Tone.js)** — A Web Audio framework for making interactive music in the browser.
- **[LMMS/lmms](https://github.com/LMMS/lmms)** — Cross-platform music production software
- **[IrosTheBeggar/mStream](https://github.com/IrosTheBeggar/mStream)** — The easiest music streaming server available
- **[ZaneH/piano-trainer](https://github.com/ZaneH/piano-trainer)** — 🎹 Memorize piano scales with ease! A piano practice program w/ MIDI support. Consider it an interactive reference manual
- **[kevincennis/TinyMusic](https://github.com/kevincennis/TinyMusic)** — A simple, lightweight music synth/sequencer in JavaScript using the Web Audio API.
- **[ExistentialAudio/BlackHole](https://github.com/ExistentialAudio/BlackHole)** — BlackHole is a modern macOS audio loopback driver that allows applications to pass audio to other applications with zero additional latency.
- **[bbc/peaks.js](https://github.com/bbc/peaks.js)** — JavaScript UI component for interacting with audio waveforms
- **[meyda/meyda](https://github.com/meyda/meyda)** — Audio feature extraction for JavaScript.
- **[kylestetz/slang](https://github.com/kylestetz/slang)** — 🎤 a simple audio programming language implemented in JS
- **[makaroni4/guitar_bro](https://github.com/makaroni4/guitar_bro)** — Guitar Bro – browser game that helps you learn notes on guitar

## 📦 platforms (43)

Services and platforms - runnable on Docker or VPS

- **[mjmlio/mjml](https://github.com/mjmlio/mjml)** — MJML: the only framework that makes responsive email easy
- **[Notifuse/notifuse](https://github.com/Notifuse/notifuse)** — Open-source, self-hosted newsletter, email marketing and transactional email platform. Visual MJML editor, Liquid templating, 7 sending providers.
- **[iam-abbas/Reddit-Stock-Trends](https://github.com/iam-abbas/Reddit-Stock-Trends)** — Fetch currently trending stocks on Reddit
- **[manifoldmarkets/manifold](https://github.com/manifoldmarkets/manifold)** — Manifold Markets: A market for every question
- **[zedeus/nitter](https://github.com/zedeus/nitter)** — `(archived)` Alternative Twitter front-end
- **[huginn/huginn](https://github.com/huginn/huginn)** — Create agents that monitor and act on your behalf. Your agents are standing by!
- **[dzikoysk/reposilite](https://github.com/dzikoysk/reposilite)** — Lightweight and easy-to-use repository management software dedicated for the Maven-based artifacts in the JVM ecosystem 📦
- **[TryQuiet/quiet](https://github.com/TryQuiet/quiet)** — A private, p2p alternative to Slack and Discord built on Tor & IPFS
- **[knadh/listmonk](https://github.com/knadh/listmonk)** — High performance, self-hosted, newsletter and mailing list manager with a modern dashboard. Single binary app.
- **[nsqio/nsq](https://github.com/nsqio/nsq)** — A realtime distributed messaging platform
- **[zentralopensource/zentral](https://github.com/zentralopensource/zentral)** — Zentral is a control plane for secure, observable Apple endpoints in enterprises. Configure, observe, and enforce the desired state of every Apple endpoint. Manage that desired state as code through GitOps and Terraform.
- **[binwiederhier/ntfy](https://github.com/binwiederhier/ntfy)** — Send push notifications to your phone or desktop using PUT/POST
- **[ergochat/ergo](https://github.com/ergochat/ergo)** — A modern IRC server (daemon/ircd) written in Go.
- **[evcc-io/evcc](https://github.com/evcc-io/evcc)** — smart charging ☀️🚘
- **[chubin/wttr.in](https://github.com/chubin/wttr.in)** — :partly_sunny: The right way to check the weather
- **[OpenHealthForAll/open-health](https://github.com/OpenHealthForAll/open-health)** — OpenHealth, AI Health Assistant | Powered by Your Data
- **[Budibase/budibase](https://github.com/Budibase/budibase)** — AI agents, automations and apps that run your operations. Model agnostic.
- **[appsmithorg/appsmith](https://github.com/appsmithorg/appsmith)** — Platform to build admin panels, internal tools, and dashboards. Integrates with 25+ databases and any API.
- **[apache/answer](https://github.com/apache/answer)** — A Q&A platform software for teams at any scales. Whether it's a community forum, help center, or knowledge management platform, you can always count on Apache Answer.
- **[discuitnet/discuit](https://github.com/discuitnet/discuit)** — A free and open-source community discussion platform.
- **[thingsboard/thingsboard](https://github.com/thingsboard/thingsboard)** — All-in-one IoT Platform - Device management, data collection, processing and visualization.
- **[medusajs/medusa](https://github.com/medusajs/medusa)** — The world's most flexible commerce platform for agents and developers
- **[smallstep/certificates](https://github.com/smallstep/certificates)** — 🛡️ A private certificate authority (X.509 & SSH) & ACME server for secure automated certificate management, so you can use TLS everywhere & SSO for SSH.
- **[janeczku/calibre-web](https://github.com/janeczku/calibre-web)** — :books: Web app for browsing, reading and downloading eBooks stored in a Calibre database
- **[hashicorp/nomad](https://github.com/hashicorp/nomad)** — Nomad is an easy-to-use, flexible, and performant workload orchestrator that can deploy a mix of microservice, batch, containerized, and non-containerized applications. Nomad is easy to operate and scale and has native Consul and Vault integrations.
- **[olric-data/olric](https://github.com/olric-data/olric)** — Distributed, in-memory key/value store and cache. It can be used as an embedded Go library and a language-independent service.
- **[xipki/xipki](https://github.com/xipki/xipki)** — XiPKI: Compact open source PKI (CA, OCSP responder, certificate protocols ACME, CMP, EST, SCEP), with full support of PQC MLDSA (Dilithium) and MLKEM (Kyber).
- **[theparanoids/crypki](https://github.com/theparanoids/crypki)** — A simple service for interacting with an HSM or other PKCS#11 device.
- **[dunglas/vulcain](https://github.com/dunglas/vulcain)** — 🔨 Fast and idiomatic client-driven REST APIs.
- **[awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted)** — A list of Free Software network services and web applications which can be hosted on your own servers
- **[bitwarden/server](https://github.com/bitwarden/server)** — Bitwarden infrastructure/backend (API, database, Docker, etc).
- **[Kozea/Radicale](https://github.com/Kozea/Radicale)** — A simple CalDAV (calendar) and CardDAV (contact) server.
- **[dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden)** — Unofficial Bitwarden compatible server written in Rust, formerly known as bitwarden_rs
- **[umputun/remark42](https://github.com/umputun/remark42)** — comment engine
- **[C4illin/ConvertX](https://github.com/C4illin/ConvertX)** — 💾 Self-hosted online file converter. Supports 1000+ formats ⚙️
- **[gchq/CyberChef](https://github.com/gchq/CyberChef)** — The Cyber Swiss Army Knife - a web app for encryption, encoding, compression and data analysis
- **[FujiwaraChoki/MoneyPrinterV2](https://github.com/FujiwaraChoki/MoneyPrinterV2)** — Automate the process of making money online.
- **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** — The open-source app everyone uses to manage agents at work
- **[macadmins/sofa](https://github.com/macadmins/sofa)** — SOFA | A MacAdmin's Simple Organized Feed for Apple Software Updates
- **[markqvist/NomadNet](https://github.com/markqvist/NomadNet)** — Communicate Freely
- **[chattocorp/chatto](https://github.com/chattocorp/chatto)** — A fully-featured team and group chat application that you can easily selfhost.
- **[traefik/traefik](https://github.com/traefik/traefik)** — The Cloud Native Application Proxy
- **[pgsty/silo](https://github.com/pgsty/silo)** — S3-Compatible Object Storage. A MinIO fork maintained by PGSTY

## 👾 re-game (12)

rewrite/recomp/decomp games

- **[TekRantGaming/digdug-native](https://github.com/TekRantGaming/digdug-native)** — Native Windows and Linux port of Namco's Dig Dug arcade game (bring your own ROMs). Controller support, widescreen fill, in-game menu.
- **[gilshlo/Alley-Cat](https://github.com/gilshlo/Alley-Cat)** — Alley-Cat recreation
- **[MaddoScientisto/Crusader-Map-Viewer](https://github.com/MaddoScientisto/Crusader-Map-Viewer)** — A map viewer for Crusader: No Remorse and Crusader: No Regret
- **[rhuizer/alleycat](https://github.com/rhuizer/alleycat)** — An open source IBM AlleyCat 1984 implementation
- **[petarov/alleycat.exe](https://github.com/petarov/alleycat.exe)** — x86_64 recompilation of Alley Cat - a video game by Bill Williams for Atari (1983) and IBM PC (1984)
- **[sebsebseb1982/crusader-no-remorse-decomp](https://github.com/sebsebseb1982/crusader-no-remorse-decomp)** — No pity... No mercy... No Remorse.
- **[SubmitGame/awesome-decomp-games](https://github.com/SubmitGame/awesome-decomp-games)** — Rated, auto-refreshed list of decompiled, recompiled & reverse-engineered games: decomps, static recomps, source ports, engine remakes, browser ports.
- **[petarov/saboteur2](https://github.com/petarov/saboteur2)** — A recompilation of Saboteur II: Avenging Angel (1987) from its original DOS executable to x86_64 platforms
- **[missingno7/pre2_port](https://github.com/missingno7/pre2_port)** — Prehistorik 2 DOS_RE Source-Port Workbench
- **[Pyrdacor/freeserf.net](https://github.com/Pyrdacor/freeserf.net)** — Settlers 1 clone written in C#
- **[grovdata/RodLegacy](https://github.com/grovdata/RodLegacy)** — A modern reimplementation of Street Rod 1&2
- **[OpenDUNE/OpenDUNE](https://github.com/OpenDUNE/OpenDUNE)** — DUNE, REINVENTED

## 🦀 rust-dev (2)

rust libs, tools, learn

- **[ferrous-systems/rust-training](https://github.com/ferrous-systems/rust-training)** — Learning materials for the Rust Training courses by Ferrous Systems
- **[microsoft/RustTraining](https://github.com/microsoft/RustTraining)** — Beginner, advanced, expert level Rust training material

## 🕸️ web-dev (62)

js/typescript libs and other web frameworks

- **[franciscop/picnic](https://github.com/franciscop/picnic)** — :handbag: A beautiful CSS library to kickstart your projects
- **[bigskysoftware/htmx](https://github.com/bigskysoftware/htmx)** — </> htmx - high power tools for HTML
- **[orchidjs/tom-select](https://github.com/orchidjs/tom-select)** — Tom Select is a lightweight (~16kb gzipped) hybrid of a textbox and select box. Forked from selectize.js to provide a framework agnostic autocomplete widget with native-feeling keyboard navigation. Useful for tagging, contact lists, etc.
- **[freshframework/fresh](https://github.com/freshframework/fresh)** — The framework so simple, you already know it.
- **[oapi-codegen/oapi-codegen](https://github.com/oapi-codegen/oapi-codegen)** — Generate Go client and server boilerplate from OpenAPI 3 specifications
- **[SawyerHood/draw-a-ui](https://github.com/SawyerHood/draw-a-ui)** — Draw a mockup and generate html for it
- **[shadcn-ui/ui](https://github.com/shadcn-ui/ui)** — Composable, accessible components with thoughtful defaults. Build your own component library with code you can customize, extend, and make your own.
- **[Kalabasa/htmz](https://github.com/Kalabasa/htmz)** — html with targeted manipulation zones
- **[microsoft/fluentui-system-icons](https://github.com/microsoft/fluentui-system-icons)** — Fluent System Icons are a collection of familiar, friendly and modern icons from Microsoft.
- **[codazoda/neatcss](https://github.com/codazoda/neatcss)** — Rapidly build efficient sites with Neat, the minimalist css framework.
- **[xz/new.css](https://github.com/xz/new.css)** — A classless CSS framework to write modern websites using only HTML.
- **[bansal/pattern.css](https://github.com/bansal/pattern.css)** — CSS only library to fill empty background with beautiful patterns.
- **[animate-css/animate.css](https://github.com/animate-css/animate.css)** — 🍿 A cross-browser library of CSS animations. As easy to use as an easy thing.
- **[ubershmekel/cssbed](https://github.com/ubershmekel/cssbed)** — Test bed for simple css resets that make your static page nice without classes.
- **[jgthms/bulma](https://github.com/jgthms/bulma)** — Modern CSS framework based on Flexbox
- **[Dogfalo/materialize](https://github.com/Dogfalo/materialize)** — Materialize, a CSS Framework based on Material Design
- **[mdbootstrap/mdb-ui-kit](https://github.com/mdbootstrap/mdb-ui-kit)** — Bootstrap 5 & Material Design UI KIT
- **[pure-css/pure](https://github.com/pure-css/pure)** — A set of small, responsive CSS modules that you can use in every web project.
- **[nostalgic-css/NES.css](https://github.com/nostalgic-css/NES.css)** — NES-style CSS Framework | ファミコン風CSSフレームワーク
- **[astrit/css.gg](https://github.com/astrit/css.gg)** — 700+ Pure CSS, SVG & Figma UI Icons, 6000+ glyphs, patterns, colors and layouts.
- **[milligram/milligram](https://github.com/milligram/milligram)** — A minimalist CSS framework.
- **[tabler/tabler-icons](https://github.com/tabler/tabler-icons)** — A set of over 6500 free MIT-licensed high-quality SVG icons for you to use in your web projects.
- **[kognise/water.css](https://github.com/kognise/water.css)** — A drop-in collection of CSS styles to make simple websites just a little nicer
- **[sbstjn/timesheet.js](https://github.com/sbstjn/timesheet.js)** — JavaScript library for HTML5 & CSS3 time sheets
- **[troxler/awesome-css-frameworks](https://github.com/troxler/awesome-css-frameworks)** — List of awesome CSS frameworks in 2026
- **[trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms)** — 📝 Algorithms and data structures implemented in JavaScript with explanations and links to further readings
- **[Leaflet/Leaflet](https://github.com/Leaflet/Leaflet)** — 🍃 number one JavaScript library for interactive maps 🇺🇦
- **[lipis/flag-icons](https://github.com/lipis/flag-icons)** — :flags: A curated collection of all country flags in SVG — plus the CSS for easier integration
- **[alpinejs/alpine](https://github.com/alpinejs/alpine)** — A rugged, minimal framework for composing JavaScript behavior in your markup.
- **[just-js/just](https://github.com/just-js/just)** — the only javascript runtime to hit no.1 on techempower :fire:
- **[denoland/deno](https://github.com/denoland/deno)** — A modern runtime for JavaScript and TypeScript.
- **[nextapps-de/winbox](https://github.com/nextapps-de/winbox)** — WinBox is a modern HTML5 window manager for the Web.
- **[emailmonday/Cerberus](https://github.com/emailmonday/Cerberus)** — Simple, but solid patterns for responsive HTML email templates and newsletters. Even in Outlook and Gmail.
- **[goodsign/monday](https://github.com/goodsign/monday)** — Monday is a minimalistic l10n, i18n package for translation of month and day of week names in time.Date objects.
- **[arwes/arwes](https://github.com/arwes/arwes)** — Futuristic Sci-Fi UI Web Framework.
- **[rough-stuff/rough](https://github.com/rough-stuff/rough)** — Create graphics with a hand-drawn, sketchy, appearance
- **[shipshapecode/shepherd](https://github.com/shipshapecode/shepherd)** — Guide your users through a tour of your app
- **[akveo/eva-icons](https://github.com/akveo/eva-icons)** — A pack of more than 480 beautifully crafted Open Source icons. SVG, Sketch, Web Font and Animations support.
- **[jarek-foksa/xel](https://github.com/jarek-foksa/xel)** — Xel - Widget toolkit for building native-like Electron and Web apps
- **[yoannmoinet/nipplejs](https://github.com/yoannmoinet/nipplejs)** — :video_game: A virtual joystick for touch capable interfaces.
- **[pmndrs/react-spring](https://github.com/pmndrs/react-spring)** — ✌️ A spring physics based React animation library
- **[Tonejs/Tone.js](https://github.com/Tonejs/Tone.js)** — A Web Audio framework for making interactive music in the browser.
- **[kevincennis/TinyMusic](https://github.com/kevincennis/TinyMusic)** — A simple, lightweight music synth/sequencer in JavaScript using the Web Audio API.
- **[bbc/peaks.js](https://github.com/bbc/peaks.js)** — JavaScript UI component for interacting with audio waveforms
- **[meyda/meyda](https://github.com/meyda/meyda)** — Audio feature extraction for JavaScript.
- **[pixijs/pixijs](https://github.com/pixijs/pixijs)** — The HTML5 Creation Engine: Create beautiful digital content with the fastest, most flexible 2D WebGL renderer.
- **[rainyear/javascript-in-one-pic](https://github.com/rainyear/javascript-in-one-pic)** — Learn javascript in one picture.
- **[bgrins/javascript-astar](https://github.com/bgrins/javascript-astar)** — A* Search / Pathfinding Algorithm in Javascript
- **[olkinn/forest-blue-iTerm](https://github.com/olkinn/forest-blue-iTerm)** — :evergreen_tree: A fresh calm color theme for iTerm
- **[ejci/favico.js](https://github.com/ejci/favico.js)** — Make use of your favicon with badges, images or videos
- **[hakimel/Meny](https://github.com/hakimel/Meny)** — A three dimensional and space effecient menu
- **[romeovs/creep](https://github.com/romeovs/creep)** — a pretty sweet 4px wide pixel font.
- **[NUKnightLab/TimelineJS](https://github.com/NUKnightLab/TimelineJS)** — `(archived)` TimelineJS: A Storytelling Timeline built in JavaScript.
- **[bitwiseshiftleft/sjcl](https://github.com/bitwiseshiftleft/sjcl)** — [DEPRECATED] Stanford Javascript Crypto Library
- **[picocss/pico](https://github.com/picocss/pico)** — `(archived)` Minimal CSS Framework for semantic HTML
- **[dbohdan/classless-css](https://github.com/dbohdan/classless-css)** — A list of classless CSS themes/frameworks with screenshots
- **[iconify/iconify](https://github.com/iconify/iconify)** — Universal icon framework. One syntax for FontAwesome, Material Design Icons, DashIcons, Feather Icons, EmojiOne, Noto Emoji and many other open source icon sets (over 200 icon sets and ~300k icons). SVG framework, React, Vue and Svelte components!
- **[andybrewer/mvp](https://github.com/andybrewer/mvp)** — MVP.css — Minimalist classless CSS stylesheet for HTML elements
- **[bigskysoftware/intercooler-js](https://github.com/bigskysoftware/intercooler-js)** — Making AJAX as easy as anchor tags
- **[jsfiddle/togetherjs](https://github.com/jsfiddle/togetherjs)** — A service for your website that makes it surprisingly easy to collaborate in real-time.
- **[chartist-js/chartist](https://github.com/chartist-js/chartist)** — Simple responsive charts
- **[cheeriojs/cheerio](https://github.com/cheeriojs/cheerio)** — The fast, flexible, and elegant library for parsing and manipulating HTML and XML.

## Other (141)

- **[kazu-yamamoto/pgpdump](https://github.com/kazu-yamamoto/pgpdump)** — A PGP packet visualizer
- **[ValyriaTear/ValyriaTear](https://github.com/ValyriaTear/ValyriaTear)** — Open Source J-RPG (Based on the Hero of Allacrost engine)
- **[nullptrlabs/pgmodeler](https://github.com/nullptrlabs/pgmodeler)** — Open-source data modeling tool designed for PostgreSQL. No more typing DDL commands. Let pgModeler do the work for you!
- **[jedisct1/libsodium](https://github.com/jedisct1/libsodium)** — A modern, portable, easy to use crypto library.
- **[Blizzard/s2protocol](https://github.com/Blizzard/s2protocol)** — Python library to decode StarCraft II replay protocols
- **[clippyjs/clippy.js](https://github.com/clippyjs/clippy.js)** — Add Clippy or his friends to any website for instant nostalgia.
- **[lapo-luchini/asn1js](https://github.com/lapo-luchini/asn1js)** — JavaScript generic ASN.1 parser
- **[glfw/glfw](https://github.com/glfw/glfw)** — A multi-platform library for OpenGL, OpenGL ES, Vulkan, window and input
- **[medialize/URI.js](https://github.com/medialize/URI.js)** — Javascript URL mutation library
- **[adambard/learnxinyminutes-docs](https://github.com/adambard/learnxinyminutes-docs)** — Code documentation written as code! How novel and totally my idea!
- **[zerotier/ZeroTierOne](https://github.com/zerotier/ZeroTierOne)** — A Smart Ethernet Switch for Earth
- **[bramp/js-sequence-diagrams](https://github.com/bramp/js-sequence-diagrams)** — Draws simple SVG sequence diagrams from textual representation of the diagram
- **[greensock/GSAP](https://github.com/greensock/GSAP)** — GSAP (GreenSock Animation Platform), a JavaScript animation library for the modern web
- **[verekia/initializr](https://github.com/verekia/initializr)** — HTML5 Boilerplate Build Tool
- **[zzzprojects/sqlfiddle](https://github.com/zzzprojects/sqlfiddle)**
- **[EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books)** — :books: Freely available programming books
- **[jstherightway/js-the-right-way](https://github.com/jstherightway/js-the-right-way)** — An easy-to-read, quick reference for JS best practices, accepted coding standards, and links around the Web
- **[pump-io/pump.io](https://github.com/pump-io/pump.io)** — Social server with an ActivityStreams API
- **[framework7io/framework7](https://github.com/framework7io/framework7)** — Full featured HTML framework for building iOS & Android apps
- **[interagent/http-api-design](https://github.com/interagent/http-api-design)** — HTTP API design guide extracted from work on the Heroku Platform API
- **[hoodiehq/hoodie](https://github.com/hoodiehq/hoodie)** — :dog: The Offline First JavaScript Backend
- **[geraintluff/tv4](https://github.com/geraintluff/tv4)** — Tiny Validator for JSON Schema v4
- **[gka/chroma.js](https://github.com/gka/chroma.js)** — JavaScript library for all kinds of color manipulations
- **[claritylab/lucida](https://github.com/claritylab/lucida)** — Speech and Vision Based Intelligent Personal Assistant
- **[0xAX/linux-insides](https://github.com/0xAX/linux-insides)** — A book-in-progress about the Linux kernel and its insides.
- **[wsargent/docker-cheat-sheet](https://github.com/wsargent/docker-cheat-sheet)** — Docker Cheat Sheet
- **[h2o/h2o](https://github.com/h2o/h2o)** — H2O - the optimized HTTP/1, HTTP/2, HTTP/3 server
- **[pgilad/leasot](https://github.com/pgilad/leasot)** — Parse and output TODOs and FIXMEs from comments in your files
- **[paperjs/paper.js](https://github.com/paperjs/paper.js)** — The Swiss Army Knife of Vector Graphics Scripting – Scriptographer ported to JavaScript and the browser, using HTML5 Canvas. Created by @lehni & @puckey
- **[nvie/gitflow](https://github.com/nvie/gitflow)** — `(archived)` Git extensions to provide high-level repository operations for Vincent Driessen's branching model.
- **[tmux/tmux](https://github.com/tmux/tmux)** — tmux source code
- **[etcd-io/etcd](https://github.com/etcd-io/etcd)** — Distributed reliable key-value store for the most critical data of a distributed system
- **[wasabeef/awesome-android-ui](https://github.com/wasabeef/awesome-android-ui)** — A curated list of awesome Android UI/UX libraries
- **[owenashurst/agar.io-clone](https://github.com/owenashurst/agar.io-clone)** — Agar.io clone written with Socket.IO and HTML5 canvas
- **[codepath/android_guides](https://github.com/codepath/android_guides)** — Extensive Open-Source Guides for Android Developers
- **[jgm/pandoc](https://github.com/jgm/pandoc)** — Universal markup converter
- **[miki151/keeperrl](https://github.com/miki151/keeperrl)** — Source code of KeeperRL
- **[JuanPotato/Legofy](https://github.com/JuanPotato/Legofy)** — Make images look as if they are made out of 1x1 LEGO blocks
- **[sharpbracket/redshift](https://github.com/sharpbracket/redshift)** — `(archived)` Redshift adjusts the color temperature of your screen according to your surroundings. This may help your eyes hurt less if you are working in front of the screen at night.
- **[opengaming/osgameclones](https://github.com/opengaming/osgameclones)** — Open Source Clones of Popular Games
- **[0ad/0ad](https://github.com/0ad/0ad)** — `(archived)` [DEPRECATED] Git mirror of the 0 A.D. SVN source code (migrated to https://gitea.wildfiregames.com on August 20th 2024)
- **[slact/nchan](https://github.com/slact/nchan)** — Fast, horizontally scalable, multiprocess pub/sub queuing server and proxy for HTTP, long-polling, Websockets and EventSource (SSE), powered by Nginx.
- **[jlevy/og-equity-compensation](https://github.com/jlevy/og-equity-compensation)** — Stock options, RSUs, taxes — read the latest edition: www.holloway.com/ec
- **[Keith-S-Thompson/how-to-c-response](https://github.com/Keith-S-Thompson/how-to-c-response)** — A critique of "How to C in 2016"
- **[ronf/asyncssh](https://github.com/ronf/asyncssh)** — AsyncSSH is a Python package which provides an asynchronous client and server implementation of the SSHv2 protocol on top of the Python asyncio framework.
- **[awesomedata/awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets)** — A topic-centric list of HQ open datasets.
- **[AppImage/AppImageKit](https://github.com/AppImage/AppImageKit)** — Package desktop applications as AppImages that run on common Linux-based operating systems, such as RHEL, CentOS, openSUSE, SLED, Ubuntu, Fedora, debian and derivatives. Join #AppImage on irc.libera.chat
- **[Introduction-to-Autonomous-Robots/Introduction-to-Autonomous-Robots](https://github.com/Introduction-to-Autonomous-Robots/Introduction-to-Autonomous-Robots)** — Introduction to Autonomous Robots
- **[concurrencykit/ck](https://github.com/concurrencykit/ck)** — Concurrency primitives, safe memory reclamation mechanisms and non-blocking (including lock-free) data structures designed to aid in the research, design and implementation of high performance concurrent systems developed in C99+.
- **[gittup/tup](https://github.com/gittup/tup)** — Tup is a file-based build system.
- **[mortenjust/cleartext-mac](https://github.com/mortenjust/cleartext-mac)** — A text editor that will help you write clearer and simpler
- **[auth0/auth0.js](https://github.com/auth0/auth0.js)** — Auth0 headless browser sdk
- **[vicoyeh/pointers-for-software-engineers](https://github.com/vicoyeh/pointers-for-software-engineers)** — A curated list of topics to start learning software engineering
- **[a1studmuffin/SpaceshipGenerator](https://github.com/a1studmuffin/SpaceshipGenerator)** — A Blender script to procedurally generate 3D spaceships
- **[inkle/inky](https://github.com/inkle/inky)** — An editor for ink: inkle's narrative scripting language
- **[chrislgarry/Apollo-11](https://github.com/chrislgarry/Apollo-11)** — Original Apollo 11 Guidance Computer (AGC) source code for the command and lunar modules.
- **[stateless4j/stateless4j](https://github.com/stateless4j/stateless4j)** — Lightweight Java State Machine
- **[tj/git-extras](https://github.com/tj/git-extras)** — GIT utilities -- repo summary, repl, changelog population, author commit percentages and more
- **[pavel-odintsov/fastnetmon](https://github.com/pavel-odintsov/fastnetmon)** — Very fast DDoS sensor with sFlow/Netflow/IPFIX/SPAN support
- **[elendirx/web2web](https://github.com/elendirx/web2web)** — P2P web powered by torrents and blockchain.
- **[ReFirmLabs/binwalk](https://github.com/ReFirmLabs/binwalk)** — Firmware Analysis Tool
- **[socketio/engine.io](https://github.com/socketio/engine.io)** — The engine used in the Socket.IO JavaScript server, which manages the low-level transports such as HTTP long-polling and WebSocket.
- **[aerkalov/ebooklib](https://github.com/aerkalov/ebooklib)** — A versatile Python library for EPUB2/EPUB3 manipulation and processing.
- **[bitwarden/clients](https://github.com/bitwarden/clients)** — Bitwarden client apps (web, browser extension, desktop, and cli).
- **[ZuzooVn/machine-learning-for-software-engineers](https://github.com/ZuzooVn/machine-learning-for-software-engineers)** — A complete daily plan for studying to become a machine learning engineer.
- **[sindresorhus/awesome](https://github.com/sindresorhus/awesome)** — 😎 Awesome lists about all kinds of interesting topics [NOTE: Pull requests are temporarily disabled until I have a chance to catch up with the existing ones]
- **[Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses)** — List of Computer Science courses with video lectures.
- **[qiao/PathFinding.js](https://github.com/qiao/PathFinding.js)** — A comprehensive path-finding library for grid based games
- **[n0shake/Public-APIs](https://github.com/n0shake/Public-APIs)** — 📚 A public list of APIs from round the web.
- **[palatable/lambda](https://github.com/palatable/lambda)** — Functional patterns for Java
- **[bitfighter/bitfighter](https://github.com/bitfighter/bitfighter)** — The Bitfighter source code
- **[jpillora/chisel](https://github.com/jpillora/chisel)** — A fast TCP/UDP tunnel over HTTP
- **[skeeto/enchive](https://github.com/skeeto/enchive)** — Encrypted personal archives
- **[atomashpolskiy/bt](https://github.com/atomashpolskiy/bt)** — BitTorrent library and client with DHT, magnet links, encryption and more
- **[keon/algorithms](https://github.com/keon/algorithms)** — Minimal examples of data structures and algorithms in Python
- **[jmapio/jmap](https://github.com/jmapio/jmap)** — JSON Meta Application Protocol Specification (JMAP)
- **[gendotnew/ai](https://github.com/gendotnew/ai)**
- **[ranapat/tasksf](https://github.com/ranapat/tasksf)** — Simple tasks manager factory
- **[ranapat/ely](https://github.com/ranapat/ely)** — Emit Light and Yell
- **[cisagov/pshtt](https://github.com/cisagov/pshtt)** — Scan domains and return data based on HTTPS best practices
- **[sdmg15/Best-websites-a-programmer-should-visit](https://github.com/sdmg15/Best-websites-a-programmer-should-visit)** — `(archived)` :link: Some useful websites for programmers.
- **[veltman/flubber](https://github.com/veltman/flubber)** — Tools for smoother shape animations.
- **[cs231n/cs231n.github.io](https://github.com/cs231n/cs231n.github.io)** — Public facing notes page
- **[public-apis/public-apis](https://github.com/public-apis/public-apis)** — A collective list of free APIs
- **[bokub/chalk-animation](https://github.com/bokub/chalk-animation)** — :clapper: Colorful animations in terminal output
- **[Zheaoli/awesome-coins](https://github.com/Zheaoli/awesome-coins)** — ₿ A guide (for humans!) to cryto-currencies and their algos.
- **[mbeaudru/modern-js-cheatsheet](https://github.com/mbeaudru/modern-js-cheatsheet)** — Cheatsheet for the JavaScript knowledge you will frequently encounter in modern projects.
- **[graphql/graphql-playground](https://github.com/graphql/graphql-playground)** — `(archived)` 🎮 GraphQL IDE for better development workflows (GraphQL Subscriptions, interactive docs & collaboration)
- **[Shopify/draggable](https://github.com/Shopify/draggable)** — `(archived)` The JavaScript Drag & Drop library your grandparents warned you about.
- **[HelloZeroNet/ZeroNet](https://github.com/HelloZeroNet/ZeroNet)** — ZeroNet - Decentralized websites using Bitcoin crypto and BitTorrent network
- **[fogleman/primitive](https://github.com/fogleman/primitive)** — Reproducing images with geometric primitives.
- **[mfornos/awesome-microservices](https://github.com/mfornos/awesome-microservices)** — A curated list of Microservice Architecture related principles and technologies.
- **[openalpr/openalpr](https://github.com/openalpr/openalpr)** — Automatic License Plate Recognition library
- **[franciscop/server](https://github.com/franciscop/server)** — :desktop_computer: Simple and powerful server for Node.js
- **[liabru/matter-js](https://github.com/liabru/matter-js)** — a 2D rigid body physics engine for the web ▲● ■
- **[russellsamora/scrollama](https://github.com/russellsamora/scrollama)** — Scrollytelling with IntersectionObserver.
- **[OpenGenus/cosmos](https://github.com/OpenGenus/cosmos)** — World's largest Contributor driven code dataset | Used in Quark Search Engine, @OpenGenus IQ, OpenGenus Visual Project
- **[edent/SuperTinyIcons](https://github.com/edent/SuperTinyIcons)** — Under 1KB each! Super Tiny Icons are miniscule SVG versions of your favourite website and app logos
- **[nayafia/lemonade-stand](https://github.com/nayafia/lemonade-stand)** — A handy guide to financial support for open source
- **[wolfcw/libfaketime](https://github.com/wolfcw/libfaketime)** — libfaketime modifies the system time for a single application
- **[boardgameio/boardgame.io](https://github.com/boardgameio/boardgame.io)** — State Management and Multiplayer Networking for Turn-Based Games
- **[EdwardRaff/JSAT](https://github.com/EdwardRaff/JSAT)** — Java Statistical Analysis Tool, a Java library for Machine Learning
- **[heynickc/awesome-ddd](https://github.com/heynickc/awesome-ddd)** — A curated list of Domain-Driven Design (DDD), Command Query Responsibility Segregation (CQRS), Event Sourcing, and Event Storming resources
- **[viatsko/awesome-vscode](https://github.com/viatsko/awesome-vscode)** — 🎨 A curated list of delightful VS Code packages and resources.
- **[mjswensen/themer](https://github.com/mjswensen/themer)** — 🎨 themer takes a set of colors and outputs themes for your apps (editors, terminals, wallpapers, and more).
- **[getify/You-Dont-Know-JS](https://github.com/getify/You-Dont-Know-JS)** — A book series (2 published editions) on the JS language.
- **[shekhargulati/30-seconds-of-java](https://github.com/shekhargulati/30-seconds-of-java)** — Curated collection of useful little Java functions that you can understand quickly
- **[mail-in-a-box/mailinabox](https://github.com/mail-in-a-box/mailinabox)** — Mail-in-a-Box helps individuals take back control of their email by defining a one-click, easy-to-deploy SMTP+everything else server: a mail server in a box.
- **[jupyterlab/jupyterlab](https://github.com/jupyterlab/jupyterlab)** — JupyterLab computational environment.
- **[google/trillian](https://github.com/google/trillian)** — A transparent, highly scalable and cryptographically verifiable data store.
- **[mathiasbynens/jsesc](https://github.com/mathiasbynens/jsesc)** — Given some data, jsesc returns the shortest possible stringified & ASCII-safe representation of that data.
- **[segmentio/evergreen](https://github.com/segmentio/evergreen)** — 🌲 Evergreen React UI Framework by Segment
- **[Chocobozzz/PeerTube](https://github.com/Chocobozzz/PeerTube)** — ActivityPub-federated video streaming platform using P2P directly in your web browser
- **[SadeghHayeri/GreenTunnel](https://github.com/SadeghHayeri/GreenTunnel)** — GreenTunnel is an anti-censorship utility designed to bypass the DPI system that is put in place by various ISPs to block access to certain websites.
- **[toml-lang/toml](https://github.com/toml-lang/toml)** — Tom's Obvious, Minimal Language
- **[metafizzy/zdog](https://github.com/metafizzy/zdog)** — Flat, round, designer-friendly pseudo-3D engine for canvas & SVG
- **[calebwin/emu](https://github.com/calebwin/emu)** — The write-once-run-anywhere GPGPU library for Rust
- **[hoppscotch/hoppscotch](https://github.com/hoppscotch/hoppscotch)** — Open-Source API Development Ecosystem • https://hoppscotch.io • Offline, On-Prem & Cloud • Web, Desktop & CLI • Open-Source Alternative to Postman, Insomnia
- **[didi/booster](https://github.com/didi/booster)** — 🚀Optimizer for mobile applications
- **[mermaid-js/mermaid](https://github.com/mermaid-js/mermaid)** — Generation of diagrams like flowcharts or sequence diagrams from text in a similar manner as markdown
- **[skorokithakis/expounder](https://github.com/skorokithakis/expounder)** — A library for explaining things in HTML.
- **[aaronjanse/dns-over-wikipedia](https://github.com/aaronjanse/dns-over-wikipedia)** — Redirect `.idk` domains using Wikipedia
- **[lucperkins/rek](https://github.com/lucperkins/rek)** — An easy HTTP client for Go. Inspired by the immortal Requests.
- **[sonictruth/vr-dos](https://github.com/sonictruth/vr-dos)** — 💾 Virtual Reality DOS
- **[goplus/xgo](https://github.com/goplus/xgo)** — XGo is a programming language that reads like plain English. But it's also incredibly powerful — it lets you leverage assets from C/C++, Go, Python, and JavaScript/TypeScript, creating a unified software engineering ecosystem. Our vision is to enable everyone to become a builder of the world.
- **[naptha/tesseract.js](https://github.com/naptha/tesseract.js)** — Pure Javascript OCR for more than 100 Languages 📖🎉🖥
- **[thedevsaddam/docgen](https://github.com/thedevsaddam/docgen)** — Transform your postman collection to HTML/Markdown documentation
- **[Trellmor/bind-adblock](https://github.com/Trellmor/bind-adblock)** — Use the BIND DNS server to block ads
- **[GuitarML/SmartGuitarAmp](https://github.com/GuitarML/SmartGuitarAmp)** — Guitar plugin made with JUCE that uses neural networks to emulate a tube amplifier.
- **[mxrch/GHunt](https://github.com/mxrch/GHunt)** — 🕵️‍♂️ Offensive Google framework.
- **[jakearchibald/svgomg](https://github.com/jakearchibald/svgomg)** — Web GUI for SVGO
- **[logisim-evolution/logisim-evolution](https://github.com/logisim-evolution/logisim-evolution)** — Digital logic design tool and simulator
- **[osnr/TabFS](https://github.com/osnr/TabFS)** — 🗄 Mount your browser tabs as a filesystem.
- **[rnpgp/rnp](https://github.com/rnpgp/rnp)** — RNP: high performance C++ OpenPGP library used by Mozilla Thunderbird
- **[getzola/zola](https://github.com/getzola/zola)** — A fast static site generator in a single binary with everything built-in. https://www.getzola.org
- **[GorvGoyl/Clone-Wars](https://github.com/GorvGoyl/Clone-Wars)** — 100+ open-source clones of popular sites like Airbnb, Amazon, Instagram, Netflix, Tiktok, Spotify, Whatsapp, Youtube etc. See source code, demo links, tech stack, github stars.
- **[jschauma/cs631apue](https://github.com/jschauma/cs631apue)** — Stevens Institute of Technology - CS631 Advanced Programming in the UNIX Environment
- **[valyala/fastjson](https://github.com/valyala/fastjson)** — Fast JSON parser and validator for Go. No custom structs, no code generation, no reflection
- **[zitadel/zitadel](https://github.com/zitadel/zitadel)** — ZITADEL - Identity infrastructure, simplified for you.
- **[josh-blake/pixie](https://github.com/josh-blake/pixie)** — A Raspberry Pi 5 GPS Time Disciplined Stratum 1 Time Server with PTP and Realtime Kernel
- **[petarov/neverstarget](https://github.com/petarov/neverstarget)** — A list of all your starred repos lists
