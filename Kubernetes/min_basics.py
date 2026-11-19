'''

What is an Operating System (OS)?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

An OS is a software program. It's the first and biggest program that runs on a computer, and its job is to manage the hardware and run all your other programs.


It's software, not a physical part.

A computer's hardware is just electronics. Nothing useful happens until some software tells the hardware what to do. When we press the power button, the first thing 
that starts is the OS.


The OS is made up of 2 parts:

* The Kernel: The core of the OS. It talks directly to the hardware, decides which program gets the CPU and how much memory each one gets, and handles files and 
              the network.

* Tools around the kernel: the shell and the commands (ls, cd, cat), plus the system settings.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

What an OS does?

The computer's hardware (CPU, memory, disk, network card) can't run Python code by itself. The OS sits between the hardware and programs and does the basic jobs:

- Starts and stops programs (processes).
- Gives each program some memory and CPU.
- Stores files on disk.
- Sends and receives network traffic.

    Python code  ->  OS (Linux / macOS / Windows)  ->  Hardware


---------------------------------------------------------------------------------------------------------------------------------------------------------------------

LINUX


Linux is software, so it has open source code on GitHub (mostly written in C).

The Linux kernel is nothing but the Linux project's code. But when people say "Linux" casually, they often mean the kernel plus the tools around it (the shell and 
commands like ls and cat). Those tools are separate programs, written by other projects, and they are not part of the kernel.


So the chain is:

    Engineer -> Shell -> Command -> Kernel -> Hardware

Commands like ls and cat are small programs that ask the OS to do something. We type them into a shell (bash or zsh), which reads the command and asks the
OS to run it.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Where does our code run?


NOTE: Almost all servers, including EC2 machines, EKS machines and containers, use Linux, not macOS or Windows.


Our code runs on a Mac while we develop (macOS is the OS). When it's deployed, it runs on Linux, because that's what servers use.
Linux is free and stable, and we can control it entirely from the command line without a screen.


'''
