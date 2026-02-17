'''

MCP is a standard way for LLMs to securely connect to external tools, data sources, and services at runtime.

Model Context Protocol (MCP) is a standardized framework introduced by Anthropic in 2024. It acts as a universal bridge between LLMs and external
tools, APIs, or data sources. Instead of building custom integrations for each system, MCP provides a consistent communication layer that lets
AI applications access real world information in a structured, secure and scalable way.


Why we Need MCP?

Unified Connectivity: Eliminates repetitive, service specific integrations by offering a single protocol for all tools and data sources.

Core components of MCP Architecture

1. MCP Host - The AI app we use (Ex: App code in VSC, etc)
2. MCP client - the connector between host and server
3. MCP Server - the source of data or context.


'''