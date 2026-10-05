# AbeyYaar

## Your AI Friend for Students

AbeyYaar is an open-source AI companion I am building for students.

The idea is simple: student life is not only about studying. There are placements, internships, resumes, career decisions, money, college life, family pressure, relationships, and a lot of everyday doubts.

Instead of building another chatbot that only gives answers, I want AbeyYaar to feel more like a helpful friend — someone a student can talk to when they need an answer, a plan, a second opinion, or simply someone to talk to.

The project is built around local AI using Ollama and Gemma, with a focus on privacy, practical help, and an architecture that can grow over time.

---

## What I want AbeyYaar to help with

The long-term idea covers different parts of student life:

### Career and Placement

- Career guidance
- Internship opportunities
- Resume review and building
- Placement preparation
- Interview preparation
- Project and skill suggestions

### Learning

- Skill learning
- Personalized learning paths
- Skill gap analysis
- Roadmaps
- Resources and project suggestions

### Decisions

- Laptop and phone buying decisions
- Product comparisons
- Budget planning
- Pros and cons of different choices
- Everyday decision support

### Student Life

- College life
- Hostel and PG related help
- Travel and basic college resources
- Money and expense management
- Templates and checklists for common tasks

### Personal Conversations

Students do not always come with technical questions.

Sometimes the conversation can be about feeling low, loneliness, family pressure, relationships, confusion, or simply having a bad day.

I want AbeyYaar to handle these conversations with empathy and appropriate safety boundaries rather than treating everything like a normal technical query.

---

## How the project works

The basic flow is designed around an AI companion core.

```text
User Input
    |
    v
Conversation Understanding
    |
    v
Intent Detection
    |
    +----------------------+
    |                      |
    v                      v
Personal Context       Decision Support
 / Memory                  |
    |                      |
    +----------+-----------+
               |
               v
        Safety Detection
               |
               v
       Agent / Tools
               |
               v
        Ollama + Gemma
               |
               v
     Personalized Response
```

The important part is that the model is not expected to handle everything by itself.

The agent can understand what the user is trying to do and route the request towards the relevant tool or capability.

---

## Local AI and Privacy

One of the main things I wanted to experiment with is local AI.

AbeyYaar uses:

- Ollama for running the model locally
- Gemma as the language model

The goal is to keep the basic AI experience on the user's own machine instead of depending on a paid remote AI API for every conversation.

This also makes the project useful for learning and experimenting with local LLMs, agents, memory, tools, and safety.

> Note: "Local" depends on how the application is configured and what external services are added in the future. The current design is centered around local model inference through Ollama.

---

## Agent Architecture

The project is organized around a few core ideas:

### Conversation Understanding

Understand what the user is actually asking instead of treating every message the same way.

### Intent Detection

Identify the general goal of the conversation and decide what kind of help is needed.

### Personal Context / Memory

Keep relevant student context so that future responses can become more useful and personalized.

### Decision Support

Help break down choices, compare options, and explain the reasoning behind a recommendation.

### Safety

Safety is an important part of the project, especially for conversations involving emotional distress or potentially harmful situations.

The goal is not to pretend that an AI can replace a trusted person or a professional. In serious situations, the system should encourage appropriate real-world support.

---

## Tools and Modules

The project is being designed around small, focused tools rather than putting everything inside one large agent file.

Some of the planned and current areas include:

- Career guidance
- Resume assistance
- Budget planning
- Learning and career roadmaps
- Decision support
- Student profile/context

This makes it easier to add new capabilities without rewriting the whole project.

---

## MVP

For the first major version, I am focusing on five core areas:

### 1. Career Copilot

- Resume review and building
- Internship and placement guidance
- Interview preparation
- Project ideas

### 2. Buying and Decision Assistant

- Laptop and phone recommendations
- Product comparison
- Budget planning
- Pros and cons
- Decision support

### 3. Skill Roadmap

- Personalized learning paths
- Skill gap analysis
- Learning resources
- Project suggestions
- Progress-oriented roadmaps

### 4. Student Life Helper

- College and hostel/PG related guidance
- Money management
- Everyday decision support
- Useful templates and checklists

### 5. Wellbeing and Safety

- Supportive conversations
- Handling loneliness and difficult situations
- Emotional support within appropriate boundaries
- Safety-aware responses
- Encouraging trusted-person or professional support when necessary

These areas represent the direction of the project. Some are already implemented while others are part of the roadmap.

---

## Project Structure

```text
AbeyYaar/
|
├── app/
│   ├── agent/
│   │   ├── agent.py
│   │   ├── intent.py
│   │   ├── memory.py
│   │   └── safety.py
│   |
│   ├── ollama/
│   │   └── client.py
│   |
│   ├── tools/
│   │   ├── career.py
│   │   ├── resume.py
│   │   ├── budget.py
│   │   ├── roadmap.py
│   │   └── decisions.py
│   |
│   ├── models/
│   │   └── schemas.py
│   |
│   └── main.py
|
├── data/
│   └── student_profile.json
|
├── frontend/
|
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Tech Stack

- Python
- Ollama
- Gemma
- HTML
- CSS
- JavaScript
- Git
- GitHub

The main backend and agent logic are written in Python. Ollama provides the local model runtime, while Gemma handles the language generation.

---

## Getting Started

### Requirements

Before running the project, make sure you have:

- Python 3.10 or newer
- Git
- Ollama

### Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd AbeyYaar
```

### Create a virtual environment

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Get the model

Make sure Ollama is installed and running, then:

```bash
ollama pull gemma4:e2b
```

### Run

```bash
python -m app.main
```

---

## Example Conversation

The terminal interface is intentionally simple.

```text
==============================
        Your AI Friend
==============================

You: Bhai placement ka darr hai

Friend: Tension mat le bhai. Step by step
prepare karte hain.

You: DSA karu kya?

Friend: Haan bhai, placement ke liye DSA
important hai.
```

The goal is not to make the conversation sound overly formal. I want the interaction to feel natural and useful.

---

## Current Status

This project is actively being built.

The current focus is getting the core agent, local model integration, basic tools, frontend, and student-focused workflows working reliably.

Some ideas described in this README are part of the planned direction and may not be fully implemented yet.

---

## Roadmap

- [x] Local Ollama integration
- [x] Gemma integration
- [x] Basic agent architecture
- [x] Intent handling
- [x] Safety layer
- [x] Student-focused tool structure
- [x] Terminal conversation
- [x] Frontend
- [ ] Better memory
- [ ] More career and placement tools
- [ ] Better resume workflows
- [ ] Improved product comparison
- [ ] More student-life utilities
- [ ] Better personalization
- [ ] Faster and more efficient responses
- [ ] More community-built tools

---

## Contributing

I want AbeyYaar to be an open-source project, so contributions are welcome.

You can contribute with:

- New student-focused tools
- Bug fixes
- Better prompts
- Agent improvements
- UI improvements
- Documentation
- Testing
- Ideas for useful student workflows

You do not need to build a huge feature to contribute. Even a small improvement can make the project better.

---

## A note from the builder

I started AbeyYaar because I wanted to build something that feels a little different from a typical AI chatbot.

There are already many AI tools that can answer questions. What I am interested in is building something that understands the context around student life and can help with the things that happen outside a textbook too.

This is still a work in progress. I am learning and improving the project as I build it, and I want the repository to grow with contributions and ideas from other developers.

The long-term goal is simple:

**Build an AI friend that students can actually find useful in real life.**

---

## License

This project is licensed under the MIT License.
