import sys

from reportlab.lib.colors import Color, HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

FONT_DIR = "/System/Library/Fonts/Supplemental/"
pdfmetrics.registerFont(TTFont("TNR", FONT_DIR + "Times New Roman.ttf"))
pdfmetrics.registerFont(TTFont("TNR-B", FONT_DIR + "Times New Roman Bold.ttf"))
pdfmetrics.registerFont(TTFont("TNR-I", FONT_DIR + "Times New Roman Italic.ttf"))
pdfmetrics.registerFont(TTFont("TNR-BI", FONT_DIR + "Times New Roman Bold Italic.ttf"))
pdfmetrics.registerFont(TTFont("Arial-B", FONT_DIR + "Arial Bold.ttf"))
pdfmetrics.registerFontFamily("TNR", normal="TNR", bold="TNR-B", italic="TNR-I", boldItalic="TNR-BI")

NAVY = HexColor("#1A1A2E")
SKILL = HexColor("#1F2937")
RULE = Color(0.122, 0.306, 0.475)

OUT = sys.argv[1] if len(sys.argv) > 1 else "Harsha_Resume_9390003039.pdf"
SCALE = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0

BODY = 10 * SCALE
LEAD = 11.6 * SCALE

name_style = ParagraphStyle("name", fontName="Arial-B", fontSize=18, leading=21, alignment=TA_CENTER, textColor=NAVY)
contact_style = ParagraphStyle("contact", fontName="TNR", fontSize=10, leading=12, alignment=TA_CENTER)
section_style = ParagraphStyle("section", fontName="TNR-B", fontSize=11.5, leading=13, spaceBefore=4 * SCALE)
body_style = ParagraphStyle("body", fontName="TNR", fontSize=BODY, leading=LEAD, alignment=TA_JUSTIFY)
skill_style = ParagraphStyle("skill", fontName="TNR", fontSize=BODY, leading=LEAD, textColor=SKILL, leftIndent=0, alignment=TA_JUSTIFY)
bullet_style = ParagraphStyle(
    "bullet", fontName="TNR", fontSize=BODY, leading=LEAD, textColor=NAVY, alignment=TA_JUSTIFY,
    leftIndent=20, bulletIndent=4, bulletFontName="TNR", bulletFontSize=BODY, spaceAfter=0.6 * SCALE,
)
role_left = ParagraphStyle("role_l", fontName="TNR-B", fontSize=11, leading=13)
role_right = ParagraphStyle("role_r", fontName="TNR-I", fontSize=9.5, leading=13, alignment=TA_RIGHT)
project_style = ParagraphStyle("project", fontName="TNR-I", fontSize=BODY, leading=LEAD, spaceAfter=1)

story = []


def section(title):
    story.append(Paragraph(title, section_style))
    story.append(HRFlowable(width="100%", thickness=1, color=RULE, spaceBefore=1, spaceAfter=3 * SCALE))


def role(org, title, where_when, project=None):
    t = Table(
        [[Paragraph(f"{org} | <i><font name='TNR-I'>{title}</font></i>", role_left), Paragraph(where_when, role_right)]],
        colWidths=["62%", "38%"],
    )
    t.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 3 * SCALE), ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
        ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
    ]))
    story.append(t)
    if project:
        story.append(Paragraph(project, project_style))


def bullets(items):
    for it in items:
        story.append(Paragraph(it, bullet_style, bulletText="\u2022"))


story.append(Paragraph("MANO HARSHA DAVULURI", name_style))
story.append(Spacer(1, 3))
story.append(Paragraph(
    "+91 9390003039 | manoharsha44@gmail.com | www.linkedin.com/in/mano-harsha-davuluri | Bengaluru, India",
    contact_style,
))

section("PROFESSIONAL SUMMARY")
story.append(Paragraph(
    "Results-driven <b>NITian</b> and <b>AI &amp; Data Engineer</b> with 3 years of experience building production "
    "Generative AI applications and scalable data platforms. Specializes in agentic AI (MCP, LLM tool-calling, RAG "
    "with vector search), LLMOps with MLflow, and FastAPI services on Databricks, with a strong foundation in Spark, "
    "AWS, data lakes, and ETL pipelines. Architected and launched an enterprise conversational AI assistant that "
    "enables natural-language data discovery across data assets, products, and domains. Proven track record of "
    "leading cross-functional teams and driving AI-led innovation with data governance at enterprise scale.",
    body_style,
))

section("TECHNICAL SKILLS")
skills = [
    ("Generative AI &amp; Agents",
     "Agentic AI, Multi-agent Systems (Agent-to-Agent), RAG, MCP (FastMCP), LangChain, LangGraph, ChatDatabricks, "
     "LLMs (Claude, Llama), Prompt Engineering, Guardrails, Embeddings, Hybrid Search (pgvector HNSW, RRF)."),
    ("LLMOps &amp; AI Platforms",
     "MLflow 3 (Tracing, LLM Judges), Model Serving, AI Gateway (Routing, Fallbacks), Databricks Apps."),
    ("Cloud &amp; Platforms",
     "Databricks (Unity Catalog, Lakebase, Delta Lake, SQL Warehouses), AWS (S3, Lambda, EKS/Kubernetes)."),
    ("Data Engineering",
     "Apache Spark, PySpark, Spark SQL, Delta Lake, Brickflow, SparkExpectations, DBT, Informatica CDGC."),
    ("Data Modeling",
     "Dimensional Modeling, Star/Snowflake Schema, SCD Type 1/2, Medallion, Lakehouse, Data Governance."),
    ("Programming &amp; DevOps",
     "Python, SQL, FastAPI Microservices, Git, Docker, Jenkins CI/CD, OAuth 2.0 (Okta, M2M), pytest."),
]
for label, value in skills:
    story.append(Paragraph(f"<b>{label}:</b> {value}", skill_style))

section("PROFESSIONAL EXPERIENCE")
role("Nike", "Software Engineer II \u2013 AI", "Bengaluru, India | Jan 2026 \u2013 Present",
     project="Compass AI \u2013 Agentic chatbot for Nike\u2019s enterprise data catalog")
bullets([
    "Developed and extended an <b>MCP (Model Context Protocol)</b> server on Databricks Apps for a <b>LangChain AI agent</b> "
    "powered by <b>Claude Sonnet 4.5 (Anthropic)</b>, growing it to <b>12 LLM-callable tools</b>, incl. a <b>multi-agent</b> "
    "(agent-to-agent) tool calling Nike\u2019s AirTalk chatbot on the user\u2019s behalf via <b>Okta OAuth</b>, and tools "
    "for AI-proposed data products, docs lookup, and catalog stats.",
    "Created retrieval tools over <b>Lakebase (Postgres)</b> with <b>hybrid semantic search</b> (pgvector + "
    "full-text via <b>Reciprocal Rank Fusion</b>) and safe SQL access; replaced an external REST API with direct "
    "table queries, removing a network hop and its auth.",
    "Instrumented end-to-end <b>MLflow 3 tracing</b>, propagating request/session IDs from FastAPI to the MCP server "
    "via HTTP headers to group each multi-turn chat into one session, scored by <b>LLM-as-a-judge</b> evaluators "
    "(completeness, role adherence, tool-call efficiency, user frustration) with time-to-first-token monitoring.",
    "Configured <b>Databricks AI Gateway</b> with weighted <b>traffic splitting</b> (70% Claude Sonnet 4.6, 30% Claude "
    "Opus 5.5) and session-sticky routing, plus an automatic <b>fallback</b> to Llama 3.3 70B for high availability; "
    "added Anthropic <b>prompt caching</b> to cut token cost and latency.",
    "Crafted the agent\u2019s <b>system prompt and guardrails</b>: scope restriction to Nike metadata, "
    "non-disclosure of internals, correct bot identity, and accurate deep links to products, assets, and metrics.",
    "Productionized the MCP server across <b>dev/QA/prod</b> with <b>Jenkins CI/CD</b>, per-env config, "
    "<b>service-principal OAuth M2M</b>, and Cerberus secrets; retired a legacy MCP server and scheduled "
    "access-scope and vector index refresh jobs.",
    "Shipped <b>FastAPI</b> chatbot features: chat-history APIs (sessions, timestamped recent queries, per-session "
    "limits), a live health endpoint for UI \u201cOnline\u201d status, and resilient ServiceNow ticketing, at a "
    "<b>90% test coverage</b> gate.",
    "Built medallion <b>ETL pipelines</b> (Spark, Brickflow) and a gold-layer <b>dimensional model</b> "
    "(22 dims, 5 facts) with SparkExpectations DQ rules, grounding the agent across <b>100,000+</b> data assets.",
])

role("Epsilon (Publicis Groupe)", "Data Engineer", "Bengaluru, India | Aug 2023 \u2013 Dec 2025")
bullets([
    "Designed a comprehensive Data Quality framework for the Prospect project, featuring automated discrepancy "
    "detection and real-time alerting mechanisms to ensure data integrity and compliance.",
    "Constructed scalable ETL/ELT data solutions processing over 150+ billion records daily into data lakes and "
    "warehouses using Spark, and trained ML models that enhanced decision-making, driving a 25% boost in quarterly revenue.",
    "Optimized and tuned Spark jobs for large-scale datasets (30+ TB), applying performance best practices and "
    "reducing infrastructure costs by 46%.",
    "Partnered with cross-functional teams to define data governance standards and set up CI/CD pipelines for "
    "data workflows.",
    "Owned end-to-end data pipelines spanning ingestion, extract-transform-load processes, data archiving, "
    "warehousing and recurring reporting using Apache Spark on Databricks Delta tables.",
    "Worked closely with solution architects and business stakeholders to design and deploy complex ML models for "
    "predictive analytics and BI solutions.",
])

section("CERTIFICATIONS")
bullets([
    "Databricks Certified AI Engineer Associate \u2013 Databricks (Issued 2026)",
    "Databricks Certified Data Engineer Associate \u2013 Databricks (Issued 2023)",
])

section("EDUCATION")
story.append(Paragraph(
    "National Institute of Technology (NIT) Karnataka <font name='TNR-I' size='9.5'>| Aug 2019 - May 2023</font>",
    role_left,
))
story.append(Paragraph("Bachelor of Technology | Surathkal, Karnataka", body_style))

doc = SimpleDocTemplate(
    OUT, pagesize=letter, leftMargin=28, rightMargin=34, topMargin=10, bottomMargin=10,
    title="Mano Harsha Davuluri - Resume", author="Mano Harsha Davuluri",
)
doc.build(story)

from pypdf import PdfReader
print("pages:", len(PdfReader(OUT).pages))
