# Operational Excellence Playbook

## Execution Velocity Patterns

### The Amazon Two-Pizza Team Rule
**Principle**: Teams small enough to be fed by two pizzas
**Implementation**:
- 6-8 person maximum
- Full ownership of service
- Direct customer feedback
- Independent deployment
- Separate P&L if possible

**Metrics**:
- Decision speed: <24 hours
- Deploy frequency: Multiple per day
- Time to market: <6 weeks for new features
- Meeting overhead: <20% of time

### The Spotify Squad Model
**Structure**:
- Squads: 5-9 people owning feature
- Tribes: Collection of squads (<100 people)
- Chapters: Skill-based groups (engineering, design)
- Guilds: Interest-based communities

**Benefits**:
- Autonomous execution
- Cross-functional collaboration
- Knowledge sharing
- Reduced dependencies

## Resource Optimization Patterns

### AWS Working Backwards
**Process**:
1. Write press release first
2. Write FAQ document
3. Define customer experience
4. Only then build

**Resource Impact**:
- Reduces wasted development by 60%
- Clarifies resource needs upfront
- Prevents feature creep
- Aligns team on outcome

### Toyota Kata
**Improvement Cycle**:
1. Understand direction
2. Grasp current condition
3. Define next condition
4. Iterate toward target

**Daily Questions**:
- What is the target condition?
- What is actual condition now?
- What obstacles prevent target?
- What is next step?
- When can we see what we learned?

## Operational Scaling Stages

### Stage 1: Founder Mode (0-10 people)
**Characteristics**:
- Everyone does everything
- Direct communication
- No process needed
- Speed over structure

**Resource Profile**:
- Burn: $50-150K/month
- Runway target: 18 months
- Hiring: Generalists only
- Infrastructure: Off-the-shelf

### Stage 2: Early Team (10-30 people)
**Characteristics**:
- Specialization emerges
- First processes required
- Communication breaks
- Culture solidifies

**Resource Profile**:
- Burn: $150-500K/month
- Runway target: 12-18 months
- Hiring: Senior individuals
- Infrastructure: Some custom

### Stage 3: Growth (30-100 people)
**Characteristics**:
- Middle management layer
- Process becomes critical
- Silos form
- Efficiency matters

**Resource Profile**:
- Burn: $500K-2M/month
- Runway target: 12+ months
- Hiring: Teams not individuals
- Infrastructure: Platform investment

### Stage 4: Scale (100+ people)
**Characteristics**:
- Multiple business units
- Heavy process
- Innovation slows
- Optimization focus

**Resource Profile**:
- Burn: $2M+/month
- Runway: Cash flow positive
- Hiring: Organizational capability
- Infrastructure: Enterprise grade

## Critical Path Optimization

### Theory of Constraints (TOC)
**Five Focusing Steps**:
1. Identify constraint
2. Exploit constraint
3. Subordinate to constraint
4. Elevate constraint
5. Repeat

**Application**:
- Engineering bottleneck → Hire senior engineers
- Sales bottleneck → Improve lead quality
- Customer success bottleneck → Build self-service
- Cash bottleneck → Extend runway or grow revenue

### PERT Analysis
**Three-Point Estimation**:
```
Expected Time = (Optimistic + 4×Likely + Pessimistic) / 6
Standard Deviation = (Pessimistic - Optimistic) / 6
```

**Buffer Calculation**:
- 68% confidence: Expected + 1σ
- 95% confidence: Expected + 2σ
- 99% confidence: Expected + 3σ

## Burn Rate Management

### The 40% Rule
**Formula**: Growth Rate + Profit Margin ≥ 40%

**Examples**:
- 100% growth, -60% margin = 40% (Acceptable)
- 20% growth, 10% margin = 30% (Concerning)
- 50% growth, 0% margin = 50% (Good)

### Default Alive Calculator
```python
def months_to_default_alive(cash, burn_rate, revenue, growth_rate):
    months = 0
    while cash > 0 and revenue < burn_rate:
        cash -= (burn_rate - revenue)
        revenue *= (1 + growth_rate)
        burn_rate *= 0.98  # Assume 2% efficiency gain
        months += 1
    return months if revenue >= burn_rate else -1
```

### Pivot Triggers
**Hard Pivots Required When**:
- <6 months runway, no funding in sight
- CAC payback >18 months
- Churn >10% monthly
- Growth <20% with negative margins

**Soft Pivots Considered When**:
- NPS <30
- Sales cycle lengthening
- Competition gaining 2x faster
- Key assumptions proven false

## MVP Execution Templates

### Wizard of Oz MVP
**When to Use**:
- Complex automation needed
- Uncertain about solution
- High cost to build

**Implementation**:
1. Build simple frontend
2. Humans perform backend
3. Measure actual usage
4. Automate only proven paths
5. Maintain manual fallback

**Example**: Zappos started by posting shoes from local stores

### Concierge MVP
**When to Use**:
- B2B or high-touch B2C
- Complex customer needs
- Relationship-driven sale

**Implementation**:
1. Manually onboard each customer
2. Personally deliver value
3. Document every step
4. Identify patterns
5. Scale proven patterns only

**Example**: Airbnb founders personally photographed listings

### Smoke Test MVP
**When to Use**:
- Demand validation needed
- Low cost to test
- Clear value proposition

**Implementation**:
1. Create landing page
2. Drive traffic (paid/organic)
3. Measure conversion to "buy"
4. Show "coming soon"
5. Build only if demand proven

**Example**: Dropbox video before building product

## Operational Metrics That Matter

### SaaS Metrics Hierarchy
**Level 1 - Survival**:
- Monthly Recurring Revenue (MRR)
- Burn rate
- Runway months

**Level 2 - Growth**:
- MRR growth rate
- Customer acquisition cost
- Churn rate

**Level 3 - Efficiency**:
- LTV/CAC ratio
- Gross margin
- CAC payback period

**Level 4 - Excellence**:
- Net revenue retention
- Sales efficiency
- Rule of 40

### Operational Health Scores

**Engineering Health**:
```
Score = (Deploy Frequency × Lead Time × MTTR × Change Failure Rate)^0.25
Excellent: >0.8
Good: 0.6-0.8
Needs Improvement: <0.6
```

**Customer Health**:
```
Score = (NPS + 100) / 200 × Retention Rate × Support Resolution Rate
Excellent: >0.8
Good: 0.6-0.8
Needs Improvement: <0.6
```

**Financial Health**:
```
Score = (Gross Margin × Growth Rate × Capital Efficiency)^0.33
Excellent: >0.5
Good: 0.3-0.5
Needs Improvement: <0.3
```

## Resource Allocation Framework

### 70-20-10 Rule
- 70%: Core business improvement
- 20%: Emerging opportunities
- 10%: Experimental/moonshots

### Engineering Time Allocation
- 60%: New features
- 20%: Technical debt
- 10%: Bug fixes
- 10%: Innovation time

### Marketing Budget Allocation
- 40%: Proven channels
- 30%: Scaling channels
- 20%: Testing channels
- 10%: Brand building