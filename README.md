# AI Learnings

A collection of hands-on AI agent projects for learning and experimentation.

## Projects

### [Finance Research Crew](crew/financial_researcher/README.md)

A multi-agent financial research system built with CrewAI. Give it a company name, and the crew researches the business using recent web sources before producing a structured financial report with market insights.

### [Debate Crew](crew/debate/README.md)

A multi-agent debate simulator built with CrewAI. Give it a motion and two debaters argue for and against it; an impartial judge then declares a winner.

### Deep Research Agent

This project is a simple multi-agent research workflow built using the OpenAI Agents SDK.

## Agents

### 1. Planner Agent

* Takes the user's query.
* Creates a search plan.
* Generates 3 search terms to research the topic.

### 2. Search Agent

* Performs web searches using `WebSearchTool`.
* Runs all searches in parallel using `asyncio`.
* Returns a short summary for each search result.

### 3. Writer Agent

* Takes the search summaries.
* Combines the information into a detailed report.
* Generates:

  * A short summary
  * A markdown report
  * Follow-up questions

### 4. Email Agent

* Converts the report into HTML.
* Sends the report using the email tool.

### 5. Email Tool

* Uses SendGrid to send the email.

## Flow

1. User provides a research query.
2. Planner Agent creates a search plan.
3. Search Agent performs the searches in parallel.
4. Writer Agent creates the final report.
5. Email Agent sends the report by email.

## Possible Improvements

1. **More Search Rounds**

   * Let the system perform additional searches if more information is needed.

2. **Add References**

   * Include source links and citations in the final report.

3. **Better Search Planning**

   * Use more or fewer searches depending on the complexity of the query.

4. **Research Feedback Loop**

   * Add a Critic Agent between the Search Agent and Writer Agent.
   * The Critic Agent reviews the search results and checks whether they provide enough coverage for the original query.
   * If important topics are missing, it generates additional search queries and triggers another search round.
   * Once the research is considered complete, the results are passed to the Writer Agent.
5. **Make the Agent Autonomous with tools, Handoffs, Guardrails 🤖**
