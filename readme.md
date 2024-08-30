# Linear Algebra AI Teaching Assistant

## Introduction

An AI chatbot specializing in linear algebra. It supports rapid deployment and replaces backend LLM according to different hardware conditions.

## Author
- Haisheng Wang, East China Normal University
- Zeyuan Lai, University of Science and Technology of China
- Hongzhi Wan, Nanjing University

## Background

Since its launch in 2022, ChatGPT has brought large language models into everyday use, helping university faculty and students with questions and problems. Despite the continuous enhancement of general-purpose pre-trained language models, their professional capabilities in research, teaching, and learning still show some limitations. To make large language models more effective for university education, our team has developed an "AI Teaching Assistant" using the MindSpore framework, the RAG knowledge base, and the Qwen2 pre-trained model. This assistant is equipped with strong professional skills and a comprehensive interactive interface, which not only alleviates the teaching workload of educators but also significantly improves student learning outcomes.

Currently, the knowledge base of our project consists of a dataset of over 200,000 words, crafted by our team. When integrated with the large model, it has demonstrated exceptional results in the field of linear algebra. Moving forward, our team will focus on enhancing the AI Teaching Assistant's generalization capabilities by incorporating academic papers, textbooks, reference materials, exam questions, and other resources directly into the RAG knowledge base, enabling students from different majors and grade levels to use it effectively.

## Usage

### Start the Frontend Server

We recommend using [nvm](https://github.com/nvm-sh/nvm) to manage versions of Node.js and [pnpm](https://pnpm.io/) to manage packages.

```sh
$ nvm use 20
$ pwd
/path/to/repo/ai-navigator
$ pnpm install
$ pnpm run dev
```

### Start the Backend Server

```sh
$ pwd
/path/to/repo/chat
$ sh server.sh
```