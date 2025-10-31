# Domain Expertise Compendium

## Technical Domain Patterns

### System Architecture Evolution

#### Stage 1: Monolith (0-100K users)
**Architecture**: Single application, single database
**Advantages**: Simple, fast development, easy debugging
**Challenges**: Scaling limits, deployment risk
**Key Decisions**: Framework selection, database choice
**Migration Trigger**: >100ms response times, deployment fear

#### Stage 2: Service-Oriented (100K-1M users)
**Architecture**: Multiple services, shared databases
**Advantages**: Independent scaling, team autonomy
**Challenges**: Distributed complexity, data consistency
**Key Decisions**: Service boundaries, communication protocols
**Migration Trigger**: Team conflicts, scaling bottlenecks

#### Stage 3: Microservices (1M-10M users)
**Architecture**: Many services, service-specific databases
**Advantages**: Full autonomy, polyglot, resilient
**Challenges**: Operational complexity, debugging difficulty
**Key Decisions**: Service mesh, observability stack
**Migration Trigger**: Innovation velocity, global scale

#### Stage 4: Platform (10M+ users)
**Architecture**: Platform services, edge computing
**Advantages**: Global scale, ecosystem enabling
**Challenges**: Extreme complexity, consistency
**Key Decisions**: Platform boundaries, API strategy

### Technology Selection Framework

**Language Selection Matrix**
```
Performance Critical: Rust, C++, Go
Rapid Development: Python, Ruby, JavaScript  
Enterprise: Java, C#, Go
Data/ML: Python, R, Scala
Systems: Rust, Go, C
Mobile: Swift, Kotlin, React Native
```

**Database Selection Criteria**
```
Transactional + Relational → PostgreSQL
Document + Flexible → MongoDB
Key-Value + Fast → Redis
Graph + Connected → Neo4j
Time-Series → InfluxDB, TimescaleDB
Analytics → ClickHouse, Snowflake
```

**Infrastructure Decisions**
```
<$10K MRR → Heroku, Vercel
$10-100K MRR → AWS/GCP with managed services
$100K-1M MRR → Kubernetes on cloud
>$1M MRR → Multi-cloud, owned infrastructure
```

## Financial Domain Patterns

### SaaS Financial Benchmarks

**Growth Stage Metrics**
```
Seed Stage:
- Growth: 20-30% MoM
- Burn Multiple: <4
- Runway: 18-24 months
- Efficiency: Not measured

Series A:
- Growth: 15-20% MoM  
- Burn Multiple: <2
- Gross Margin: >60%
- CAC Payback: <18 months

Series B:
- Growth: 10-15% MoM
- Burn Multiple: <1.5
- Gross Margin: >70%
- Net Retention: >100%

Series C+:
- Growth: T2D3 path
- Rule of 40: >40%
- Gross Margin: >75%
- Net Retention: >110%
```

### Valuation Methodologies

**Revenue Multiples by Growth Rate**
```
<20% growth: 1-3x ARR
20-40% growth: 3-6x ARR
40-60% growth: 6-10x ARR
60-100% growth: 10-15x ARR
>100% growth: 15-25x ARR
```

**Adjustments**
- Net Retention >120%: +20% premium
- Gross Margin >80%: +15% premium
- Category Leader: +30% premium
- High Churn: -30% discount
- Concentrated Revenue: -20% discount

### Unit Economics Framework

**LTV Calculation**
```
LTV = ARPU × Gross Margin × Customer Lifetime
Where Customer Lifetime = 1 / Churn Rate
```

**CAC Components**
```
CAC = (Sales Costs + Marketing Costs) / New Customers
Include: Salaries, ads, tools, overhead allocation
Exclude: Customer success, R&D, G&A
```

**Payback Period**
```
Payback = CAC / (ARPU × Gross Margin)
Excellent: <6 months
Good: 6-12 months
Acceptable: 12-18 months
Concerning: >18 months
```

## Legal Domain Patterns

### Regulatory Complexity by Industry

**Healthcare (Highest)**
- HIPAA compliance
- FDA approvals
- State licensing
- International standards
- Timeline: 2-10 years

**Financial Services (High)**
- SEC/FINRA oversight
- State regulations
- KYC/AML requirements
- International compliance
- Timeline: 1-3 years

**Education (Moderate-High)**
- FERPA compliance
- State certifications
- Accessibility requirements
- Title IX considerations
- Timeline: 6-18 months

**Consumer (Moderate)**
- FTC oversight
- Privacy laws (GDPR, CCPA)
- Product safety
- Advertising regulations
- Timeline: 3-12 months

**B2B SaaS (Lower)**
- Standard compliance (SOC2)
- Data privacy
- Contract law
- IP considerations
- Timeline: 3-6 months

### Intellectual Property Strategy

**Patent Strategy by Stage**
```
Pre-Product: Provisional patents only
MVP: Core innovation patents
Growth: Defensive portfolio
Scale: Offensive capabilities
Mature: Cross-licensing focus
```

**Trade Secret vs Patent Decision**
```
Trade Secret When:
- Reverse engineering difficult
- Competitive advantage >20 years
- Detection of infringement hard
- Core to competitive moat

Patent When:
- Reverse engineering easy
- Market advantage window <20 years
- Infringement detectable
- Licensing opportunity exists
```

## Industry-Specific Patterns

### B2B SaaS Patterns

**Sales Motion by ACV**
```
<$1K: Pure self-service
$1-10K: Product-led growth
$10-25K: Inside sales
$25-100K: Field sales hybrid
>$100K: Enterprise sales
```

**Expansion Strategy**
```
Land: Sell to team/department
Adopt: Prove value, increase usage
Expand: Adjacent teams/use cases
Renew: Multi-year, platform deal
```

### Marketplace Patterns

**Liquidity Strategies**
```
Single Player Mode: Value before network
Subsidize Supply: Pay/guarantee early suppliers
Aggregate Demand: Bring buyers in bulk
Make Market: Be buyer of last resort
Geographic Density: City by city expansion
```

**Take Rate Evolution**
```
Launch: 0-5% (maximize liquidity)
Growth: 5-15% (value established)
Scale: 15-25% (market power)
Mature: 20-30% (platform standard)
```

### Consumer Patterns

**Viral Mechanics**
```
K-Factor = Invites Sent × Conversion Rate
K > 1: Viral growth
K = 0.5-1: Strong word-of-mouth
K < 0.5: Paid acquisition needed
```

**Retention Benchmarks**
```
D1: >80% Great, <60% Problem
D7: >40% Great, <20% Problem
D30: >20% Great, <10% Problem
```

## Data & Analytics Patterns

### Analytics Maturity Model

**Level 1: Descriptive**
- What happened?
- Basic dashboards
- Historical reporting
- Tools: Google Analytics, Mixpanel

**Level 2: Diagnostic**
- Why did it happen?
- Drill-down capability
- Correlation analysis
- Tools: Amplitude, Tableau

**Level 3: Predictive**
- What will happen?
- ML models
- Forecasting
- Tools: DataRobot, H2O.ai

**Level 4: Prescriptive**
- What should we do?
- Optimization
- Automated decisions
- Tools: Custom ML, Reinforcement Learning

**Level 5: Cognitive**
- Autonomous optimization
- Self-learning systems
- AI-driven strategy
- Tools: Custom AI platforms

### ML/AI Readiness Assessment

**Data Requirements**
```
Minimum viable dataset:
- Supervised: 10,000+ labeled examples
- Unsupervised: 50,000+ examples
- Deep Learning: 100,000+ examples
- Reinforcement: Simulation environment
```

**Infrastructure Needs**
```
Experimentation: Jupyter, Colab
Production POC: Cloud ML services
Scale Production: Kubernetes + GPUs
Mission Critical: Dedicated ML platform
```

## Contrarian Perspectives

### When Conventional Wisdom Fails

**"First Mover Advantage"**
Reality: Fast follower often wins
- Google not first search engine
- Facebook not first social network
- iPhone not first smartphone
Examples: Better execution > first mover

**"Network Effects Moat"**
Reality: Networks can unravel quickly
- MySpace → Facebook
- WhatsApp disrupting SMS
- TikTok disrupting Instagram
Pattern: User experience > network size

**"Data is the New Oil"**
Reality: Most data is worthless
- Collection without purpose
- Privacy liability growing
- Algorithms matter more than quantity
Truth: Insights > data volume

**"Disruption From Below"**
Reality: Disruption from orthogonal
- iPhone disrupted from above (premium)
- Tesla disrupted from above (luxury)
- Uber disrupted from side (convenience)
Pattern: New dimension of value

**"Platform Always Wins"**
Reality: Platforms vulnerable to multi-homing
- Restaurants on multiple delivery apps
- Drivers on Uber and Lyft
- Sellers on Amazon and Shopify
Truth: Switching costs determine power

## Expert Knowledge Signatures

### How to Recognize True Expertise

**Technical Expert Tells**
- Knows why not just how
- Discusses tradeoffs not solutions
- Admits technical debt
- Has migration scars
- Mentions observability first

**Financial Expert Tells**
- Focuses on cash not revenue
- Discusses cohorts not averages
- Knows hidden costs
- Models scenarios not point estimates
- Understands investor psychology

**Legal Expert Tells**
- Prevents not just responds
- Knows judge/regulator tendencies
- Discusses precedent
- Identifies non-obvious risks
- Suggests structure creativity

**Industry Expert Tells**
- Knows unwritten rules
- Has competitor back-channels
- Understands customer politics
- Sees 2-3 moves ahead
- Recognizes patterns

**Product Expert Tells**
- Talks to users weekly
- Shows not tells
- Kills features ruthlessly
- Measures outcome not output
- Admits product failures