"""

Comparison: LangChain Agent vs Chains (LLMChain, SequentialChain) vs chatDatabricks()
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


| Feature                    | LangChain Agent (initialize_agent)                          | Chains (LLMChain, SequentialChain)                          | chatDatabricks()                                |
| -------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------- |

| Core Idea                  | Autonomous agent that dynamically decides how to solve tasks | Predefined pipelines of prompts and models                  | Direct LLM call hosted on Databricks            |

| Tool Use                   | Yes - can call external tools (search, calculator, APIs, DBs)| No - only prompt -> LLM -> output                           | No - just model response                        |

| Planning                   | Adaptive reasoning loop (decides steps at runtime)          | None in LLMChain; fixed sequence in SequentialChain         | None - single response                          |

| Memory                     | Short-term + long-term memory integration                   | Limited (can store context manually)                        | Session-based only                              |

| Middleware / Guardrails    | Supports retries, summarization, human-in-the-loop          | Not built-in                                                | Not built-in                                    |

| Workflow Style             | Flexible, autonomous, multi-step                            | Deterministic, fixed pipeline                               | Simple, direct                                  |

| Best For                   | Complex workflows, automation, research assistants          | Simple Q&A, structured multi-step tasks                     | Quick chat/Q&A integrated with Databricks       |

| Invocation                 | agent.run("task") -> agent decides workflow                 | llm_chain.run("input") or seq_chain.run("input") -> fixed flow | chatDatabricks().run("prompt") -> direct output |





Main difference is Tool Use is possible in LangChain Agent but not in Chains (LLMChain, SequentialChain) and chatDatabricks().

"""
