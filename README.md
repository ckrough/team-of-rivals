# Team of Rivals: AI Decision-Making Framework

A strategic decision-making framework inspired by Abraham Lincoln's "Team of Rivals" approach, implemented as Claude AI Skills. Get diverse, adversarial perspectives on your decisions instead of a single AI viewpoint.

## Why This Exists

Most AI assistants provide a single perspective. But the best decisions come from productive disagreement—where different viewpoints challenge assumptions, expose blind spots, and force rigorous thinking.

This framework creates five distinct AI personas that analyze your decisions from different angles:
- **APEX** (The Visionary) - Expands possibilities, ignores constraints
- **VETO** (The Skeptic) - Demands evidence, calculates risks
- **FORGE** (The Operator) - Maps resources, grounds in reality
- **COMPASS** (The Ethicist) - Evaluates stakeholder impact, long-term consequences
- **Domain Expert** - Provides specialized technical, financial, or industry depth

## How It Works

These are [Claude AI Skills](https://support.anthropic.com/en/articles/9950645-what-are-skills-in-claude-ai) - specialized personas you can invoke in conversation with Claude. Each skill applies structured analytical frameworks to your decisions and argues from genuine conviction, creating productive tension rather than false consensus.

### Installation

1. Clone this repository
2. In Claude AI (claude.ai), navigate to your Skills settings
3. Import the skills from the `team-of-rivals/` directory
4. Each skill can now be invoked during conversations

### Using the Skills

**For a single perspective:**
```
Invoke the APEX skill and analyze this opportunity: [your decision]
```

**For comprehensive analysis (recommended):**
```
I need to decide whether to [your decision].

Please analyze this using:
1. APEX (visionary perspective)
2. VETO (skeptical analysis)
3. FORGE (operational reality)
4. COMPASS (ethical evaluation)
5. Domain Expert (specify: technical/financial/legal/market)

Then synthesize the perspectives.
```

## The Team

### APEX - The Visionary
**When to use:** Expanding possibilities, challenging constraints, identifying transformative opportunities

**Approach:**
- Questions every limitation as negotiable
- Frames problems as market opportunities worth billions
- References moonshot examples (SpaceX, Amazon, Tesla)
- Pushes for platform plays over point solutions
- Thinks 10x, not 10%

**Output:** Vision expansion, market creation potential, platform strategy, capital requirements

---

### VETO - The Skeptic
**When to use:** Evaluating risks, stress-testing assumptions, demanding evidence

**Approach:**
- Demands quantifiable evidence for every claim
- Calculates failure probabilities and worst-case scenarios
- Identifies survivorship bias and hidden assumptions
- Models second and third-order effects
- References historical failures with similar characteristics

**Output:** Risk assessment, evidence quality analysis, base rate reality, failure scenarios

---

### FORGE - The Operator
**When to use:** Assessing feasibility, planning execution, resource allocation

**Approach:**
- Maps required resources (time, money, people, infrastructure)
- Identifies critical path dependencies and bottlenecks
- Calculates burn rates and runway
- Defines MVP and iteration velocity
- Focuses on what's actually buildable

**Output:** Resource requirements, execution timeline, burn analysis, MVP definition, operational risks

---

### COMPASS - The Ethicist
**When to use:** Evaluating values alignment, long-term consequences, stakeholder impact

**Approach:**
- Evaluates impact on all stakeholders, not just shareholders
- Assesses 10+ year reputation trajectory
- Questions incentive alignment and moral hazard
- Considers regulatory evolution
- Applies frameworks like Rawls' veil of ignorance

**Output:** Stakeholder impact, ethical assessment, reputation trajectory, regulatory risks, cascade effects

---

### Domain Expert - Adaptive Specialist
**When to use:** Decisions requiring specific technical, financial, legal, or industry expertise

**Approach:**
- Automatically adapts to decision context
- Rotates between: CTO, CFO, General Counsel, Industry Veteran, CPO, CDO, CPO
- Provides depth where others provide breadth
- Knows domain-specific gotchas and unwritten rules

**Output:** Domain-specific assessment, critical insights, integration with other perspectives, blind spots

## Example Use Cases

### Startup Strategy
- **APEX**: Platform opportunity, market creation potential
- **VETO**: Base rate of startup success, failure modes
- **FORGE**: Burn rate, MVP scope, hiring timeline
- **COMPASS**: Stakeholder impact, reputation risks
- **Expert** (CFO): Unit economics, funding strategy

### Product Launch
- **APEX**: Market expansion opportunity, network effects
- **VETO**: Historical product success rates, assumptions
- **FORGE**: Development timeline, resource needs
- **COMPASS**: User impact, ethical considerations
- **Expert** (CPO): Product-market fit signals, feature prioritization

### Technical Architecture Decision
- **APEX**: Scalability to billions, platform potential
- **VETO**: Complexity risks, vendor lock-in
- **FORGE**: Implementation timeline, team capabilities
- **COMPASS**: Open source vs proprietary ethics
- **Expert** (CTO): Technical debt, scaling patterns

## Key Principles

1. **Genuine Disagreement**: Each persona argues with conviction, even if outnumbered
2. **No False Consensus**: Productive tension is the goal, not agreement
3. **Evidence-Based**: VETO demands data; others must respond with facts
4. **Long-Term Thinking**: COMPASS and APEX consider 10-20 year horizons
5. **Execution Reality**: FORGE keeps visions grounded in what's buildable

## Decision Synthesis

After gathering all perspectives:

1. **Unanimous Agreement** - Rare but powerful signals (proceed with confidence)
2. **Irreconcilable Tensions** - Identify where judgment calls are required
3. **Risk-Adjusted Recommendations** - Weight each perspective's concerns
4. **Action Items** - Extract concrete next steps

## Contributing

This framework is designed to evolve. Contributions welcome:
- Refining existing persona frameworks
- Adding new analytical tools to each skill
- Creating new rival personas for specific domains
- Sharing decision synthesis patterns

## Inspiration

Abraham Lincoln assembled a cabinet of his political rivals—people who disagreed with him and each other. This created productive tension that led to better decisions during America's most critical period. This framework applies that principle to AI-assisted decision-making.

## License

This project is open source. Use it to make better decisions.
