# Emile Plastic - Project Instructions for Claude Code

## Project Overview
E-commerce website for plastic raw materials (B2B).
Belgian-based business selling Chinese plastic products to European customers.

## Tech Stack
- Frontend: React + TypeScript
- Backend: FastAPI (Python)
- Package Manager: UV (Python), npm (Frontend)
- AI: LangChain + LangGraph
- LLM: Grok API (testing)
- Vector DB: Cloud-based (TBD: Pinecone or Qdrant)
- CRM: HubSpot (free tier)
- Container: Docker
- CI/CD: GitHub Actions

## Rules for Claude Code
1. Every file must be decoupled — one responsibility per file
2. Never make decisions on your own — always ask first
3. Always create tests after building any feature
4. Never hardcode API keys — always use .env file
5. After finishing any task, show proof it works
6. Keep frontend and backend completely separate

## Languages
- English and Chinese (i18n support required)

## User Roles
- Admin: Emile (full access)
- Partner: Chinese partners (partial access)
- Customer: Buyers (public access)

## Chat Channels
- Live Chat (MVP first)
- Telegram Bot (MVP first)
- WhatsApp + Messenger (later)

## Key Customer Questions (chatbot must answer)
- Price of specific grade/product
- On-time delivery information
- Product quality certifications
- Shipment costs and conditions