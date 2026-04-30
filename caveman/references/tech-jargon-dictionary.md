# Tech Jargon Dictionary

Plain-English definitions for 200+ technical terms. Use this when `/caveman:explain` needs to define a term, or when `/caveman:smash` needs a replacement.

Format: **Term** — Plain definition. *One-sentence analogy where helpful.*

---

## A

**Abstraction** — A simplified version of something complex that hides the messy details underneath. *Like a car's steering wheel — you turn it, and the car steers. You don't need to know about the steering column.*

**Agile** — A way to build software in small chunks, testing and improving as you go, instead of planning everything upfront.

**Algorithm** — A list of steps to solve a problem. *Like a recipe, but for a computer.*

**API (Application Programming Interface)** — A defined way for two programs to talk to each other. *Like a menu at a restaurant — you ask for what you want, and the kitchen sends it back.*

**Asynchronous** — Something that runs in the background without making you wait. *Like sending a text and getting a reply later, instead of calling and waiting on the line.*

**Authentication** — Proving who you are. Usually: username + password.

**Authorization** — Checking what you're allowed to do after you've proven who you are.

**Auto-scaling** — A system that adds more servers automatically when traffic increases, and removes them when traffic drops.

---

## B

**Backend** — The part of an app that runs on the server. Users don't see it, but it stores data and does the main work.

**Bandwidth** — How much data can move through a connection at once. Also misused in meetings to mean "time available."

**Boilerplate** — Standard code that gets copied and used as a starting template. Not clever — just necessary.

**Branch (git)** — A separate copy of the code where you can make changes without affecting the main version.

**Bug** — A mistake in the code that causes unexpected behavior.

**Build** — The process of converting source code into a working program.

---

## C

**Cache** — A temporary storage spot for data you use a lot, so you don't have to fetch it from the original source every time. *Like keeping a pen on your desk instead of walking to the supply closet each time.*

**CI/CD (Continuous Integration / Continuous Deployment)** — An automated system that builds, tests, and ships code every time a developer makes a change.

**CLI (Command-Line Interface)** — A text-based way to interact with a program by typing commands. No buttons, just text.

**Cloud** — Someone else's server, rented over the internet.

**Code review** — When one developer reads another developer's code to catch mistakes before it ships.

**Commit** — A saved snapshot of changes to the code. *Like a checkpoint in a video game.*

**Container** — A packaged version of an app that includes everything it needs to run, so it works the same anywhere.

**CRUD** — Create, Read, Update, Delete. The four basic operations for any database.

**CSS (Cascading Style Sheets)** — The code that controls how a webpage looks: colors, fonts, layout.

---

## D

**Database** — An organized place to store and retrieve information.

**Debugging** — Finding and fixing bugs in code.

**Dependency** — A piece of code your program needs from somewhere else to work.

**Deploy** — To put a working version of an app onto a server so people can use it.

**Deprecate** — To mark something as old and no longer supported. It still works, but you should stop using it.

**Docker** — A tool that packages apps into containers so they run the same everywhere.

**Domain** — A website address (like example.com).

**DRY (Don't Repeat Yourself)** — A coding principle: if you write the same logic twice, combine it into one place.

---

## E

**Endpoint** — A specific URL in an API where you send requests. *Like a specific window at a post office.*

**Environment** — The settings and tools needed to run an app in a specific context (development, testing, production).

**Error handling** — Code that catches problems and responds gracefully instead of crashing.

---

## F

**Feature flag** — A switch that lets you turn a feature on or off without deploying new code.

**Framework** — A pre-built collection of code that handles common tasks, so you don't build everything from scratch.

**Frontend** — The part of an app that users see and interact with. HTML, CSS, and JavaScript live here.

**Function** — A named block of code that performs a specific task. You can call it repeatedly instead of writing the same code over and over.

---

## G

**Git** — A system that tracks changes to code over time, so you can go back to any previous version.

**GitHub / GitLab** — Websites that host git repositories and help teams collaborate on code.

**GraphQL** — A way to request data from a server where you specify exactly what you need. Less data wasted compared to REST.

---

## H

**Hash** — A fixed-size code generated from any data. Same input always gives the same hash. *Like a fingerprint for data.*

**HTTP / HTTPS** — The protocol for sending data between a browser and a server. HTTPS is the secure version.

**Hotfix** — An emergency fix shipped quickly to address a critical bug in production.

---

## I

**IDE (Integrated Development Environment)** — A text editor built for writing code, with tools like auto-complete, error highlighting, and debugging.

**Idempotent** — An operation you can run multiple times and get the same result. *Like pressing the elevator button more than once — it doesn't summon two elevators.*

**Index (database)** — A shortcut that makes database lookups faster. *Like the index at the back of a book.*

**Infrastructure** — The servers, networks, and tools that an app runs on.

**Integration test** — A test that checks whether multiple parts of the app work correctly together.

---

## J

**JSON (JavaScript Object Notation)** — A simple, readable format for sending structured data between systems. Looks like `{"key": "value"}`.

**JWT (JSON Web Token)** — A compact, signed token used to prove identity. *Like a signed ticket that proves you paid.*

---

## K

**Kubernetes (K8s)** — A system that manages containers across many servers, automatically restarting failed containers and spreading the load.

---

## L

**Latency** — The time between sending a request and getting a response. *How long it takes for your ping to come back.*

**Library** — A collection of pre-written code you can include in your project to add specific functionality.

**Load balancer** — A system that spreads incoming traffic across multiple servers so no single server gets overwhelmed.

**Logging** — Recording what an app does over time, so you can diagnose problems later.

---

## M

**Merge** — Combining changes from one branch of code into another.

**Microservice** — A small, independent service that does one specific job. Apps are built from many microservices instead of one large program.

**Migration** — Moving data from one database structure (or system) to another.

**Mock** — A fake version of something (like a database or API) used in tests so you don't need the real thing.

**Monolith** — A single large codebase where everything is tightly connected. The opposite of microservices.

---

## N

**Node** — A single server or machine in a network.

**NPM** — A tool for installing JavaScript packages (libraries of code).

---

## O

**OAuth** — A standard way to let users sign in to one app using their account from another app (like "Sign in with Google").

**Open source** — Code that anyone can read, use, and modify freely.

**ORM (Object-Relational Mapper)** — A tool that lets you interact with a database using your programming language instead of SQL.

---

## P

**Package** — A bundle of code that adds specific functionality to your project.

**Pipeline** — A series of automated steps that code goes through: build → test → deploy.

**Production** — The live environment where real users access the app.

**Pull request (PR)** — A request to merge your code changes into the main branch. Others review it first.

---

## Q

**Query** — A request to a database to get, add, change, or delete data.

**Queue** — A waiting line for tasks. *Like a checkout line at a store — tasks are processed in order.*

---

## R

**Refactor** — Restructuring existing code to be cleaner or simpler without changing what it does.

**Regression** — A bug introduced by a recent change that broke something that previously worked.

**Repository (repo)** — A folder that holds all the code for a project, tracked by git.

**REST** — A standard way to build APIs using HTTP. Each resource has a URL, and you use HTTP verbs (GET, POST, PUT, DELETE) to interact with it.

**Rollback** — Reverting to a previous version of the code or database after a bad deployment.

**Runtime** — The time when a program is actually running (as opposed to compile time, when it's being built).

---

## S

**Schema** — A defined structure for data — what fields exist, what types they are.

**SDK (Software Development Kit)** — A package of tools that makes it easier to build apps for a specific platform or service.

**Serverless** — Running code without managing servers. You write the function; the cloud provider handles everything else.

**SQL (Structured Query Language)** — A language for talking to relational databases. You write statements like `SELECT name FROM users WHERE age > 30`.

**SSH (Secure Shell)** — A secure way to connect to a remote server from your terminal.

**Staging** — A copy of the production environment used for testing before a real release.

**State** — The current condition of a system or component. *What's happening right now.*

**Synchronous** — Operations that run one at a time, in order. You wait for each to finish before starting the next.

---

## T

**TDD (Test-Driven Development)** — Writing tests before writing the code. The tests define what the code must do.

**Technical debt** — Shortcuts taken now that will slow you down later. *Like borrowing money — it's fine short-term but you pay interest.*

**Token** — A piece of data that proves identity or grants access. *Like a ticket.*

**TypeScript** — JavaScript with type checking added. It catches type mistakes before the code runs.

---

## U

**Unit test** — A test that checks a single small piece of code in isolation.

**URL (Uniform Resource Locator)** — A web address.

---

## V

**Version control** — A system for tracking every change ever made to a file, with the ability to go back to any previous state.

**VPN (Virtual Private Network)** — A secure tunnel that connects your device to a private network over the internet.

---

## W

**Webhook** — A way for one app to automatically notify another when something happens. *Like setting up a notification: "call me when X happens."*

**WebSocket** — A persistent connection between a browser and a server that lets both sides send messages at any time. Used for real-time features like chat.

---

## X

**XML (eXtensible Markup Language)** — An older data format, similar to JSON but more verbose. Looks like `<key>value</key>`.

---

## Y / Z

**YAML** — A human-readable format for writing configuration. Used in Docker, Kubernetes, CI/CD pipelines.

**Zero-downtime deployment** — Releasing new code without taking the app offline. Users never see a disruption.
